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
