"""Entwürfe 4 und 5: eigener Seitenaufbau (nicht nur andere Farben)."""
from content import IMG, EVENTS, NEWS, PAGES, CONTACTS, LITTLE_BIRD, NAV, VALUES, MATERIAL, PATH
from dsl import G, H, P, A, Buttons, Img, UL, Raw, Nav, Details
from common import (brand, contact_card, doc_list, events_list, news_grid, values_list, section_head,
                    material_strip, ARROW)

FONT = "https://fonts.googleapis.com/css2?family="
JOBS = "https://montessori-erding.de/jobs/"
MONTHS = {"Jan": "Januar", "Feb": "Februar", "Mär": "März"}


def anchor(title):
    import re
    t = title.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


# ==================================================================
# Entwurf 4 · Atelier – Menü links, Magazin-Layout, Schwarz/Weiß + Rot
# ==================================================================
def v4_header(current):
    return G("site-header side",
             G("side-top", brand("Montessori<br/><span>Erding</span>"), Nav(NAV, current)),
             G("side-bottom",
               Buttons([("Aufnahme 2027/28", "termine#aufnahme", "primary")], cls="header-cta"),
               P(A("<strong>Wir suchen</strong> eine Lehrkraft (m/w/d) für die Grundschule", JOBS), "side-job"),
               P("Kinderhaus Erding<br/>Schule Aufkirchen", "side-meta")),
             tag="header")


def v4_index_row(no, title, meta, text, ref, img, alt):
    return Raw(f'<a class="index-row" href="{{{{{ref}}}}}"><span class="index-no">{no}</span>'
               f'<span class="index-title">{title}</span><span class="index-meta">{meta}</span>'
               f'<span class="index-text">{text}</span>'
               f'<img class="index-img" src="{img}" alt="{alt}" loading="lazy"/>'
               f'<span class="index-go">{ARROW}</span></a>')


def v4_date_rows(events):
    rows = []
    for e in events:
        rows.append(G("date-row",
                      P(f'{e["d"]}. {MONTHS.get(e["m"], e["m"])} {e["y"]}', "date-when"),
                      H(3, e["title"]),
                      P(f'{e["wd"]}, {e["time"]}', "date-time"),
                      P(e["place"], "date-place")))
    return G("date-table", *rows)


def v4_home():
    return [
        G("cover",
          G("cover-text",
            P("Montessori in Erding und Aufkirchen", "kicker"),
            H(1, "Selbst entdecken.<br/><em>Gemeinsam wachsen.</em>"),
            P("Kinderhaus, Schule und Verein: Seit über 30 Jahren begleiten wir Kinder vom ersten Lebensjahr "
              "bis zum Schulabschluss – in ihrem eigenen Tempo.", "lead")),
          G("mosaic",
            Img(IMG["hero"], "Kinder lernen mit Montessori-Material", "m-a", eager=True),
            Img(IMG["kinderhaus"], "Kinder spielen im Garten des Kinderhauses", "m-b", eager=True),
            Img(IMG["karte"], "Weltkarten-Puzzle aus dem Montessori-Material", "m-c", eager=True)),
          tag="section"),
        G("index",
          P("Inhalt", "kicker"),
          v4_index_row("01", "Kinderhaus", "Erding · ab 1 Jahr",
                       "Krippe und Kindergarten im Passivhaus mit Garten.", "kinderhaus", IMG["raum"], ""),
          v4_index_row("02", "Schule", "Aufkirchen · 1. bis 10. Jahrgang",
                       "Altersgemischte Klassen, Freiarbeit, grünes Klassenzimmer.", "schule", IMG["schule"], ""),
          v4_index_row("03", "Verein", "Landkreis Erding e. V.",
                       "Die Gemeinschaft hinter Kinderhaus und Schule.", "verein", IMG["hero"], ""),
          v4_index_row("04", "Termine & Aufnahme", "Schuljahr 2027/28",
                       "Tag der offenen Tür, Infoabend, Anmeldung.", "termine", IMG["karte"], ""),
          tag="section"),
        G("dates",
          G("dates-head", P("Termine", "kicker"), H(2, "Im Kalender"),
            P(A("Alle Termine & Aufnahme", "termine", "more"))),
          v4_date_rows(EVENTS[:4]),
          tag="section"),
        G("statement",
          Raw('<blockquote class="big-quote"><p>„Was Kinder betrifft, betrifft die Menschheit.“</p>'
              '<cite>Maria Montessori</cite></blockquote>'),
          G("statement-values", P("Für Vielfalt und Demokratie", "kicker"), values_list()),
          tag="section"),
        G("journal",
          G("journal-head", P("Aktuelles", "kicker"), H(2, "Aus dem Schulleben")),
          news_grid(4, "news-grid columns"),
          tag="section"),
        G("shelf",
          G("shelf-head", P("Material", "kicker"), H(2, "Aus unseren Regalen")),
          material_strip("material scroller"),
          tag="section"),
    ]


def v4_subpage(key, decor=None):
    p = PAGES[key]
    toc = "".join(f'<li><a href="#{anchor(s["title"])}">{s["title"]}</a></li>' for s in p["sections"])
    rows = []
    for s in p["sections"]:
        links = " ".join(A(l, r, "more") for l, r in s["links"])
        rows.append(G("essay-row", H(2, s["title"]),
                      G("essay-text", P(s["text"]), P(links, "essay-links") if links else None),
                      tag="section", id=anchor(s["title"])))
    donate = None
    if p.get("donate"):
        d = p["donate"]
        donate = G("essay-row donate-row", H(2, d["title"]),
                   G("essay-text", P(d["text"]),
                     G("donate-box",
                       P(f'<span>IBAN</span><strong>{d["iban"]}</strong>'),
                       P(f'<span>Bank</span>{d["bank"]}'),
                       P(f'<span>Verwendungszweck</span>{d["ref"]}'))),
                   tag="section", id="unterstuetzen")
    material = None
    if key == "kinderhaus":
        material = G("essay-row", H(2, "Unser Material"), G("essay-text", material_strip("material scroller")),
                     tag="section", id="material")
    return [
        G("page-cover",
          P(p["kicker"], "kicker"),
          H(1, p["title"]),
          G("cover-cols", P(p["lead"], "lead"),
            Buttons([(p["cta"][0], p["cta"][1], "primary"), ("Kontakt", "kontakt", "secondary")])),
          Img(p["img"], p["img_alt"], "cover-img", eager=True),
          tag="section"),
        G("fact-line", *[G("fact", P(n, "fact-n"), P(t, "fact-t")) for n, t in p["facts"]], tag="section"),
        G("essay",
          G("toc", Raw(f'<nav aria-label="Auf dieser Seite"><p class="kicker">Auf dieser Seite</p><ol>{toc}</ol></nav>'),
            tag="aside"),
          G("essay-body", *rows, material, donate,
            G("essay-row", H(2, "Downloads"), G("essay-text", doc_list(p["docs"])), tag="section", id="downloads"),
            G("essay-row", H(2, "Kontakt"), G("essay-text", contact_card(p["contact"])), tag="section", id="kontakt")),
          tag="section"),
    ]


# ==================================================================
# Entwurf 5 · Mosaik – Kachel-Raster, schwebendes Menü, Petrol/Apricot/Flieder
# ==================================================================
def v5_header(current):
    return G("site-header float",
             G("header-inner", brand(), Nav(NAV, current),
               Buttons([("Aufnahme", "termine#aufnahme", "primary")], cls="header-cta")),
             tag="header")


def tile(cls, *children, tag="div"):
    return G("tile " + cls, *children, tag=tag)


def v5_home():
    e = EVENTS[0]
    return [
        G("bento",
          tile("t-hero",
               Img(IMG["hero"], "Kinder lernen mit Montessori-Material", "tile-bg", eager=True),
               G("tile-over",
                 P("Kinderhaus Erding · Schule Aufkirchen", "kicker"),
                 H(1, "Montessori im Landkreis Erding"),
                 P("Vom ersten Lebensjahr bis zum Schulabschluss – selbstständig lernen in einer starken Gemeinschaft.", "lead"),
                 Buttons([("Einrichtungen entdecken", "#bereiche", "primary"), ("Kontakt", "kontakt", "secondary")]))),
          tile("t-next",
               P("Nächster Termin", "kicker"),
               P(f'{e["d"]}<span>.{MONTHS[e["m"]][:3]}</span>', "big-date"),
               H(3, e["title"]),
               P(f'{e["wd"]}, {e["time"]} · {e["place"]}', "tile-small"),
               P(A("Alle Termine", "termine", "more"))),
          tile("t-cta",
               P("Kinderhaus", "kicker"),
               H(3, "Krippen- oder Kindergartenplatz vormerken"),
               P("Online über das Familienportal Little Bird der Stadt Erding.", "tile-small"),
               P(A("Zu Little Bird", LITTLE_BIRD, "more"))),
          tag="section"),
        G("bento", tile("t-title", P("Drei Bereiche", "kicker"), H(2, "Wo möchten Sie hin?")),
          Raw(f'<a class="tile t-photo t-kh" href="{{{{kinderhaus}}}}"><img src="{IMG["raum"]}" alt="" loading="lazy"/>'
              f'<span class="chip">ab 1 Jahr</span><span class="photo-label">Kinderhaus<small>Krippe & Kindergarten in Erding</small></span></a>'),
          Raw(f'<a class="tile t-photo t-sch" href="{{{{schule}}}}"><img src="{IMG["schule"]}" alt="" loading="lazy"/>'
              f'<span class="chip">1.–10. Jahrgang</span><span class="photo-label">Schule<small>Montessori-Volksschule Aufkirchen</small></span></a>'),
          Raw(f'<a class="tile t-photo t-ver" href="{{{{verein}}}}"><img src="{IMG["kinderhaus"]}" alt="" loading="lazy"/>'
              f'<span class="chip">für alle</span><span class="photo-label">Verein<small>Träger von Kinderhaus & Schule</small></span></a>'),
          tag="section", id="bereiche"),
        G("bento",
          tile("t-quote", Raw('<blockquote><p>„Hilf mir, es selbst zu tun.“</p><cite>Maria Montessori</cite></blockquote>')),
          tile("t-job", P("Stellenangebot", "kicker"), H(3, "Wir suchen eine Lehrkraft (m/w/d) für die Grundschule"),
               P(A("Zur Stellenanzeige", JOBS, "more"))),
          tile("t-dates", G("tile-head", H(2, "Termine"), P(A("Alle", "termine", "more"))), events_list(4, "events compact")),
          tile("t-news", G("tile-head", H(2, "Aktuelles"),
                           P(A("Mehr", "https://montessori-erding.de/schule/neuigkeiten/", "more"))),
               news_grid(4, "news-list")),
          tile("t-values", P("Unsere Haltung", "kicker"), H(3, "Für Vielfalt und Demokratie"), values_list()),
          tag="section"),
        G("bento",
          tile("t-material", G("tile-head", H(2, "Material zum Anfassen")), material_strip()),
          tag="section"),
    ]


def v5_subpage(key, decor=None):
    p = PAGES[key]
    colors = ["c-apricot", "c-lilac", "c-mint", "c-sky"]
    items = []
    for i, s in enumerate(p["sections"]):
        links = " ".join(A(l, r, "more") for l, r in s["links"])
        items.append(Details(s["title"], P(s["text"]), P(links, "acc-links") if links else None,
                             cls="acc", open=(i == 0)))
    extra = []
    if p.get("donate"):
        d = p["donate"]
        extra.append(tile("t-donate", P("Spenden & helfen", "kicker"), H(2, d["title"]), P(d["text"]),
                          G("donate-box",
                            P(f'<span>IBAN</span><strong>{d["iban"]}</strong>'),
                            P(f'<span>Bank</span>{d["bank"]}'),
                            P(f'<span>Verwendungszweck</span>{d["ref"]}'))))
    if key == "kinderhaus":
        extra.append(tile("t-material", G("tile-head", H(2, "Unser Material")), material_strip()))
    return [
        G("bento",
          tile("t-phead", P(p["kicker"], "kicker"), H(1, p["title"]), P(p["lead"], "lead"),
               Buttons([(p["cta"][0], p["cta"][1], "primary"), ("Kontakt", "kontakt", "secondary")])),
          tile("t-pimg", Img(p["img"], p["img_alt"], "tile-bg", eager=True)),
          *[tile(f"t-fact {colors[i % 4]}", P(n, "fact-n"), P(t, "fact-t")) for i, (n, t) in enumerate(p["facts"])],
          tag="section"),
        G("bento",
          tile("t-acc", G("tile-head", H(2, "Das Wichtigste im Überblick")), G("accordion", *items)),
          tile("t-side",
               G("side-box", H(3, "Downloads & Links"), doc_list(p["docs"])),
               G("side-box side-contact", H(3, "Ansprechpartner"), contact_card(p["contact"]))),
          *extra,
          tag="section", id="unterstuetzen" if p.get("donate") else None),
    ]


MORE = [
    {
        "slug": "v4",
        "theme": "montessori-atelier",
        "name": "Atelier",
        "claim": "Ruhig & redaktionell",
        "desc": "Menü links an der Seite wie in einem Magazin, viel Weißraum, große Schrift, Schwarz-Weiß mit "
                "dem Rot aus dem Logo. Unterseiten mit Inhaltsverzeichnis.",
        "fonts": FONT + "Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700&display=swap",
        "swatch": ["#fbfaf7", "#121212", "#d7261e", "#1f4ea1"],
        "home": v4_home,
        "header": v4_header,
        "header_extra": None,
        "subpage": v4_subpage,
        "tagline": "Selbst entdecken. Gemeinsam wachsen. Montessori in Erding und Aufkirchen.",
        "decor": None,
    },
    {
        "slug": "v5",
        "theme": "montessori-mosaik",
        "name": "Mosaik",
        "claim": "Modern & übersichtlich",
        "desc": "Alles auf einen Blick in Kacheln wie auf einer Pinnwand. Schwebendes Menü, Petrol mit Apricot "
                "und Flieder. Unterseiten mit aufklappbaren Themen.",
        "fonts": FONT + "Outfit:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap",
        "swatch": ["#f3efe7", "#12403f", "#ffb48a", "#cdbdff"],
        "home": v5_home,
        "header": v5_header,
        "header_extra": None,
        "subpage": v5_subpage,
        "tagline": "Montessori im Landkreis Erding – vom ersten Lebensjahr bis zum Schulabschluss.",
        "decor": None,
    },
]
