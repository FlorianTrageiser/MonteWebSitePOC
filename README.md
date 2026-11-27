# Montessori Erding – Website-Entwürfe

Fünf Entwürfe für eine neue Website von [montessori-erding.de](https://montessori-erding.de),
gebaut mit den echten Inhalten der heutigen Seite.

**Ansehen:** https://floriantrageiser.github.io/MonteWebSitePOC/

| Entwurf | Stil | Vorschau | WordPress-Theme |
|---|---|---|---|
| 1 · Wurzeln | natürlich & warm | [öffnen](https://floriantrageiser.github.io/MonteWebSitePOC/v1/index.html) | `themes/montessori-wurzeln` |
| 2 · Kompass | klar & modern | [öffnen](https://floriantrageiser.github.io/MonteWebSitePOC/v2/index.html) | `themes/montessori-kompass` |
| 3 · Farbenspiel | bunt & lebendig | [öffnen](https://floriantrageiser.github.io/MonteWebSitePOC/v3/index.html) | `themes/montessori-farbenspiel` |
| 4 · Atelier | ruhig & redaktionell, Menü links | [öffnen](https://floriantrageiser.github.io/MonteWebSitePOC/v4/index.html) | `themes/montessori-atelier` |
| 5 · Mosaik | modern, Kachel-Raster | [öffnen](https://floriantrageiser.github.io/MonteWebSitePOC/v5/index.html) | `themes/montessori-mosaik` |

Jeder Entwurf hat Startseite, Kinderhaus, Schule, Verein, Termine & Aufnahme und Kontakt.

## Aufbau

```
build/      Quelle: Inhalte (content.py), Seitenaufbau (common.py, versions.py), Gestaltung (css/)
docs/       erzeugte Vorschau für GitHub Pages (+ Theme-ZIPs in docs/downloads)
themes/     erzeugte WordPress-Block-Themes (eins pro Entwurf)
```

Vorschau und Theme kommen aus derselben Quelle: Jeder Abschnitt ist ein normaler
WordPress-Block (Gruppe, Überschrift, Absatz, Button, Bild) und lässt sich im Editor bearbeiten.

Neu erzeugen: `python3 build/build.py`

## WordPress

Theme-ZIP aus `docs/downloads/` unter *Design → Themes → Theme hochladen* installieren.
Seiten `kinderhaus`, `schule`, `verein`, `termine`, `kontakt` anlegen und die passende
Vorlage „Seite: …“ einfügen. Details im README des jeweiligen Themes.
Getestet mit WordPress 6.7 (lokal, SQLite).

## Hinweise

- Fotos werden direkt von montessori-erding.de geladen.
- Termine (Stand 26.11.2026) und Texte vor einer Veröffentlichung prüfen.
