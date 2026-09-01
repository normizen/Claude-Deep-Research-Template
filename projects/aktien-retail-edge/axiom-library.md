# Axiom-Library — aktien-retail-edge

Axiome sind physikalische, logische oder strukturelle Grundwahrheiten über die Domäne,
die nicht durch Marktdynamik, Meinung oder Konvention entfernt werden können.

**Status-Legende:** Bestätigt (mehrfach unabhängig erarbeitet) | Tentativ (einmal, ungeprüft) | Widerlegt

Volltext mit Implikationen: `scratchpad/2026-08-30-aktien-retail-edge-strategic-axioms.md`

---

## Axiome

### A1: Aktie als Anspruch auf Zahlungsströme
**Formulierung:** Eine Aktie ist ein rechtlicher Anspruch auf einen anteiligen zukünftigen Zahlungsstrom eines Unternehmens (Dividenden, Rückkäufe, Liquidationserlös), keine bloße Wette auf einen Kursverlauf ohne Unterlegung.
**Entdeckt in Session:** 2026-08-30-aktien-retail-edge-strategic
**Status:** Tentativ
**Typ:** Strukturell (altert langsam)

### A2: Idiosynkratische Kursbewegung ist näherungsweise Zero-Sum netto Kosten
**Formulierung:** Zerlegt man eine Kursbewegung in systematischen und idiosynkratischen Anteil, ist der idiosynkratische Anteil auf Horizonten von Tagen bis wenigen Monaten strukturell ein Umverteilungsspiel unter den zu diesem Zeitpunkt Handelnden — abzüglich Transaktionskosten und Steuern, die real aus dem System abfließen.
**Entdeckt in Session:** 2026-08-30-aktien-retail-edge-strategic
**Status:** Tentativ
**Typ:** Strukturell
**Hinweis:** Widerspricht der pauschalen Erwartung, Aktien seien Positive-Sum und deshalb "einfacher" als Futures. Die Positive-Sum-Eigenschaft der Anlageklasse rettet kurzfristiges Stock-Picking nicht.

### A3: Preisfindung erfordert Berechnung — Berechnung kostet Zeit
**Formulierung:** Die Einpreisung neuer Information erfordert kognitive/rechnerische Verarbeitung durch handelnde Marktteilnehmer. Dieser Prozess hat eine physikalisch notwendige Nicht-Null-Dauer.
**Entdeckt in Session:** 2026-08-30-aktien-retail-edge-strategic
**Status:** Tentativ
**Typ:** Strukturell

### A4: Recherche-Aufmerksamkeit folgt Kapitalallokations-Ökonomie, nicht Informationsbedarf
**Formulierung:** Institutionelle Analysekapazität wird danach zugeteilt, wie viel Kapital sich in eine Position sinnvoll investieren lässt — nicht danach, wo das größte ungehobene Informationspotenzial liegt. Unternehmen unterhalb einer bestimmten Marktkapitalisierung sind für große Kapitalpools strukturell uninteressant zu covern, selbst bei hoher Ineffizienz.
**Entdeckt in Session:** 2026-08-30-aktien-retail-edge-strategic
**Status:** Tentativ
**Typ:** Strukturell
**Bedeutung:** Einer der beiden Mechanismen, die kleines Kapital vom Nachteil zum Segment-Selektor machen.

### A5: Marktwirkung skaliert mit Positionsgröße relativ zur Liquidität
**Formulierung:** Der Preis-Impact eines Trades ist eine Funktion der Ordergröße relativ zur Orderbuchtiefe. Unterhalb eines liquiditätsabhängigen Schwellenwerts bewegt eine Order den Preis nicht messbar gegen sich selbst; oberhalb tut sie es zwingend.
**Entdeckt in Session:** 2026-08-30-aktien-retail-edge-strategic
**Status:** Tentativ
**Typ:** Strukturell
**Bedeutung:** Zweiter Mechanismus des Segment-Selektor-Arguments.

### A6: Diversifikation reduziert nur unsystematisches Risiko
**Formulierung:** Der Diversifikationseffekt konvergiert gegen die systematische Marktvarianz und verschwindet nie vollständig, egal wie viele Positionen gehalten werden.
**Entdeckt in Session:** 2026-08-30-aktien-retail-edge-strategic
**Status:** Tentativ
**Typ:** Strukturell

### A7: Ein Stop-Loss garantiert keinen Ausstiegspreis, nur eine Ausführungsabsicht
**Formulierung:** Eine Stop-Loss-Order löst bei Erreichen der Schwelle eine Marktorder aus — sie garantiert Ausführung, nicht Preis. Bei Kurslücken (Overnight-Gap, Handelsunterbrechung, Liquiditätsentzug) kann der realisierte Verlust die geplante Grenze überschreiten.
**Entdeckt in Session:** 2026-08-30-aktien-retail-edge-strategic
**Status:** Tentativ
**Typ:** Strukturell
**Bedeutung:** Die harte User-Grenze "nie mehr verlieren als vorab riskiert" ist mit einer Stop-Order allein NICHT erfüllbar. Sie muss in die Sizing-Mathematik eingebaut werden.

### A8: Fundamentaler Wert ist nicht beobachtbar, nur schätzbar
**Formulierung:** Der wahre Unternehmenswert ist die Summe aller zukünftigen diskontierten Zahlungsströme — eine Größe, die per Definition erst in der Zukunft feststeht und in der Gegenwart nur geschätzt, nie gemessen werden kann.
**Entdeckt in Session:** 2026-08-30-aktien-retail-edge-strategic
**Status:** Tentativ
**Typ:** Strukturell

---

## Prüfung der geerbten Axiome aus `futures-trading-edge`

Durchgeführt in Phase 1, Session 2026-08-30. Volltext-Begründungen im Scratchpad.

| Futures-Axiom | Urteil | Kern der Begründung |
|---|---|---|
| A1(f) GEX als Dealer-Zwang | **EINGESCHRÄNKT** | Nur bei großen, optionsliquiden Namen — kaum im Kern-Zielraum dieses Projekts |
| A2(f) Orderflow als struktureller Einblick | **EINGESCHRÄNKT** | Mechanismus gilt, aber Aktien-Datenzugang ist fragmentiert und schwächer als bei Futures |
| A3(f) Kapital-Effizienz als Retail-Constraint | **ÜBERNOMMEN + ERWEITERT** | Kein monotoner Nachteil — kleines Kapital hat auch Vorteilszonen |
| A4(f) Zero-Sum mit asymmetrischen Kosten | **EINGESCHRÄNKT / WIDERSPRICHT** | Auf Instrumentenebene falsch für Aktien, auf Ebene der idiosynkratischen Bewegung strukturell zero-sum-artig → wurde zu neuem A2 |
| A5(f) Preis als instantaner Clearingpunkt | **WIDERSPRICHT (Kernprämisse)** | Aktien haben einen Fundamentalanker, den Futures nicht haben. Korollar zu technischen Indikatoren bleibt bestätigt |
| A6(f) Informations-Zeitwert fällt monoton | **ÜBERNOMMEN** | Trifft die Kernfrage "vor der Entfaltung einsteigen" direkt |
| A7(f) Kognitive Kapazität biologisch begrenzt | **ÜBERNOMMEN** | Unverändert gültig |
| A8(f) Regime-Nicht-Stationarität | **EINGESCHRÄNKT** | Prämisse gilt, Detektionsmechanismus über Orderflow bei Aktien fraglich |
| A9(f) Liquiditätsträger mit Hedging-Zwang | **VERWORFEN** | Für den Kern-Zielraum ungültig, nur in schmaler Randzone großer optionsliquider Werte |
