#!/usr/bin/env python3
"""Erzeugt
  docs/            statische Vorschau (GitHub Pages) aller drei Entwürfe
  themes/<name>/   je ein WordPress-Block-Theme pro Entwurf

Aufruf:  python3 build/build.py
"""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from content import PAGES  # noqa: E402
from dsl import Ctx, R, esc  # noqa: E402
from common import header, footer, subpage, termine_page, kontakt_page  # noqa: E402
from versions import VERSIONS  # noqa: E402

DOCS = os.path.join(ROOT, "docs")
THEMES = os.path.join(ROOT, "themes")

TITLES = {
    "index": "Startseite",
    "kinderhaus": "Kinderhaus",
    "schule": "Schule",
    "verein": "Verein",
    "termine": "Termine & Aufnahme",
    "kontakt": "Kontakt",
}


def css_for(v):
    base = open(os.path.join(HERE, "css", "base.css")).read()
    own = open(os.path.join(HERE, "css", f'{v["slug"]}.css')).read()
    head, rest = own.split("/*BASE*/", 1)
    return head + base + rest


def page_tree(v, key):
    if key == "index":
        return v["home"]()
    if key == "termine":
        return termine_page(v["decor"])
    if key == "kontakt":
        return kontakt_page(v["decor"])
    return subpage(key, v["decor"])


def header_tree(v, current):
    extra = v["header_extra"]() if v["header_extra"] else None
    return header(current, extra)


DEMO_CSS = """
.demo-bar{position:relative;z-index:50;display:flex;flex-wrap:wrap;gap:.5rem 1rem;align-items:center;justify-content:center;
 padding:.45rem 1rem;background:#111;color:#eee;font:500 13px/1.4 system-ui,-apple-system,sans-serif}
.demo-bar a{color:#fff;text-decoration:none;padding:.15rem .55rem;border-radius:99px;border:1px solid #444}
.demo-bar a[aria-current]{background:#fff;color:#111;border-color:#fff}
.demo-bar a:hover{border-color:#fff}
.demo-bar .demo-label{opacity:.75}
"""


def demo_bar(v):
    links = " ".join(
        f'<a href="../{o["slug"]}/index.html"{" aria-current=true" if o is v else ""}>{i + 1} · {o["name"]}</a>'
        for i, o in enumerate(VERSIONS))
    return (f'<div class="demo-bar"><span class="demo-label">Entwurf zur Ansicht – Montessori Erding</span>'
            f'{links}<a href="../index.html">Übersicht</a></div>')


def render_preview(v):
    out = os.path.join(DOCS, v["slug"])
    os.makedirs(out, exist_ok=True)
    c = Ctx("html")
    open(os.path.join(out, "style.css"), "w").write(css_for(v))
    for key, title in TITLES.items():
        body = R(page_tree(v, key), c)
        page_title = "Montessori Erding" if key == "index" else f"{title} · Montessori Erding"
        doc = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(page_title)}</title>
<meta name="description" content="Entwurf {esc(v['name'])}: Montessori Kinderhaus Erding, Schule Aufkirchen und Montessori-Verein Landkreis Erding e. V.">
<meta name="robots" content="noindex">
<link rel="icon" href="../assets/logo-figuren.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{v['fonts']}">
<link rel="stylesheet" href="style.css">
<style>{DEMO_CSS}</style>
</head>
<body class="{v['slug']} page-{key}">
<a class="skip-link" href="#main">Zum Inhalt springen</a>
{demo_bar(v)}
{R(header_tree(v, key), c)}
<main id="main">
{body}
</main>
{R(footer(v["tagline"]), c)}
</body>
</html>
"""
        with open(os.path.join(out, f"{key}.html"), "w") as f:
            f.write(doc)


def render_overview():
    cards = []
    for i, v in enumerate(VERSIONS):
        sw = "".join(f'<i style="background:{col}"></i>' for col in v["swatch"])
        cards.append(f"""<div class="ov-item"><a class="ov-card" href="{v['slug']}/index.html">
  <span class="ov-thumb" aria-hidden="true"><iframe src="{v['slug']}/index.html" tabindex="-1" loading="lazy" scrolling="no" title="Vorschau {esc(v['name'])}"></iframe></span>
  <span class="ov-body"><span class="ov-num">Entwurf {i + 1}</span>
  <span class="ov-name">{esc(v['name'])}</span><span class="ov-claim">{esc(v['claim'])}</span>
  <span class="ov-desc">{esc(v['desc'])}</span><span class="ov-sw">{sw}</span>
  <span class="ov-go">Ansehen →</span></span></a>
  <a class="ov-dl" href="downloads/{v['theme']}.zip">WordPress-Theme herunterladen (.zip)</a></div>""")
    doc = f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Website-Entwürfe · Montessori Erding</title>
<meta name="robots" content="noindex">
<link rel="icon" href="assets/logo-figuren.png">
<style>
:root{{--bg:#f4f1ec;--ink:#1a1a1a;--muted:#5d5d5d;--card:#fff;--line:#e2ddd5}}
@media (prefers-color-scheme:dark){{:root{{--bg:#151515;--ink:#f1f1f1;--muted:#b4b4b4;--card:#1f1f1f;--line:#333}}}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}}
.wrap{{max-width:1180px;margin:0 auto;padding:56px 20px 72px}}
header{{display:flex;gap:18px;align-items:center;margin-bottom:12px}}
header img{{width:64px;height:auto}}
h1{{font-size:clamp(28px,4vw,44px);line-height:1.1;margin:0;letter-spacing:-.02em}}
.intro{{color:var(--muted);max-width:60ch;margin:14px 0 40px;font-size:18px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px}}
.ov-card{{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;
 color:inherit;text-decoration:none;transition:transform .2s,box-shadow .2s}}
.ov-card:hover{{transform:translateY(-3px);box-shadow:0 18px 40px rgba(0,0,0,.12)}}
.ov-thumb{{display:block;position:relative;aspect-ratio:4/3;overflow:hidden;border-bottom:1px solid var(--line);background:#eee}}
.ov-thumb iframe{{position:absolute;top:0;left:0;width:1366px;height:1024px;border:0;transform-origin:0 0;transform:scale(var(--s,.27));pointer-events:none}}
.ov-body{{display:flex;flex-direction:column;gap:6px;padding:20px 22px 24px;flex:1}}
.ov-num{{font-size:13px;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}}
.ov-name{{font-size:26px;font-weight:700;letter-spacing:-.01em}}
.ov-claim{{font-weight:600}}
.ov-desc{{color:var(--muted)}}
.ov-sw{{display:flex;gap:6px;margin:8px 0 4px}}
.ov-sw i{{width:26px;height:26px;border-radius:50%;border:1px solid rgba(0,0,0,.15)}}
.ov-go{{margin-top:auto;padding-top:10px;font-weight:700}}
.ov-item{{display:flex;flex-direction:column;gap:10px}}
.ov-card{{flex:1}}
.ov-dl{{color:var(--muted);font-size:14px;padding-left:4px}}
.note{{margin-top:40px;color:var(--muted);font-size:14px;max-width:70ch}}
</style>
</head>
<body>
<div class="wrap">
<header><img src="assets/logo-figuren.png" alt=""><h1>Neue Website für Montessori Erding</h1></header>
<p class="intro">Drei Entwürfe mit den echten Inhalten der heutigen Website. Jeder Entwurf hat eine Startseite
und Unterseiten für Kinderhaus, Schule, Verein, Termine und Kontakt. Einfach anklicken und durchklicken.</p>
<div class="grid">
{''.join(cards)}
</div>
<p class="note">Hinweis: Das sind Entwürfe zur Ansicht. Fotos werden von montessori-erding.de geladen,
Termine und Texte bitte vor einer Veröffentlichung prüfen. Jeder Entwurf liegt auch als WordPress-Theme im Repository.</p>
</div>
<script>
function fit(){{document.querySelectorAll('.ov-thumb').forEach(t=>t.style.setProperty('--s',t.clientWidth/1366))}}
addEventListener('resize',fit);fit();
</script>
</body>
</html>
"""
    with open(os.path.join(DOCS, "index.html"), "w") as f:
        f.write(doc)


# ---------------------------------------------------------------- WordPress
def php_pattern(slug, title, markup, cats="", extra=""):
    return f"""<?php
/**
 * Title: {title}
 * Slug: {slug}
 * Categories: {cats}
 * Inserter: yes{extra}
 */
?>
{markup}
"""


def theme_json(v):
    css = open(os.path.join(HERE, "css", f'{v["slug"]}.css')).read()
    import re
    tokens = dict(re.findall(r"--([a-z0-9-]+):\s*(#[0-9a-fA-F]{3,8})", css.split("}")[0]))
    palette = [{"slug": k, "name": k.replace("-", " ").title(), "color": val} for k, val in tokens.items()]
    return {
        "$schema": "https://schemas.wp.org/wp/6.6/theme.json",
        "version": 3,
        "settings": {
            "appearanceTools": True,
            "useRootPaddingAwareAlignments": False,
            "layout": {"contentSize": "760px", "wideSize": "1240px"},
            "color": {"palette": palette, "defaultPalette": False, "defaultGradients": False},
            "typography": {"defaultFontSizes": False},
        },
        "styles": {"spacing": {"blockGap": "0px", "padding": {"top": "0", "bottom": "0", "left": "0", "right": "0"}}},
        "templateParts": [
            {"name": "header", "title": "Kopfbereich", "area": "header"},
            {"name": "footer", "title": "Fußbereich", "area": "footer"},
        ],
        "customTemplates": [],
    }


def render_theme(v):
    tdir = os.path.join(THEMES, v["theme"])
    if os.path.exists(tdir):
        shutil.rmtree(tdir)
    for sub in ("templates", "parts", "patterns", "assets"):
        os.makedirs(os.path.join(tdir, sub))
    c = Ctx("wp")
    slug = v["theme"]
    # Im Theme gibt es nur einen Entwurf: Präfix entfernen, damit die Stile auch im Editor greifen.
    css = css_for(v).replace("." + v["slug"] + " ", "")
    with open(os.path.join(tdir, "style.css"), "w") as f:
        f.write(f"""/*
Theme Name: Montessori Erding – {v['name']}
Theme URI: https://github.com/FlorianTrageiser/MonteWebSitePOC
Author: Montessori-Verein Landkreis Erding e. V.
Description: Entwurf „{v['name']}“ ({v['claim']}). {v['desc']}
Version: 0.1.0
Requires at least: 6.6
Tested up to: 6.8
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: {slug}
*/
{css}
/* WordPress-Anpassungen */
.wp-site-blocks{{padding:0}}
.wp-site-blocks > * + *{{margin-block-start:0}}
""")
    with open(os.path.join(tdir, "theme.json"), "w") as f:
        json.dump(theme_json(v), f, ensure_ascii=False, indent=2)
    with open(os.path.join(tdir, "functions.php"), "w") as f:
        f.write(f"""<?php
/**
 * Montessori Erding – {v['name']}
 */

add_action( 'wp_enqueue_scripts', function () {{
	wp_enqueue_style( '{slug}-fonts', '{v['fonts']}', array(), null );
	wp_enqueue_style( '{slug}', get_stylesheet_uri(), array(), wp_get_theme()->get( 'Version' ) );
}} );

add_filter( 'body_class', function ( $classes ) {{
	$classes[] = '{v['slug']}';
	return $classes;
}} );

add_action( 'after_setup_theme', function () {{
	add_editor_style( array( '{v['fonts']}', 'style.css' ) );
}} );

add_action( 'init', function () {{
	register_block_pattern_category( 'montessori', array( 'label' => 'Montessori Erding' ) );
	register_block_style( 'core/button', array( 'name' => 'primary', 'label' => 'Primär' ) );
	register_block_style( 'core/button', array( 'name' => 'secondary', 'label' => 'Sekundär' ) );
}} );
""")
    with open(os.path.join(tdir, "patterns", "header.php"), "w") as f:
        f.write(php_pattern(f"{slug}/header", "Kopfbereich", R(header_tree(v, None), c), "header", "\n * Block Types: core/template-part/header"))
    with open(os.path.join(tdir, "patterns", "footer.php"), "w") as f:
        f.write(php_pattern(f"{slug}/footer", "Fußbereich", R(footer(v["tagline"]), c), "footer", "\n * Block Types: core/template-part/footer"))
    for key, title in TITLES.items():
        name = "home" if key == "index" else f"seite-{key}"
        extra = "" if key == "index" else "\n * Post Types: page\n * Block Types: core/post-content"
        with open(os.path.join(tdir, "patterns", f"{name}.php"), "w") as f:
            f.write(php_pattern(f"{slug}/{name}", f"Seite: {title}", R(page_tree(v, key), c), "montessori", extra))
    w = lambda p, s: open(os.path.join(tdir, p), "w").write(s)  # noqa: E731
    w("parts/header.html", f'<!-- wp:pattern {{"slug":"{slug}/header"}} /-->\n')
    w("parts/footer.html", f'<!-- wp:pattern {{"slug":"{slug}/footer"}} /-->\n')
    hdr = '<!-- wp:template-part {"slug":"header","area":"header","tagName":"div"} /-->'
    ftr = '<!-- wp:template-part {"slug":"footer","area":"footer","tagName":"div"} /-->'
    w("templates/front-page.html", f"""{hdr}
<!-- wp:group {{"tagName":"main","anchor":"main","layout":{{"type":"default"}}}} -->
<main id="main" class="wp-block-group">
<!-- wp:pattern {{"slug":"{slug}/home"}} /-->
</main>
<!-- /wp:group -->
{ftr}
""")
    w("templates/page.html", f"""{hdr}
<!-- wp:group {{"tagName":"main","anchor":"main","layout":{{"type":"default"}}}} -->
<main id="main" class="wp-block-group">
<!-- wp:post-content {{"layout":{{"type":"default"}}}} /-->
</main>
<!-- /wp:group -->
{ftr}
""")
    single = f"""{hdr}
<!-- wp:group {{"tagName":"main","anchor":"main","className":"article","layout":{{"type":"default"}}}} -->
<main id="main" class="wp-block-group article">
<!-- wp:post-date {{"className":"kicker"}} /-->
<!-- wp:post-title {{"level":1}} /-->
<!-- wp:post-featured-image /-->
<!-- wp:post-content {{"layout":{{"type":"constrained"}}}} /-->
</main>
<!-- /wp:group -->
{ftr}
"""
    w("templates/single.html", single)
    w("templates/index.html", f"""{hdr}
<!-- wp:group {{"tagName":"main","anchor":"main","className":"article","layout":{{"type":"default"}}}} -->
<main id="main" class="wp-block-group article">
<!-- wp:heading {{"level":1}} -->
<h1 class="wp-block-heading">Aktuelles</h1>
<!-- /wp:heading -->
<!-- wp:query {{"queryId":1,"query":{{"perPage":10,"postType":"post","inherit":true}},"className":"news-grid"}} -->
<div class="wp-block-query news-grid">
<!-- wp:post-template -->
<!-- wp:group {{"className":"news-card","layout":{{"type":"default"}}}} -->
<div class="wp-block-group news-card">
<!-- wp:post-date {{"className":"news-meta"}} /-->
<!-- wp:post-title {{"level":3,"isLink":true}} /-->
<!-- wp:post-excerpt /-->
</div>
<!-- /wp:group -->
<!-- /wp:post-template -->
<!-- wp:query-pagination /-->
</div>
<!-- /wp:query -->
</main>
<!-- /wp:group -->
{ftr}
""")
    shutil.copy(os.path.join(HERE, "assets", "logo-figuren.png"), os.path.join(tdir, "assets", "logo-figuren.png"))
    shot = os.path.join(HERE, "assets", "screens", f'{v["slug"]}.jpg')
    if os.path.exists(shot):
        shutil.copy(shot, os.path.join(tdir, "screenshot.jpg"))
    w("README.md", f"""# Montessori Erding – {v['name']} ({v['claim']})

{v['desc']}

## Installation

1. Ordner `{slug}` als ZIP packen und unter *Design → Themes → Theme hochladen* installieren.
2. Seiten anlegen: Kinderhaus, Schule, Verein, Termine, Kontakt (Titelform = Adresse, z. B. `/kinderhaus/`).
3. Beim Anlegen einer Seite schlägt WordPress die passende Vorlage („Seite: Kinderhaus“ …) vor.
4. Unter *Einstellungen → Lesen* eine statische Startseite wählen – sie nutzt automatisch die Vorlage `front-page`.

Alle Abschnitte sind normale WordPress-Blöcke (Gruppen, Überschriften, Absätze, Buttons, Bilder)
und können im Editor bearbeitet werden. Die Gestaltung steckt in `style.css`.
""")


def zip_theme(v):
    import zipfile
    os.makedirs(os.path.join(DOCS, "downloads"), exist_ok=True)
    src = os.path.join(THEMES, v["theme"])
    with zipfile.ZipFile(os.path.join(DOCS, "downloads", f'{v["theme"]}.zip'), "w", zipfile.ZIP_DEFLATED) as z:
        for dp, _, files in os.walk(src):
            for fn in sorted(files):
                full = os.path.join(dp, fn)
                z.write(full, os.path.join(v["theme"], os.path.relpath(full, src)))


def main():
    os.makedirs(os.path.join(DOCS, "assets"), exist_ok=True)
    shutil.copy(os.path.join(HERE, "assets", "logo-figuren.png"), os.path.join(DOCS, "assets", "logo-figuren.png"))
    open(os.path.join(DOCS, ".nojekyll"), "w").close()
    for v in VERSIONS:
        render_preview(v)
        render_theme(v)
        zip_theme(v)
    render_overview()
    print("ok")


if __name__ == "__main__":
    main()
