"""Bausteine, die alle drei Entwürfe nutzen. Das Aussehen kommt aus dem
jeweiligen CSS; einzelne Entwürfe ergänzen eigene Abschnitte."""
from content import (CONTACTS, EVENTS, NEWS, PAGES, SCHOOL_DOCS, LITTLE_BIRD,
                     FOOTER_LINKS, NAV, VALUES, MATERIAL)
from dsl import G, H, P, A, Buttons, Img, UL, Raw, Nav

ARROW = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13m-5-6 6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
DOC = '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l5 5v13H7zM14 3v5h5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>'


def brand(name_html="Montessori <span>Erding</span>"):
    return Raw(
        f'<a class="brand" href="{{{{index}}}}" aria-label="Montessori Erding – Startseite">'
        f'<img src="__ASSET__logo-figuren.png" alt="" width="54" height="38"/>'
        f'<span class="brand-name">{name_html}</span></a>')


def header(current, extra_before=None, cta=("Aufnahme", "termine#aufnahme")):
    return G("site-header", extra_before,
             G("header-inner", brand(), Nav(NAV, current),
               Buttons([(cta[0], cta[1], "primary")], cls="header-cta")),
             tag="header")


def contact_card(i, cls="contact-card"):
    k = CONTACTS[i]
    return G(cls,
             H(3, k["name"]),
             P(k["sub"], "contact-sub"),
             P(f'{k["street"]}<br/>{k["city"]}'),
             P(f'<a href="tel:{k["phone"].replace(" ", "")}">{k["phone"]}</a><br/>'
               f'<a href="mailto:{k["mail"]}">{k["mail"]}</a>', "contact-links"))


def footer(tagline):
    links = " ".join(A(l, r) for l, r in FOOTER_LINKS)
    return G("site-footer",
             G("footer-inner",
               G("footer-brand", brand(), P(tagline, "footer-tagline")),
               G("footer-contacts", *[contact_card(i, "footer-contact") for i in range(3)]),
               ),
             G("footer-bottom", P(links, "footer-links"),
               P("© 2026 Montessori-Verein Landkreis Erding e. V.", "footer-copy")),
             tag="footer")


def event_item(e, cls="event"):
    return G(cls,
             Raw(f'<div class="event-date"><span class="event-d">{e["d"]}</span>'
                 f'<span class="event-m">{e["m"]}</span></div>'),
             G("event-body",
               P(f'<span class="tag tag-{e["tag"].lower()}">{e["tag"]}</span> {e["wd"]}, {e["time"]}', "event-meta"),
               H(3, e["title"]),
               P(e["place"], "event-place")))


def events_list(n=None, cls="events"):
    return G(cls, *[event_item(e) for e in EVENTS[:n]])


def news_card(n, cls="news-card"):
    return G(cls,
             P(f'<span class="tag">{n["tag"]}</span> <span class="news-date">{n["date"]}</span>', "news-meta"),
             H(3, A(n["title"], n["url"])),
             P(n["text"]))


def news_grid(n=None, cls="news-grid"):
    return G(cls, *[news_card(x) for x in NEWS[:n]])


def doc_list(docs, cls="doc-list"):
    return UL([A(l, r) for l, r in docs], cls)


def values_list(cls="values"):
    return UL(VALUES, cls)


def material_strip(cls="material"):
    return G(cls, *[Img(src, name, "material-item", caption=name) for name, src in MATERIAL])


def section_head(kicker, title, intro=None, cls="section-head", level=2):
    return G(cls,
             P(kicker, "kicker") if kicker else None,
             H(level, title),
             P(intro, "section-intro") if intro else None)


def page_hero(p, decor=None):
    return G("page-hero",
             G("page-hero-text",
               P(p["kicker"], "kicker"),
               H(1, p["title"]),
               P(p["lead"], "lead"),
               Buttons([(p["cta"][0], p["cta"][1], "primary"), ("Kontakt", "kontakt", "secondary")])),
             G("page-hero-media", Img(p["img"], p["img_alt"], "hero-img", eager=True), decor),
             tag="section")


def facts(p):
    return G("facts", *[G("fact", P(n, "fact-n"), P(t, "fact-t")) for n, t in p["facts"]],
             tag="section", label="Auf einen Blick")


def topic_grid(p):
    cards = []
    for s in p["sections"]:
        links = " ".join(A(l, r, "more") for l, r in s["links"])
        cards.append(G("topic", H(3, s["title"]), P(s["text"]), P(links, "topic-links") if links else None))
    return G("topics", *cards)


def subpage(key, decor=None, after_hero=None, between=None):
    p = PAGES[key]
    side = [G("aside-box", H(2, "Downloads & Links", "aside-title"), doc_list(p["docs"]))]
    side.append(G("aside-box aside-contact", H(2, "Ansprechpartner", "aside-title"), contact_card(p["contact"])))
    donate = None
    if p.get("donate"):
        d = p["donate"]
        donate = G("donate",
                   G("donate-text", P("Spenden & helfen", "kicker"), H(2, d["title"]), P(d["text"])),
                   G("donate-box",
                     P(f'<span>IBAN</span><strong>{d["iban"]}</strong>'),
                     P(f'<span>Bank</span>{d["bank"]}'),
                     P(f'<span>Verwendungszweck</span>{d["ref"]}')),
                   tag="section", id="unterstuetzen")
    gallery = None
    if key == "kinderhaus":
        gallery = G("page-section",
                    section_head("Lernen mit allen Sinnen", "Unser Material",
                                 "Ein Auszug aus den Materialien, mit denen die Kinder im Kinderhaus arbeiten."),
                    material_strip(), tag="section")
    return [
        page_hero(p, decor),
        facts(p),
        after_hero,
        G("page-body",
          G("page-main", section_head(None, "Das Wichtigste im Überblick"), topic_grid(p)),
          G("page-aside", *side, tag="aside"),
          tag="section"),
        between,
        gallery,
        donate,
    ]


def termine_page(decor=None):
    k, s = CONTACTS[0], CONTACTS[1]
    return [
        G("page-hero page-hero-simple",
          G("page-hero-text",
            P("Termine & Aufnahme", "kicker"),
            H(1, "Kennenlernen, vormerken, anmelden"),
            P("Hier finden Sie die nächsten Termine und die Schritte zur Aufnahme – "
              "für das Kinderhaus in Erding und die Schule in Aufkirchen.", "lead")),
          decor, tag="section"),
        G("page-section",
          section_head("Nächste Termine", "Was als Nächstes ansteht"),
          events_list(cls="events events-full"), tag="section"),
        G("page-section admission",
          section_head("Aufnahme", "So kommt Ihr Kind zu uns", cls="section-head"),
          G("admission-grid",
            G("admission-card",
              P("Kinderhaus Erding · ab 1 Jahr", "kicker"),
              H(3, "Krippe & Kindergarten"),
              UL(["Platz online über das Familienportal <strong>Little Bird</strong> der Stadt Erding vormerken.",
                  "Beim Tag der offenen Tür am 6. Februar 2027 Räume und Team kennenlernen.",
                  "Fragen zur Aufnahme beantwortet das Kinderhaus gerne – telefonisch oder per E-Mail."], "steps"),
              Buttons([("Bei Little Bird vormerken", LITTLE_BIRD, "primary")])),
            G("admission-card",
              P("Schule Aufkirchen · ab 6 Jahren", "kicker"),
              H(3, "Erste Klasse 2027/28"),
              UL(["Tag der offenen Tür am 23. Januar 2027 und Infoabend am 28. Januar 2027 um 19 Uhr besuchen – "
                  "beides ist Voraussetzung für die Aufnahme.",
                  "Voranmeldebogen bis zum 3. Februar 2027 abgeben (Bearbeitungsgebühr 50 €).",
                  "Schnuppertag (23. Februar, 25. Februar oder 3. März) und Elternseminar am 13. März 2027."], "steps"),
              doc_list(SCHOOL_DOCS))),
          tag="section", id="aufnahme"),
    ]


def kontakt_page(decor=None):
    return [
        G("page-hero page-hero-simple",
          G("page-hero-text",
            P("Kontakt", "kicker"),
            H(1, "Wir sind für Sie da"),
            P("Wählen Sie die Einrichtung, die Sie erreichen möchten. Wir melden uns so schnell wie möglich.", "lead")),
          decor, tag="section"),
        G("page-section",
          G("contact-grid", *[contact_card(i) for i in range(3)]), tag="section"),
        G("page-section",
          section_head("Arbeiten bei uns", "Stellenangebote",
                       "Offene Stellen in Kinderhaus und Schule veröffentlichen wir auf unserer Jobseite. "
                       "Derzeit sind alle Stellen besetzt."),
          Buttons([("Zu den Stellenangeboten", "https://montessori-erding.de/jobs/", "secondary")]),
          tag="section"),
    ]
