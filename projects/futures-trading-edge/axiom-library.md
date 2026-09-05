# Axiom-Library — futures-trading-edge

## Format
Jedes Axiom: Titel | Status | Quelle | Begründung warum es ein Axiom ist (nicht argumentierbar)

---

## Axiome

### A1: GEX als mechanischer Dealer-Zwang
**Status:** Bestätigt (2x unabhängig erarbeitet)
**Quelle:** Explorer-Session 2026-03-30, arXiv:2512.17923 (91.2% Materialization Accuracy); Session 2026-04-15 First Principles
**Begründung:** Dealer-Hedging ist durch regulatorische Eigenkapitalvorschriften + Options-Preistheorie (Black-Scholes-Delta) deterministisch erzwungen. Kein Entscheidungsspielraum. GEX beschreibt mechanische Zwangsnachfrage, keine statistische Heuristik — der Unterschied ist epistemisch fundamental.
**Erweiterung (2026-04-15):** GEX ist Mechanik-Indikator, nicht Sentiment-Indikator. Mechanik ist deterministisch vorhersagbar. Das macht GEX-basierte Predictions strukturell anders belastbar als statistische Korrelationen.

### A2: Orderflow gibt strukturelle Markteinblicke (bedingt)
**Status:** Bestätigt, erweitert
**Quelle:** Explorer-Session 2026-03-30, arXiv:2507.22712; Session 2026-04-15 First Principles (A9)
**Begründung:** Bid/Ask-Volume, CVD und DOM reflektieren tatsächliche Handelsabsichten. 95% Cancellation-Rate macht rohe DOM-Analyse unzureichend — aber das Verhältnis zwischen platzierten und ausgeführten Orders ist selbst ein Signal. DOM ist bedingt informativ — nach korrektem Filter. Filterung ist nicht optional.

### A3: Kapital-Effizienz ist Retail-Constraint
**Status:** Bestätigt, erweitert
**Quelle:** User-Interview 2026-04-15; Session 2026-04-15 First Principles (A7)
**Begründung:** Mit ~10.000 EUR Kapital und ohne Overnight-Exposure ist Leverage-Effizienz und Position-Sizing ein fundamentaler Constraint. Erweitert: Kapitalgröße bestimmt den gesamten Möglichkeitsraum der Strategien — nicht nur die Positionsgröße. Institutionelle Edge-Konzepte sind ohne Kapitalanpassung für Retail strukturell nicht replizierbar.

### A4: Zero-Sum-Struktur mit asymmetrischen Transaktionskosten
**Status:** Tentativ (neu 2026-04-15)
**Quelle:** Session 2026-04-15 First Principles (A1)
**Begründung:** Futures-Märkte sind strukturell Zero-Sum: jeder realisierte Gewinn entspricht dem Verlust eines anderen, zuzüglich Transaktionskosten. Retail-Trader tragen durch Spread und Gebühren höhere Kostenlast als institutionelle Teilnehmer. Neutral zu spielen (kein Edge) bedeutet bei Retail systematisch verlieren. Ein positiver Erwartungswert muss Gebühren explizit überkompensieren.

### A5: Preis als instantaner Clearingpunkt (kein intrinsischer Informationswert)
**Status:** Tentativ (neu 2026-04-15)
**Quelle:** Session 2026-04-15 First Principles (A2)
**Begründung:** Preis ist ausschließlich der Punkt wo Käufer und Verkäufer im Moment übereinstimmen — enthält keine inhärente Information über zukünftige Bewegung. Jeder Indikator der aus Preis allein abgeleitet wird (MA, RSI etc.) enthält strukturell keine neue Information. Echter Edge muss aus dem Prozess kommen der Preise erzeugt: Orderflow, Positionierung, mechanische Zwänge.

### A6: Informations-Zeitwert fällt monoton
**Status:** Tentativ (neu 2026-04-15)
**Quelle:** Session 2026-04-15 First Principles (A4)
**Begründung:** Informativer Vorsprung sinkt monoton sobald Information für andere zugänglich wird. Öffentliche Information hat nach Arbitrage Preiswert null. Edge liegt nicht in der Information selbst, sondern in: (a) Timing des Zugangs, (b) Synthesekapazität (Kombination die andere nicht machen), (c) Erkennen mechanischer Konsequenzen die andere übersehen.

### A7: Kognitive Kapazität ist biologisch begrenzt — Systematisierung ist strukturelle Notwendigkeit
**Status:** Tentativ (neu 2026-04-15)
**Quelle:** Session 2026-04-15 First Principles (A6)
**Begründung:** Menschliches Working Memory: 7±2 Chunks, Decision Fatigue durch Cortisol-Depletion — empirisch dokumentiert. Eine Strategie die mehr simultane Variablen verfolgt als menschliche Kognition verarbeiten kann, versagt in Echtzeit-Execution unabhängig von theoretischer Validität. Externalisierung in Code/Regeln ist keine Optimierung — sie ist strukturell notwendig für Konsistenz.

### A8: Regime-Nicht-Stationarität mit messbarem Orderflow-Fingerabdruck
**Status:** Tentativ (neu 2026-04-15)
**Quelle:** Session 2026-04-15 First Principles (A8)
**Begründung:** Marktdaten wechseln zwischen statistisch unterschiedlichen Regimes. Keine einzelne Strategie ist für alle Regimes optimal. Regime-Detektion (VPIN_Regime_Detector) ist strukturell notwendig für Strategie-Konsistenz, nicht Feature-Optimierung.
**Konfidenz:** Mittel (Orderflow als Leading-Indicator für Regimewechsel stärker kontrovers als reine Regime-Existenz)

### A9: Liquidität hat immer einen Träger mit eigenen Hedging-Zwängen
**Status:** Tentativ (neu 2026-04-15)
**Quelle:** Session 2026-04-15 First Principles (A5)
**Begründung:** Sofortige Liquidität existiert nicht ohne Gegenpartei. Market-Maker/Dealer sind Gegenparteien mit eigenen Absicherungszwängen — keine neutralen Vermittler. Ihr Verhalten (Hedging, Position-Aufbau) ist strukturell vorhersagbar und nutzbar. Orderflow-Analyse die Market-Maker-Verhalten ignoriert ist strukturell unvollständig.

---
## Neue Axiome — Session 2026-09-03-pilot (Status: Tentativ)

### A10: Mechanik ≠ Erntbarkeit (Axiom/Ableitung-Trennung)
**Quelle:** Session 2026-09-03-pilot First Principles
**Begründung:** Eine wahre mechanische Wahrheit (Dealer hedgen Gamma) impliziert keinen handelbaren Effekt. Die vier Nullergebnisse widerlegen A1 nicht — sie widerlegen die stille Ableitung „Mechanismus ⇒ handelbarer Effekt". Jede Idee muss künftig beide Ebenen getrennt belegen: Ist der Mechanismus wahr? UND: Ist daraus nach Kosten ein Ertrag extrahierbar?

### A11: Kosten-Rendite-Schere
**Begründung:** Profitabilität verlangt Mindesteffektstärke × Handelsfrequenz > Gesamtkosten (Gebühren, Slippage, Steuer). Bei Retail-Kostenstruktur ist die Mindesteffektstärke hoch — das schließt die meisten schwachen Signale strukturell aus, unabhängig von ihrer statistischen Existenz.

### A12: Retail und Institutionen spielen nicht dasselbe Spiel
**Begründung:** Institutionen optimieren Capacity × Sharpe gegen Karriere-Risiko; Retail optimiert absolute Rendite auf kleines Kapital mit Zeitbudget. Achsen auf denen Institutionen NICHT konkurrieren können oder wollen (zu klein, zu illiquide für deren Größe, zu langweilig für deren Reporting) sind strukturell konkurrenzfrei.

### A13: Nicht-Erntbarkeit von Mean-Reversion als Symmetrie-Theorem
**Begründung:** In einem mean-revertierenden Markt ohne Informationsvorsprung ist jeder Entry symmetrisch — die Reversion hilft Long- und Short-Seite gleichermaßen und ist damit nach Kosten für beide negativ. Gemessen: NDX VR 0,86–0,91, aber 47,8–48,5 % Trefferquote gegen die Ausbruchsrichtung.

### A14: Steuer als Teil der Marktstruktur
**Begründung:** § 20 EStG Verlustverrechnungsbeschränkung für Termingeschäfte verändert den Netto-Erwartungswert strukturell — sie ist kein nachträgliches Detail, sondern eine Marktregel wie Spread oder Margin. Strategien mit symmetrischen Gewinn/Verlust-Profilen werden asymmetrisch bestraft.

### A15: Marktauswahl ist eine Axiomen-Entscheidung, keine Präferenz
**Begründung:** ES vs. NQ unterscheiden sich in Tick-Ökonomie, Teilnehmermix, Volatilitätsregime. Die Wahl des Instruments determiniert den Möglichkeitsraum der Strategien stärker als jede Signal-Logik danach.

### A16: Filter ohne Wirtssignal ist ein Messgerät, keine Strategie
**Begründung:** Das Cluster besitzt vier validierte Filter/Messgrößen (GTZI, Topologie, Regime, Reversion-Maße), aber null Wirtssignale mit Brutto-Edge. Ein Filter multipliziert nur den Edge seines Wirts — 0 × x = 0. Suchrichtung muss sich von Filtern zu Brutto-Signalen umkehren.

### A17: Selbst-Validierungszeit ist die dritte harte Ressource
**Begründung:** Neben Kapital (A3) und Kognition (A7): Mit 1–2 h/Tag ist die Zahl validierbarer Hypothesen pro Jahr hart begrenzt (~12–24 Tests). Jede Test-Entscheidung ist eine Opportunitäts-Entscheidung — schlechte Priorisierung ist teurer als schlechte Modelle.

---
## Runde 2 — Zwangsmechanik-Axiome (2026-09-04, Status: Tentativ)

### A18: Zwangsmechanik-Katalog
Erzwungener Flow hat drei notwendige Eigenschaften: Auslöser (Regel/Schwellwert), Zeitfenster (Frist), identifizierbarer Träger. Katalog: CME-Margin-Calls, Index-Roll-Perioden, Prop-Firm-Tagesende-Flat, Options-Dealer-Verfall, Broker-Liquidations-Engines. Kalenderfähig — wer den Regelkalender kennt, kennt die Fenster.

### A19: Erzwungener Flow ist informationslos — deshalb bepreist ihn der Markt falsch
Erzwungener Flow ist preis-unelastisch (MUSS handeln), Gegenseite elastisch (KANN warten) → temporäre, reversible Preisverzerrung. Präzisiert A13: zwangsinduzierte Reversion (asymmetrisch, Ursache endet) ≠ statistische Reversion (symmetrisch, nicht erntbar). Handelbarer Moment ist das ENDE des Zwangs, nicht das Signal.

### A20: Retail-Zwänge sind der konkurrenzfreieste Flow
Prop-Firm-Regeln (Tagesende-Flat, Trailing-Drawdown, Tagesverlust-Limits) erzeugen synchronisierten Flow in MES/MNQ-Größe — zu klein/schmutzig für Institutionen, öffentlich dokumentiert. Die eine Achse, auf der Retail strukturml besser informiert ist — ohne klassischen Informationsvorsprung. Warnung: Wer selbst Eval-Regeln unterliegt, IST Teil des Flows.

### A21: Parallelisierungs-Deckel (Beobachten billig, Validieren teuer → Kalender-First)
Aus A17: Viele Zwänge beobachten ist billig, aber jeder Validierungstest frisst einen der ~12–24 Test-Slots/Jahr. Konsequenz: Zuerst den vollen Zwangs-Kalender bauen, dann Tests bündeln (Multi-Zwang-Fenster), nicht jeden Zwang einzeln testen — Margin-Hike allein hat zu wenige Ereignisse/Jahr.

---
## Runde 3 — Übersehene Zwangsmechaniken (2026-09-05, Tentativ)

### A22: Settlement-Zwang (T+1/Basket-Hedging)
Erster KASSA-seitiger Zwang, der in Futures exportiert wird: Index-Rebalancing/ETF-Creation-Redemption erzwingt Aktienkäufe/-verkäufe zum Close; die Hedging-Seite legt sich als Flow im Futures-Fenster ab. Kalenderfest (Quartals-Rebalancing, Index-Reviews).

### A23: 0DTE-Strukturwandel — Gamma-Zwang ist jetzt TÄGLICH
SPX/ES-Optionen haben seit 2022 tägliche Verfalle. Dealer-Gamma am Verfall ist damit kein monatliches (~12/Jahr), sondern ein tägliches (~250/Jahr) Ereignis. Hebt das Power-Problem von ID30 strukturell auf: ein Verfalls-Panel ist jetzt hochfrequent testbar.

### A24: Erntbarkeits-Kriterium
Ein Zwang ist für Retail nur erntbar bei: (a) Retail-kompatible Größe (MES/MNQ), (b) kalenderfestem Ende (A19), (c) KEINEM Latenz-Rennen (kein HFT-Wettbewerb um denselben Flow). Diskreditiert: Treasury-Basis-Unwinds, ETF-NAV-Arb, Clearing-Zyklen (alle Latenz/Kapital-vergeben).

### A25: Instrumenten-Streuung schlägt Zwangs-Streuung
Statt mehrere Zwänge auf EIN Instrument zu bündeln (ID30, Power-Problem): denselben Zwang auf MEHRERE Instrumente (ES+NQ+GC+ZB) anwenden. Erweitert A21, operationalisiert A15/ID24. Cross-Sectional-Reversion nutzt dieselbe Logik mit mehr Replikaten.
