"""Die drei Entwürfe: Startseiten und Eigenheiten je Version."""
from content import IMG, PATH, EVENTS, LITTLE_BIRD, PAGES
from dsl import G, H, P, A, Buttons, Img, UL, Raw
from common import (header, footer, events_list, news_grid, values_list, material_strip,
                    section_head, subpage, termine_page, kontakt_page, contact_card, ARROW)

FONT = "https://fonts.googleapis.com/css2?family="

# ------------------------------------------------------------------
# Version 1 · „Wurzeln“ – natürlich, warm, redaktionell
# ------------------------------------------------------------------
ARCH = ('<svg class="leaf" viewBox="0 0 120 120" aria-hidden="true"><path d="M20 100C20 50 55 20 100 20c0 45-30 80-80 80Z" '
        'fill="currentColor"/><path d="M24 96 92 28" stroke="var(--paper)" stroke-width="2" fill="none"/></svg>')


def v1_home():
    e = EVENTS[0]
    return [
        G("hero",
          G("hero-text",
            P("Montessori in Erding und Aufkirchen", "kicker"),
            H(1, "Ein Ort, an dem Kinder <em>wachsen</em> dürfen."),
            P("Vom ersten Entdecken in der Krippe bis zum selbstständigen Lernen in der Schule "
              "begleiten wir Kinder – und ihre Familien.", "lead"),
            Buttons([("Unsere Einrichtungen", "#einrichtungen", "primary"),
                     ("Termine & Aufnahme", "termine", "secondary")])),
          G("hero-media",
            Img(IMG["hero"], "Kinder im Montessori Kinderhaus Erding", "hero-img", eager=True),
            Raw(ARCH),
            G("hero-note",
              P("Nächster Termin", "kicker"),
              P(f'<strong>{e["d"]}. Januar</strong> · {e["title"]}'),
              P(A(f"Alle Termine {ARROW}", "termine", "more")))),
          tag="section"),
        G("path-section",
          section_head("Ein gemeinsamer Weg", "Vom ersten Jahr bis zur Schule – und darüber hinaus"),
          G("path", *[G("path-step",
                        P(s["age"], "path-age"), H(3, s["name"]), P(s["place"], "path-place"), P(s["text"]))
                      for s in PATH]),
          tag="section"),
        G("places",
          G("place",
            Img(IMG["kinderhaus"], "Das Kinderhaus in Erding", "place-img"),
            G("place-text",
              P("Erding · Krippe & Kindergarten", "kicker"),
              H(2, "Kinderhaus"),
              P("In einem Passivhaus mit Gründach und großem Garten lernen Kinder ab dem ersten Lebensjahr "
                "in ihrem eigenen Tempo. Jede Gruppe hat ihren eigenen Weg nach draußen."),
              UL(["Zwei inklusive Krippengruppen", "Vier Kindergartengruppen", "Online vormerken über Little Bird"], "checks"),
              P(A(f"Kinderhaus entdecken {ARROW}", "kinderhaus", "more")))),
          G("place place-reverse",
            Img(IMG["klassenzimmer"], "Das grüne Klassenzimmer der Schule", "place-img"),
            G("place-text",
              P("Aufkirchen · Volksschule", "kicker"),
              H(2, "Schule"),
              P("Altersgemischte Klassen, Freiarbeit und ein grünes Klassenzimmer: Hier übernehmen Kinder "
                "Verantwortung für ihr Lernen – und füreinander."),
              UL(["Unterricht von 8:30 bis 12:45 Uhr", "Mittagsvilla und AGs am Nachmittag", "Vier Schulbuslinien"], "checks"),
              P(A(f"Schule entdecken {ARROW}", "schule", "more")))),
          G("place-mini",
            P("Landkreis Erding", "kicker"),
            H(2, "Verein"),
            P("Hinter Kinderhaus und Schule steht der Montessori-Verein: Eltern, Pädagoginnen und Pädagogen, "
              "die gemeinsam Verantwortung tragen."),
            P(A(f"Verein kennenlernen {ARROW}", "verein", "more"))),
          tag="section", id="einrichtungen"),
        G("quote",
          Raw('<blockquote class="quote-text"><p>„Was Kinder betrifft, betrifft die Menschheit.“</p>'
              '<cite>Maria Montessori</cite></blockquote>'),
          tag="section"),
        G("split",
          G("split-col",
            section_head("Termine", "Bald bei uns"),
            events_list(3),
            P(A(f"Alle Termine & Aufnahme {ARROW}", "termine", "more"))),
          G("split-col",
            section_head("Aktuelles", "Neues aus Kinderhaus, Schule und Verein"),
            news_grid(3, "news-list")),
          tag="section"),
        G("material-section",
          section_head("Lernen mit den Händen", "Dinge, mit denen Kinder die Welt begreifen",
                       "Jedes Material hat seinen Platz im Regal. Die Kinder wählen selbst – und üben, bis es sitzt."),
          material_strip(), tag="section"),
        G("values-section",
          G("values-text",
            P("Unsere Haltung", "kicker"),
            H(2, "Für Vielfalt und Demokratie"),
            P("Gemeinsam mit allen Montessori-Einrichtungen in Bayern stehen wir für eine offene Gesellschaft. "
              "Das ist die Grundlage unserer pädagogischen Arbeit.")),
          values_list(), tag="section"),
    ]


# ------------------------------------------------------------------
# Version 2 · „Kompass“ – klar, modern, serviceorientiert
# ------------------------------------------------------------------
def topbar():
    return G("topbar",
             P(f'<span class="pill">Wir suchen</span> eine Lehrkraft (m/w/d) für die Grundschule '
               f'{A("Zur Stelle " + ARROW, "https://montessori-erding.de/jobs/")}', "topbar-msg"),
             P(f'{A("MonteManager", "https://www.montemanager.de/login.php")} · {A("Kontakt", "kontakt")}', "topbar-links"))


TASK_ICONS = {
    "baby": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M5 21c1-4 4-6 7-6s6 2 7 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "school": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9l9-5 9 5-9 5-9-5Z M7 11v5c3 2 7 2 10 0v-5" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
    "cal": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="17" height="15" rx="2" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M3.5 10h17M8 3v4M16 3v4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4Z" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"/></svg>',
}


def task(icon, title, text, ref):
    return Raw(f'<a class="task" href="{{{{{ref}}}}}"><span class="task-ico">{TASK_ICONS[icon]}</span>'
               f'<span class="task-text"><strong>{title}</strong><span>{text}</span></span>{ARROW}</a>')


def v2_home():
    return [
        G("hero",
          G("hero-text",
            P("Kinderhaus Erding · Schule Aufkirchen", "kicker"),
            H(1, "Montessori im Landkreis Erding"),
            P("Vom ersten Lebensjahr bis in die Schule: Kinder lernen bei uns selbstständig, "
              "in ihrem Tempo und in einer starken Gemeinschaft.", "lead"),
            G("hero-stats",
              P("<strong>ab 1 Jahr</strong><span>Krippe</span>"),
              P("<strong>4</strong><span>Kindergartengruppen</span>"),
              P("<strong>30 Jahre</strong><span>Montessori-Schule</span>"))),
          G("tasks",
            P("Was möchten Sie tun?", "tasks-title"),
            task("baby", "Kinderhausplatz vormerken", "Online über Little Bird", LITTLE_BIRD),
            task("school", "Kind für die Schule anmelden", "Erste Klasse 2027/28", "termine#aufnahme"),
            task("cal", "Tag der offenen Tür besuchen", "Schule: 23. Jan · Kinderhaus: 6. Feb", "termine"),
            task("chat", "Kontakt aufnehmen", "Telefon & E-Mail aller Einrichtungen", "kontakt")),
          tag="section"),
        G("photo-band",
          Img(IMG["hero"], "Kinder im Kinderhaus", "band-img band-a", eager=True),
          Img(IMG["lernen"], "Lernen mit Montessori-Material", "band-img band-b", eager=True),
          Img(IMG["klassenzimmer"], "Grünes Klassenzimmer", "band-img band-c", eager=True)),
        G("block",
          section_head("Unsere Einrichtungen", "Drei Bereiche, ein gemeinsames Ziel"),
          G("cards",
            *[G("card",
                Img(img, alt, "card-img"),
                G("card-body",
                  P(kicker, "kicker"), H(3, title), P(text),
                  UL(points, "card-points"),
                  P(A(f"Mehr erfahren {ARROW}", ref, "more"))))
              for img, alt, kicker, title, text, points, ref in [
                  (IMG["kinderhaus"], "Kinderhaus Erding", "Erding", "Kinderhaus",
                   "Krippe und Kindergarten für Kinder vom ersten Lebensjahr bis zur Einschulung.",
                   ["2 inklusive Krippengruppen", "4 Kindergartengruppen", "Passivhaus mit Garten"], "kinderhaus"),
                  (IMG["schule"], "Schule Aufkirchen", "Aufkirchen", "Schule",
                   "Staatlich anerkannte Volksschule mit altersgemischten Klassen und Freiarbeit.",
                   ["Unterricht 8:30 – 12:45 Uhr", "Ganztag mit Mittagsvilla", "4 Schulbuslinien"], "schule"),
                  (IMG["lernen"], "Lernen mit Montessori-Material", "Landkreis Erding", "Verein",
                   "Der Montessori-Verein ist Träger von Kinderhaus und Schule.",
                   ["Gremien & Mitwirkung", "Markt der Künste", "Sozialfonds"], "verein"),
              ]]),
          tag="section"),
        G("block block-tint",
          G("two-col",
            G("col",
              G("head-row", section_head("Termine", "Nächste Termine"),
                P(A(f"Alle Termine {ARROW}", "termine", "more"))),
              events_list(4)),
            G("col",
              G("head-row", section_head("Aktuelles", "Neuigkeiten"),
                P(A(f"Alle Neuigkeiten {ARROW}", "https://montessori-erding.de/schule/neuigkeiten/", "more"))),
              news_grid(4, "news-list"))),
          tag="section"),
        G("block",
          section_head("Pädagogik", "Montessori in drei Sätzen"),
          G("principles",
            *[G("principle", P(n, "principle-n"), H(3, t), P(x)) for n, t, x in [
                ("01", "Die Kinder wählen selbst.",
                 "In der Freiarbeit suchen sich Kinder ihre Aufgabe aus und arbeiten so lange daran, wie sie möchten."),
                ("02", "Groß und Klein lernen zusammen.",
                 "In altersgemischten Gruppen helfen Ältere Jüngeren – und lernen dabei selbst am meisten."),
                ("03", "Die Umgebung ist vorbereitet.",
                 "Material, Räume und Abläufe sind so gestaltet, dass Kinder selbstständig handeln können."),
            ]]),
          tag="section"),
        G("block block-dark",
          G("values-row",
            G("values-text", P("Unsere Haltung", "kicker"), H(2, "Für Vielfalt und Demokratie"),
              P("Gemeinsame Erklärung der Montessori-Einrichtungen des Landesverbands Bayern.")),
            values_list()),
          tag="section"),
    ]


# ------------------------------------------------------------------
# Version 3 · „Farbenspiel“ – bunt, lebendig, verspielt
# ------------------------------------------------------------------
SHAPES = '''<svg class="shapes" viewBox="0 0 520 460" aria-hidden="true">
  <g class="tower">
    <rect x="60" y="370" width="200" height="40" rx="6" fill="#ec8fa6"/>
    <rect x="80" y="330" width="160" height="40" rx="6" fill="#f2a6b8"/>
    <rect x="100" y="290" width="120" height="40" rx="6" fill="#ec8fa6"/>
    <rect x="120" y="250" width="80" height="40" rx="6" fill="#f2a6b8"/>
    <rect x="140" y="215" width="40" height="35" rx="6" fill="#ec8fa6"/>
  </g>
  <g class="rods">
    <rect x="290" y="392" width="200" height="18" rx="4" fill="#d9382b"/>
    <rect x="290" y="366" width="160" height="18" rx="4" fill="#2f62c9"/>
    <rect x="290" y="340" width="120" height="18" rx="4" fill="#d9382b"/>
    <rect x="290" y="314" width="80" height="18" rx="4" fill="#2f62c9"/>
    <rect x="290" y="288" width="40" height="18" rx="4" fill="#d9382b"/>
  </g>
  <circle class="sun" cx="390" cy="120" r="70" fill="#f2b632"/>
  <polygon class="tri" points="70,170 150,30 230,170" fill="#2f62c9"/>
  <g class="beads" fill="#e0a21a">
    <circle cx="300" cy="230" r="11"/><circle cx="324" cy="230" r="11"/><circle cx="348" cy="230" r="11"/>
    <circle cx="372" cy="230" r="11"/><circle cx="396" cy="230" r="11"/><circle cx="420" cy="230" r="11"/>
    <circle cx="444" cy="230" r="11"/>
  </g>
  <circle class="dot" cx="470" cy="300" r="16" fill="#3f9a5b"/>
</svg>'''

MINI = {
    "pink": '<svg viewBox="0 0 60 60" aria-hidden="true"><rect x="8" y="44" width="44" height="10" rx="2"/><rect x="14" y="33" width="32" height="10" rx="2"/><rect x="20" y="22" width="20" height="10" rx="2"/><rect x="25" y="12" width="10" height="9" rx="2"/></svg>',
    "blue": '<svg viewBox="0 0 60 60" aria-hidden="true"><polygon points="30,8 54,52 6,52"/></svg>',
    "yellow": '<svg viewBox="0 0 60 60" aria-hidden="true"><circle cx="30" cy="30" r="22"/></svg>',
}


TICKER = ('<span>Tag der offenen Tür Schule · 23. Januar 2027</span><span>✦</span>'
          '<span>Infoabend · 28. Januar 2027</span><span>✦</span><span>Tag der offenen Tür Kinderhaus · 6. Februar 2027</span>'
          '<span>✦</span><span>Wir suchen eine Lehrkraft (m/w/d)</span><span>✦</span>')


def v3_home():
    return [
        G("hero",
          G("hero-text",
            P("Montessori Erding · Kinderhaus & Schule", "kicker"),
            H(1, "„Hilf mir, es <span class='hl hl-1'>selbst</span> zu <span class='hl hl-2'>tun</span>.“"),
            P("Dieser Satz von Maria Montessori begleitet uns jeden Tag – in der Krippe, im Kindergarten "
              "und in der Schule in Aufkirchen.", "lead"),
            Buttons([("Los geht’s", "#bereiche", "primary"), ("Termine & Aufnahme", "termine", "secondary")])),
          G("hero-art", Raw(SHAPES)),
          tag="section"),
        G("ticker",
          Raw('<p class="ticker-text">' + TICKER + TICKER.replace('<span>', '<span aria-hidden="true">') + '</p>')),
        G("areas",
          section_head("Drei Orte, eine Idee", "Wo möchten Sie hin?"),
          G("area-grid",
            *[Raw(f'<a class="area area-{col}" href="{{{{{ref}}}}}"><span class="area-shape">{MINI[col]}</span>'
                  f'<span class="area-age">{age}</span><span class="area-title">{title}</span>'
                  f'<span class="area-text">{text}</span><span class="area-go">Entdecken {ARROW}</span></a>')
              for col, ref, age, title, text in [
                  ("pink", "kinderhaus", "ab 1 Jahr", "Kinderhaus", "Krippe & Kindergarten in Erding – mit Garten, Gründach und viel Zeit."),
                  ("blue", "schule", "ab 6 Jahren", "Schule", "Altersgemischt lernen in Aufkirchen – mit Freiarbeit und Schulacker."),
                  ("yellow", "verein", "für alle", "Verein", "Eltern und Team tragen gemeinsam Kinderhaus und Schule."),
              ]]),
          tag="section", id="bereiche"),
        G("how",
          G("how-head", section_head("So lernen Kinder bei uns", "Drei Dinge, die uns ausmachen")),
          G("how-grid",
            *[G(f"how-item how-{i}", Raw(f'<span class="beads-n" aria-hidden="true">{"".join("<i></i>" for _ in range(i))}</span>'),
                H(3, t), P(x)) for i, t, x in [
                (1, "Selbst wählen", "Kinder suchen sich ihre Arbeit aus und bleiben so lange dran, wie sie möchten."),
                (2, "Miteinander", "Ältere zeigen Jüngeren, wie es geht – und lernen dabei selbst."),
                (3, "Begreifen", "Mit Material zum Anfassen werden Zahlen, Formen und Wörter sichtbar."),
            ]]),
          tag="section"),
        G("material-section",
          section_head("Aus unseren Regalen", "Material zum Anfassen"),
          material_strip(), tag="section"),
        G("dates",
          G("dates-head", section_head("Termine", "Kommen Sie vorbei!"),
            Buttons([("Alle Termine", "termine", "secondary")])),
          events_list(4, "events tickets"),
          tag="section"),
        G("news-section",
          section_head("Aktuelles", "Was gerade passiert"),
          news_grid(4), tag="section"),
        G("values-section",
          G("values-text", P("Unsere Haltung", "kicker"), H(2, "Für Vielfalt und Demokratie")),
          values_list("values chips"), tag="section"),
    ]


VERSIONS = [
    {
        "slug": "v1",
        "theme": "montessori-wurzeln",
        "name": "Wurzeln",
        "claim": "Natürlich & warm",
        "desc": "Erdige Farben, große Fotos und eine ruhige, redaktionelle Sprache. "
                "Erzählt den Weg vom ersten Jahr bis zur Schule.",
        "fonts": FONT + "Fraunces:opsz,wght@9..144,400;9..144,600&family=Figtree:wght@400;500;600;700&display=swap",
        "swatch": ["#f6efe3", "#1f3a2f", "#c4532f", "#e9b949"],
        "home": v1_home,
        "header_extra": None,
        "tagline": "Ein Ort, an dem Kinder wachsen dürfen – in Erding und Aufkirchen.",
        "decor": None,
    },
    {
        "slug": "v2",
        "theme": "montessori-kompass",
        "name": "Kompass",
        "claim": "Klar & modern",
        "desc": "Hell, aufgeräumt und auf schnelle Orientierung gebaut: Eltern finden in einem Klick, "
                "was sie suchen – Platz vormerken, anmelden, Termine.",
        "fonts": FONT + "Inter:wght@400;500;600;700;800&display=swap",
        "swatch": ["#ffffff", "#0f1b33", "#1f56b8", "#e2412b"],
        "home": v2_home,
        "header_extra": topbar,
        "tagline": "Montessori-Pädagogik im Landkreis Erding – vom ersten Lebensjahr bis zur Schule.",
        "decor": None,
    },
    {
        "slug": "v3",
        "theme": "montessori-farbenspiel",
        "name": "Farbenspiel",
        "claim": "Bunt & lebendig",
        "desc": "Inspiriert von den Farben des Montessori-Materials: rosa Turm, rote Stangen, goldene Perlen. "
                "Fröhlich, verspielt und trotzdem gut lesbar.",
        "fonts": FONT + "Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600;6..12,700&display=swap",
        "swatch": ["#fff8ee", "#ec8fa6", "#2f62c9", "#f2b632"],
        "home": v3_home,
        "header_extra": None,
        "tagline": "Hilf mir, es selbst zu tun. Montessori in Erding und Aufkirchen.",
        "decor": Raw('<div class="page-decor" aria-hidden="true"><i class="d1"></i><i class="d2"></i><i class="d3"></i></div>'),
    },
]
