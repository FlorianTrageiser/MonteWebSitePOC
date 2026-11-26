"""Gemeinsame Inhalte für alle drei Entwürfe.

Texte stammen von https://montessori-erding.de (Stand November 2026),
teils gekürzt. Termine bitte vor Veröffentlichung prüfen.
"""

UP = "https://montessori-erding.de/wp-content/uploads"

IMG = {
    # Kinder arbeiten mit Montessori-Material (2400 px)
    "hero": "https://www.montessori-erding.de/wp-content/uploads/2025/04/Lernen_mit_Montessorimaterial.jpg",
    # Kinder spielen im verschneiten Garten des Kinderhauses
    "kinderhaus": f"{UP}/2022/10/DSC0241__3_.jpg",
    # Gruppenraum mit offenen Regalen im Kinderhaus
    "raum": f"{UP}/2022/10/DSC0169.jpg",
    # Grünes Klassenzimmer der Schule (2560 px)
    "schule": "https://www.montessori-erding.de/wp-content/uploads/2024/11/Montesssorieschule_Beschattung_gruenes_Klassenzimmer.doc-scaled.jpg",
    # Weltkarten-Puzzle
    "karte": f"{UP}/2022/10/DSC0175.jpg",
}

MATERIAL = [
    ("Rote Stangen", f"{UP}/2022/10/csm_rote_Stangen_2e3a87e727.jpg"),
    ("Geometrische Körper", f"{UP}/2022/10/csm_geometrische_Ko__rper_fb04b3fe61.jpg"),
    ("Goldenes Perlenmaterial", f"{UP}/2022/10/csm_goldenes_Perlenmaterial_f17cb55cd9.jpg"),
    ("Farbige Einsatzzylinder", f"{UP}/2022/10/csm_Farbige_Einsatzzylinder_757cbfe5c3.jpg"),
    ("Trinomischer Kubus", f"{UP}/2022/10/csm_trinomischer_Kubus_41c69cf033.jpg"),
    ("Planeten", f"{UP}/2022/10/csm_Planeten_725c72365b.jpg"),
]

LITTLE_BIRD = "https://portal.little-bird.de/erding"
MONTEMANAGER = "https://www.montemanager.de/login.php"

CONTACTS = [
    {
        "name": "Kinderhaus Erding",
        "sub": "Krippe & Kindergarten",
        "street": "Brachvogelweg 10",
        "city": "85435 Erding",
        "phone": "08122 54 02 80",
        "mail": "kinderhaus@montessori-erding.de",
    },
    {
        "name": "Schule Aufkirchen",
        "sub": "Montessori-Volksschule · 1. bis 10. Jahrgang",
        "street": "Pfarrer-Mittermair-Str. 75",
        "city": "85445 Aufkirchen",
        "phone": "08122 50 52",
        "mail": "schule@montessori-erding.de",
    },
    {
        "name": "Montessori-Verein",
        "sub": "Landkreis Erding e. V. · Geschäftsstelle",
        "street": "Pfarrer-Mittermair-Str. 75",
        "city": "85445 Aufkirchen",
        "phone": "08122 90 34 27",
        "mail": "gf@montessori-erding.de",
    },
]

# Kommende Termine (Stand 26.11.2026)
EVENTS = [
    {"d": "23", "m": "Jan", "y": "2027", "wd": "Samstag", "time": "10 – 14 Uhr",
     "title": "Tag der offenen Tür in der Schule", "place": "Schule Aufkirchen", "tag": "Schule"},
    {"d": "28", "m": "Jan", "y": "2027", "wd": "Donnerstag", "time": "19 Uhr",
     "title": "Infoabend für Eltern der ersten Klasse", "place": "Schule Aufkirchen", "tag": "Schule"},
    {"d": "03", "m": "Feb", "y": "2027", "wd": "Mittwoch", "time": "ganztägig",
     "title": "Anmeldeschluss erste Klasse 2027/28", "place": "Schule Aufkirchen", "tag": "Aufnahme"},
    {"d": "06", "m": "Feb", "y": "2027", "wd": "Samstag", "time": "10 – 13 Uhr",
     "title": "Tag der offenen Tür im Kinderhaus", "place": "Kinderhaus Erding", "tag": "Kinderhaus"},
    {"d": "23", "m": "Feb", "y": "2027", "wd": "Dienstag", "time": "14 – 15:30 Uhr",
     "title": "Schnuppertag für neue Erstklässler", "place": "Weitere Termine: 25. Februar und 3. März", "tag": "Aufnahme"},
    {"d": "13", "m": "Mär", "y": "2027", "wd": "Samstag", "time": "10 – 15 Uhr",
     "title": "Elternseminar zur Schulaufnahme (ohne Kinder)", "place": "Teil der Aufnahme in die erste Klasse", "tag": "Aufnahme"},
]

NEWS = [
    {"tag": "Jobs", "date": "Aktuell", "title": "Wir suchen eine Lehrkraft (m/w/d) für die Grundschule",
     "text": "Sie möchten Kinder auf ihrem eigenen Weg begleiten? Wir freuen uns auf Ihre Bewerbung.",
     "url": "https://montessori-erding.de/jobs/"},
    {"tag": "Verein", "date": "November 2026", "title": "Die neue MontePost ist online",
     "text": "Unsere Zeitung mit Geschichten aus Kinderhaus, Schule und Verein – für Mitglieder nach dem Login.",
     "url": "https://www.montessori-erding.de/monte-post/"},
    {"tag": "Schule", "date": "Juli 2024", "title": "30 Jahre Montessori-Volksschule Aufkirchen",
     "text": "Mit Festakt und Schulfest haben wir das Jubiläum unserer Schule gefeiert.",
     "url": "https://montessori-erding.de/schule/neuigkeiten/"},
    {"tag": "Verein", "date": "25. Oktober 2026", "title": "Markt der Künste 2026",
     "text": "Kunstschaffende zeigten in der Schule Aufkirchen ihre Arbeit und boten Handgemachtes an.",
     "url": "https://montessori-erding.de/verein/markt-der-kuenste/"},
    {"tag": "Schule", "date": "Juli 2025", "title": "11. Erdinger Schulschachcup",
     "text": "Über 110 Schülerinnen und Schüler kamen zum Turnier zusammen.",
     "url": "https://montessori-erding.de/bericht-zum-11-erdinger-schulschachcup-am-16-juli-2025/"},
]

VALUES = [
    "Gleiche Würde aller Menschen",
    "Demokratisches Handeln auf Basis des Grundgesetzes",
    "Erziehung zum Frieden",
    "Individualität in Gemeinschaft",
    "Einsatz für eine offene, vielfältige Gesellschaft",
]

# Weg durch die Einrichtungen
PATH = [
    {"age": "ab 1 Jahr", "name": "Kinderkrippe", "place": "Kinderhaus Erding",
     "text": "Montessori-Material und beziehungsvolle Pflege nach Emmi Pikler.", "page": "kinderhaus"},
    {"age": "3 – 6 Jahre", "name": "Kindergarten", "place": "Kinderhaus Erding",
     "text": "Vier Gruppen, Morgenkreis, Freiarbeit und viel Zeit im Garten.", "page": "kinderhaus"},
    {"age": "ab 6 Jahren", "name": "Schule", "place": "Schule Aufkirchen",
     "text": "Vom 1. bis zum 10. Jahrgang: altersgemischte Klassen und Freiarbeit.", "page": "schule"},
    {"age": "danach", "name": "Weiterführend", "place": "z. B. Montessori-FOS München",
     "text": "Der Verein hat die Fachoberschule 2007 mit anderen Montessori-Vereinen gegründet.", "page": "schule"},
]

PAGES = {
    "kinderhaus": {
        "nav": "Kinderhaus",
        "kicker": "Kinderhaus Erding",
        "title": "Unser Kinderhaus",
        "lead": "Ein Lebensraum für Kinder vom ersten Lebensjahr bis zur Einschulung – "
                "und für ihre Eltern, Pädagoginnen, Pädagogen und Therapeuten.",
        "img": IMG["raum"],
        "img_alt": "Gruppenraum mit offenen Regalen im Kinderhaus",
        "facts": [("2", "inklusive Krippengruppen"), ("4", "Kindergartengruppen"),
                  ("1", "Passivhaus mit Gründach"), ("1", "Garten mit Zugang aus jeder Gruppe")],
        "cta": ("Platz über Little Bird vormerken", LITTLE_BIRD),
        "sections": [
            {"title": "Kinderkrippe",
             "text": "In der Krippe kommen Montessori-Materialien und die beziehungsorientierte Pflege nach "
                     "Emmi Pikler zusammen. Schon beim Anziehen und Wickeln haben die Kinder Zeit, selbst "
                     "mitzumachen. Bewegung und freies Spiel gehören zum Tagesablauf.",
             "links": [("Konzept Kinderkrippe (PDF)", "https://www.montessori-erding.de/wp-content/uploads/2026/01/final_Monte_ED_Konzept_Kinderkrippe_2025.pdf")]},
            {"title": "Kindergarten",
             "text": "Kinder von drei bis sechs Jahren verbringen ihren Tag in vier Gruppen. Nach dem "
                     "Morgenkreis wählen sie in der Freiarbeit Material und Spielpartner. Gartenzeit und "
                     "gemeinsame Projekte ergänzen den Vormittag.",
             "links": [("Konzept Kindergarten (PDF)", "https://www.montessori-erding.de/wp-content/uploads/2026/01/Monte_ED_Konzept_Kindergarten_2026.pdf")]},
            {"title": "Pädagogik",
             "text": "Die Kinder wählen ihr Arbeitsmaterial selbst und entscheiden, wie lange sie sich damit "
                     "beschäftigen. Das Team gestaltet die Umgebung so, dass Kinder mit unterschiedlichen "
                     "Fähigkeiten am Alltag teilnehmen können.", "links": []},
            {"title": "Unser Haus",
             "text": "Das Kinderhaus ist ein zertifiziertes Passivhaus mit Gründach. Jede Gruppe hat eigenen "
                     "Zugang zum Garten – über Terrasse, Veranda oder Balkon. Dazu kommen Werkraum, "
                     "Bewegungsraum und ein gut ausgestatteter Therapieraum.", "links": []},
            {"title": "Eltern im Kinderhaus",
             "text": "Eltern und Team tauschen sich regelmäßig über das Kind aus. Familien bringen ihre "
                     "Fähigkeiten und Ideen in die Arbeit des Kinderhauses ein.",
             "links": [("Handzettel Elternarbeit (PDF)", f"{UP}/2022/10/Kinderhaus_Handzettel_Elternarbeit.pdf")]},
            {"title": "Wie lernen Kinder mit Montessori-Material?",
             "text": "Sie wählen eine Tätigkeit selbst, wiederholen sie und probieren in ihrem Tempo. "
                     "Erwachsene beobachten und zeigen bei Bedarf den nächsten Schritt.", "links": []},
        ],
        "docs": [
            ("Beitragstabelle ab 01.08.2026", f"{UP}/2026/07/Beitragstabelle_26_08.pdf"),
            ("Hausordnung", "https://www.montessori-erding.de/wp-content/uploads/2026/02/Hausordnung-Montessori-Kinderhaus-Erding_02.2026.pdf"),
            ("Schutzkonzept", "https://www.montessori-erding.de/wp-content/uploads/2024/09/Schutzkonzept-des-Montessori-Kinderhauses-in-Erding.pdf"),
            ("Beschwerdemanagement", "https://www.montessori-erding.de/wp-content/uploads/2025/01/Beschwerdemanagement-im-Montessori-Kinderhaus.pdf"),
        ],
        "contact": 0,
    },
    "schule": {
        "nav": "Schule",
        "kicker": "Schule Aufkirchen",
        "title": "Unsere Schule",
        "lead": "Eine staatlich anerkannte Montessori-Volksschule vom 1. bis zum 10. Jahrgang. Kinder lernen in "
                "altersgemischten Klassen – mit Freiarbeit, Verantwortung und Gemeinschaft.",
        "img": IMG["schule"],
        "img_alt": "Das grüne Klassenzimmer der Montessori-Schule",
        "facts": [("1–10", "Jahrgangsstufen unter einem Dach"), ("8:30", "bis 12:45 Uhr Unterricht am Vormittag"),
                  ("1–3", "Jahrgang mit Mittagsvilla"), ("4", "Schulbuslinien")],
        "cta": ("Alles zur Schulaufnahme", "termine.html#aufnahme"),
        "sections": [
            {"title": "Unterricht",
             "text": "Der Vormittagsunterricht dauert von 8:30 bis 12:45 Uhr. In altersgemischten "
                     "Lerngruppen lernen Kinder voneinander. In höheren Stufen kommt Nachmittagsunterricht hinzu.",
             "links": []},
            {"title": "Pädagogik",
             "text": "Freiarbeit gibt den Kindern Raum, Verantwortung für ihre Arbeit zu übernehmen. "
                     "Berichte zum Entwicklungs- und Lernprozess machen Fortschritte sichtbar.",
             "links": [("21 Fragen an Montessori-Schulen (PDF)", "https://www.montessori-erding.de/wp-content/uploads/2022/10/21FragenAnMontessoriSchulen.pdf")]},
            {"title": "Schulleben",
             "text": "Beim Schach planen Kinder ihre nächsten Züge, im Zirkus trainieren sie gemeinsam in der "
                     "Sporthalle. Im Schülerladen „Mandala“ erproben Jugendliche den Alltag eines Betriebs – "
                     "vom Verkauf bis zur Buchführung.",
             "links": [("Schach im Schulalltag", "https://montessori-erding.de/schule/schulleben/schach/schach-im-schulalltag/")]},
            {"title": "Ganztag",
             "text": "Für den ersten bis dritten Jahrgang gehört die Mittagsvilla zum Angebot. Dazu kommen "
                     "Arbeitsgemeinschaften am Nachmittag.",
             "links": [("AG-Beschreibungen", "https://montessori-erding.de/schule/ganztagesschule/ag-beschreibung/"),
                       ("FAQ Ganztag", "https://montessori-erding.de/schule/ganztagesschule/faq-ogts/")]},
            {"title": "Nachhaltigkeit",
             "text": "Auf dem Schulacker mit der GemüseAckerdemie und in Fairtrade-Projekten wird Nachhaltigkeit "
                     "praktisch erfahrbar. Die Schule engagiert sich außerdem bei UNESCO und „Schule ohne Rassismus – Schule mit Courage“.",
             "links": [("AckerSchule", "https://montessori-erding.de/schule/bildung-fuer-nachhaltige-entwicklung/ackerschule/")]},
            {"title": "Bildungsweg",
             "text": "Auf das Kinderhaus folgen die Schulstufen in Aufkirchen. Eine weiterführende Möglichkeit "
                     "ist die Montessori-Fachoberschule München, die unser Verein 2007 gemeinsam mit anderen Montessori-Vereinen gegründet hat.",
             "links": [("mos-muenchen.de", "https://www.mos-muenchen.de/")]},
        ],
        "docs": [
            ("Schulkonzept (PDF)", "https://www.montessori-erding.de/wp-content/uploads/2022/11/Konzept_Schule_Neu2014.pdf"),
            ("Schulbus Linie 1 · ab Moosburg", f"{UP}/2026/07/Linie-1-2026-2027.pdf"),
            ("Schulbus Linie 2 · ab Freising", f"{UP}/2026/07/Linie-2-2026-2027.pdf"),
            ("Schulbus Linie 3 · ab Anzing", f"{UP}/2026/07/Linie-3-2026-2027.pdf"),
            ("Schulbus Linie 4 · ab Markt Schwaben", f"{UP}/2026/09/Linie-4-2026-2027.pdf"),
        ],
        "contact": 1,
    },
    "verein": {
        "nav": "Verein",
        "kicker": "Montessori-Verein Landkreis Erding e. V.",
        "title": "Der Verein hinter allem",
        "lead": "Eltern, Pädagoginnen und Pädagogen tragen gemeinsam Kinderhaus und Schule. "
                "Der Verein schafft den Rahmen – organisatorisch und finanziell.",
        "img": IMG["hero"],
        "img_alt": "Kinder lernen mit Montessori-Material",
        "facts": [("2", "Einrichtungen"), ("30+", "Jahre Montessori im Landkreis"),
                  ("1", "Sozialfonds für faire Chancen"), ("6–10", "Jahre: Aufkirchner Sport-Ferien")],
        "cta": ("Verein unterstützen", "#unterstuetzen"),
        "sections": [
            {"title": "Gremien",
             "text": "Aufsichtsrat, Vorstand und Verwaltung arbeiten mit den Leitungen und den pädagogischen "
                     "Teams zusammen. Eltern wirken über ihre Vertretungen mit.", "links": []},
            {"title": "Markt der Künste",
             "text": "Kunstschaffende zeigen ihre Arbeit und bieten Handgefertigtes an. Der Markt 2026 fand am "
                     "25. Oktober statt.",
             "links": [("Zum Markt der Künste", "https://montessori-erding.de/verein/markt-der-kuenste/")]},
            {"title": "Aufkirchner Sport-Ferien",
             "text": "Das Ferienangebot an der Schule richtet sich an Kinder von sechs bis zehn Jahren. "
                     "Bewegung und gemeinsamer Sport stehen im Mittelpunkt.", "links": []},
            {"title": "Chronik",
             "text": "Von Maria Montessoris Leben bis zur Montessori-Arbeit hier vor Ort.",
             "links": [("Zur Chronik", "https://montessori-erding.de/verein/chronik/")]},
            {"title": "Presse",
             "text": "Die Geschäftsstelle ist Anlaufstelle für Presseanfragen und stellt Mitteilungen und "
                     "freigegebene Fotos bereit.",
             "links": [("Zum Pressebereich", "https://montessori-erding.de/verein/presse/")]},
            {"title": "Familienpakt Bayern",
             "text": "Der Verein ist Mitglied im Familienpakt Bayern und fördert Projekte wie „Zirkus macht stark“.",
             "links": [("Zirkus macht stark", "https://montessori-erding.de/zirkus-macht-stark/")]},
        ],
        "docs": [
            ("Spenden über Bildungsspender", "https://www.bildungsspender.de/montessori-erding"),
            ("Links & Partner", "https://montessori-erding.de/links/"),
            ("Stellenangebote", "https://montessori-erding.de/jobs/"),
        ],
        "donate": {
            "title": "Sozialfonds",
            "text": "Der Sozialfonds ermöglicht Kindern den Schulbesuch, deren Familien keine oder reduzierte "
                    "Beiträge zahlen. Am Jahresende gibt es eine Spendenquittung.",
            "iban": "DE80 7005 1995 0000 1526 37",
            "bank": "Sparkasse Erding/Dorfen",
            "ref": "Spende Montessori Sozialfonds",
        },
        "contact": 2,
    },
}

SCHOOL_DOCS = [
    ("Wichtige Termine 1. Klasse 2027/28 (PDF)", f"{UP}/2026/09/2027-2028-Wichtige-Termine-Ersties-1.pdf"),
    ("Voranmeldebogen Schulanfänger (PDF)", "https://www.montessori-erding.de/wp-content/uploads/2025/12/Voranmeldebogen-Schulanfaenger.pdf"),
    ("Voranmeldebogen Quereinsteiger (PDF)", "https://www.montessori-erding.de/wp-content/uploads/2025/12/Voranmeldebogen-Quereinsteiger.pdf"),
]

FOOTER_LINKS = [
    ("Termine", "termine"), ("Stellenangebote", "https://montessori-erding.de/jobs/"),
    ("Links & Partner", "https://montessori-erding.de/links/"), ("MonteManager", MONTEMANAGER),
    ("Impressum", "https://montessori-erding.de/impressum/"), ("Datenschutz", "https://montessori-erding.de/datenschutz/"),
]

NAV = [("Kinderhaus", "kinderhaus"), ("Schule", "schule"), ("Verein", "verein"),
       ("Termine & Aufnahme", "termine"), ("Kontakt", "kontakt")]
