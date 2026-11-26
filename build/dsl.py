"""Kleine Baumstruktur, die sich als statisches HTML (Vorschau) oder als
WordPress-Blockmarkup (Theme-Patterns) ausgeben lässt. So bleibt die
Vorschau 1:1 das, was das Theme in WordPress erzeugt."""
import html
import json

PAGES = {"index", "kinderhaus", "schule", "verein", "termine", "kontakt"}


class Ctx:
    def __init__(self, target):
        self.target = target  # "html" | "wp"

    def link(self, ref):
        if ref.startswith(("http", "mailto:", "tel:")):
            return ref
        anchor = ""
        if "#" in ref:
            ref, anchor = ref.split("#", 1)
            anchor = "#" + anchor
        if ref.endswith(".html"):
            ref = ref[:-5]
        if ref == "":
            return anchor
        if ref in PAGES:
            if self.target == "html":
                return f"{ref}.html{anchor}"
            return ("/" if ref == "index" else f"/{ref}/") + anchor
        return ref + anchor

    def asset(self, name):
        if self.target == "html":
            return f"../assets/{name}"
        return f"<?php echo esc_url( get_theme_file_uri( 'assets/{name}' ) ); ?>"


def esc(t):
    return html.escape(t, quote=True)


def attrs_json(d):
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))


class Node:
    def render(self, c):
        raise NotImplementedError


def R(x, c):
    if x is None:
        return ""
    if isinstance(x, (list, tuple)):
        return "\n".join(R(i, c) for i in x if i is not None)
    if isinstance(x, str):
        return x
    return x.render(c)


class G(Node):
    """Gruppe (wp:group)."""

    def __init__(self, cls, *children, tag="div", id=None, label=None):
        self.cls, self.children, self.tag, self.id, self.label = cls, children, tag, id, label

    def render(self, c):
        inner = R(list(self.children), c)
        idattr = f' id="{self.id}"' if self.id else ""
        lab = f' aria-label="{esc(self.label)}"' if self.label else ""
        el = f'<{self.tag}{idattr}{lab} class="wp-block-group {self.cls}">\n{inner}\n</{self.tag}>'
        if c.target == "html":
            return el
        a = {"className": self.cls, "layout": {"type": "default"}}
        if self.tag != "div":
            a["tagName"] = self.tag
        if self.id:
            a["anchor"] = self.id
        return f"<!-- wp:group {attrs_json(a)} -->\n{el}\n<!-- /wp:group -->"


class H(Node):
    def __init__(self, level, text, cls=""):
        self.level, self.text, self.cls = level, text, cls

    def render(self, c):
        cl = ("wp-block-heading " + self.cls).strip()
        el = f'<h{self.level} class="{cl}">{self.text}</h{self.level}>'
        if c.target == "html":
            return el
        a = {"level": self.level}
        if self.cls:
            a["className"] = self.cls
        return f"<!-- wp:heading {attrs_json(a)} -->\n{el}\n<!-- /wp:heading -->"


class P(Node):
    """Absatz. Text darf Inline-HTML enthalten; Links mit {{ref}} werden aufgelöst."""

    def __init__(self, text, cls=""):
        self.text, self.cls = text, cls

    def render(self, c):
        t = resolve_inline(self.text, c)
        cl = f' class="{self.cls}"' if self.cls else ""
        el = f"<p{cl}>{t}</p>"
        if c.target == "html":
            return el
        a = {"className": self.cls} if self.cls else {}
        aj = " " + attrs_json(a) if a else ""
        return f"<!-- wp:paragraph{aj} -->\n{el}\n<!-- /wp:paragraph -->"


def resolve_inline(t, c):
    import re
    return re.sub(r"\{\{([^}]+)\}\}", lambda m: esc(c.link(m.group(1))), t)


def A(label, ref, cls=""):
    """Inline-Link als String für P()."""
    cl = f' class="{cls}"' if cls else ""
    ext = ' target="_blank" rel="noopener"' if ref.startswith("http") and ref.endswith(".pdf") else ""
    return f'<a{cl} href="{{{{{ref}}}}}"{ext}>{label}</a>'


class Buttons(Node):
    def __init__(self, items, cls=""):
        # items: (label, ref, variant)  variant: "primary"|"secondary"|"ghost"
        self.items, self.cls = items, cls

    def render(self, c):
        btns = []
        for label, ref, variant in self.items:
            href = esc(c.link(ref))
            b = (f'<div class="wp-block-button is-style-{variant}"><a class="wp-block-button__link wp-element-button" '
                 f'href="{href}">{label}</a></div>')
            if c.target == "wp":
                b = f'<!-- wp:button {attrs_json({"className": "is-style-" + variant})} -->\n{b}\n<!-- /wp:button -->'
            btns.append(b)
        el = f'<div class="wp-block-buttons {self.cls}">\n' + "\n".join(btns) + "\n</div>"
        if c.target == "html":
            return el
        a = {"className": self.cls} if self.cls else {}
        aj = " " + attrs_json(a) if a else ""
        return f"<!-- wp:buttons{aj} -->\n{el}\n<!-- /wp:buttons -->"


class Img(Node):
    def __init__(self, src, alt, cls="", asset=False, caption=None, eager=False):
        self.src, self.alt, self.cls, self.asset, self.caption, self.eager = src, alt, cls, asset, caption, eager

    def render(self, c):
        src = c.asset(self.src) if self.asset else self.src
        load = "" if self.eager else ' loading="lazy"'
        cap = f'<figcaption class="wp-element-caption">{self.caption}</figcaption>' if self.caption else ""
        el = (f'<figure class="wp-block-image size-large {self.cls}"><img src="{src}" alt="{esc(self.alt)}"'
              f'{load} decoding="async"/>{cap}</figure>')
        if c.target == "html":
            return el
        a = {"sizeSlug": "large"}
        if self.cls:
            a["className"] = self.cls
        return f"<!-- wp:image {attrs_json(a)} -->\n{el}\n<!-- /wp:image -->"


class UL(Node):
    def __init__(self, items, cls=""):
        self.items, self.cls = items, cls

    def render(self, c):
        lis = []
        for it in self.items:
            li = f"<li>{resolve_inline(it, c)}</li>"
            if c.target == "wp":
                li = f"<!-- wp:list-item -->\n{li}\n<!-- /wp:list-item -->"
            lis.append(li)
        el = f'<ul class="wp-block-list {self.cls}">\n' + "\n".join(lis) + "\n</ul>"
        if c.target == "html":
            return el
        a = {"className": self.cls} if self.cls else {}
        aj = " " + attrs_json(a) if a else ""
        return f"<!-- wp:list{aj} -->\n{el}\n<!-- /wp:list -->"


class Raw(Node):
    """Freies HTML (z. B. SVG-Dekor). In WordPress als wp:html-Block."""

    def __init__(self, markup):
        self.markup = markup

    def render(self, c):
        import re
        m = resolve_inline(self.markup, c)
        m = re.sub(r"__ASSET__([\w.\-]+)", lambda x: c.asset(x.group(1)), m)
        if c.target == "html":
            return m
        return f"<!-- wp:html -->\n{m}\n<!-- /wp:html -->"


class Nav(Node):
    """Hauptnavigation: statisch in der Vorschau, wp:navigation im Theme."""

    def __init__(self, items, current=None, cls="main-nav"):
        self.items, self.current, self.cls = items, current, cls

    def render(self, c):
        if c.target == "wp":
            links = "\n".join(
                f'<!-- wp:navigation-link {attrs_json({"label": l, "url": c.link(r), "kind": "custom"})} /-->'
                for l, r in self.items)
            a = {"overlayMenu": "mobile", "className": self.cls, "layout": {"type": "flex", "justifyContent": "right"}}
            return f"<!-- wp:navigation {attrs_json(a)} -->\n{links}\n<!-- /wp:navigation -->"
        lis = "".join(
            f'<li><a href="{esc(c.link(r))}"{" aria-current=page" if r == self.current else ""}>{l}</a></li>'
            for l, r in self.items)
        return (f'<nav class="{self.cls}" aria-label="Hauptmenü">'
                f'<details class="nav-toggle"><summary aria-label="Menü öffnen"><span></span><span></span><span></span></summary>'
                f'<ul>{lis}</ul></details><ul class="nav-desktop">{lis}</ul></nav>')
