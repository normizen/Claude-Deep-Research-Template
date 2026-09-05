# Dogma-Graveyard — futures-trading-edge

## Format
Jedes Dogma: Titel | Status | Warum es ein Dogma ist (eingepreist, nicht fundamental) | Was stattdessen wahr sein könnte

---

## Dogmen

### D1: "90% der Retail-Trader scheitern — das ist ein Naturgesetz"
**Status:** Dekonstruiert (Tentativ)
**Warum Dogma:** Die 90%-Zahl beschreibt eine Population von Tradern ohne validierte Edge, ohne Sizing-Disziplin, emotional. Populationseffekt, nicht fundamentale Unmöglichkeit.
**Was stattdessen:** Wenn die Failure-Ursachen identifizierbar und korrigierbar sind, ist struktureller Edge für Retail möglich. A4 (Zero-Sum + Kostenasymmetrie) erklärt warum die meisten scheitern: kein quantifizierter Edge der Gebühren überkompensiert.

### D2: "Wissen und Erfahrung führen im Trading zum Erfolg"
**Status:** Dekonstruiert (Bestätigt)
**Warum Dogma:** Generisches Chart-Wissen und allgemeine Erfahrung sind arbitriert. Nur strukturelles Wissen über mechanische Zwangslogiken schafft Edge.
**Was stattdessen:** Nur strukturelles Wissen zählt: mechanische Zwangslogiken (GEX), Informations-Timing-Asymmetrie, systematische Validierung.
**Erweiterung (2026-04-15 D5):** "Disziplin" ist ein Spezialfall dieses Dogmas — eine moralische Forderung an ein biologisch begrenztes System. Lösung: Systematisierung, nicht Willenskraft.

### D3: "Edge Decay ist bei allen Strategien unvermeidlich"
**Status:** Dekonstruiert (Tentativ)
**Warum Dogma:** Gilt für statistische Pattern-Strategien, nicht für Mechanik-basierte.
**Was stattdessen:** Mechanik-basierte Edges (GEX-Dealer-Hedging) sind strukturell publikations- und arbitrage-resistent weil sie kein Pattern sind — sie sind Naturgesetze der Marktstruktur. Solange Options-Märkte existieren, hedgen Dealer ihr Gamma.
**Ergänzung durch D6 (2026-04-15):** Akademische Forschung zu mechanischen Edges ist valide Informationsquelle — keine Gefahr durch Veröffentlichung.

### D4: "Stop-Loss ist Risikomanagement" (NEU 2026-04-15)
**Status:** Dekonstruiert (Tentativ)
**Warum Dogma:** Universalkonsens in Trading-Ausbildung, Broker-Kommunikation, Büchern. Aus Trend-Following-Ära (1970-1990er) wo Hard-Stops strukturell sinnvoll waren.
**Was stattdessen:** Stop-Loss ist nur Risikomanagement wenn er zur Regime-Logik der Strategie passt. In Mean-Reversion-Regimen ist ein zu enger Stop-Loss strukturell kapitalzerstörend. Echtes Risikomanagement = Positions-Sizing + Regime-Awareness, nicht mechanisches Stop-Placement.

### D5: "Trend is your friend — immer mit dem Trend handeln" (NEU 2026-04-15)
**Status:** Dekonstruiert (Tentativ)
**Warum Dogma:** Jesse-Livermore-Ära, Turtle-Traders (1980er), standardmäßig in Chartsoftware (MA, MACD, ADX). In hochliquiden Intraday-Futures mit HFT-Beteiligung sind Intraday-Trends in Millisekunden arbitriert.
**Was stattdessen:** In hochliquiden Intraday-Futures dominieren Mean-Reversion-Strukturen zu mechanischen Zonen (GEX-Walls, VWAP, POC). Trend ist ein Makro-Phänomen das intraday durch Dealer-Mechanik regelmäßig gebrochen wird.

### D6: "Mehr Daten = bessere Strategie" (NEU 2026-04-15)
**Status:** Dekonstruiert (Tentativ)
**Warum Dogma:** Data-Science-Tradition, ML-Literatur, Quant-Finance-Standardlehre. Übertragung von statistischen Grundsätzen ohne Berücksichtigung von Regime-Nicht-Stationarität.
**Was stattdessen:** Relevante Datenmenge ist nicht maximal, sondern regime-kohärent. 6 Monate kohärente Regime-Daten schlagen 5 Jahre Regime-Mix für jedes Modell. VPIN_Regime_Detector als Filter macht vorhandene Daten wertvoller ohne neue zu benötigen.

### D7: "Backtesting validiert eine Strategie" (NEU 2026-04-15)
**Status:** Dekonstruiert (Tentativ)
**Warum Dogma:** Standard-Workflow in jeder Trading-Software und Quant-Finance-Ausbildung. Hatte höheren Vorhersagewert vor HFT-Dominanz und Regime-Beschleunigung.
**Was stattdessen:** Backtesting ist notwendig aber nicht hinreichend. Entscheidende Frage: Was ist der strukturelle Mechanismus der den Edge produziert — und ist er noch aktiv? Mechanismus-First-Entwicklung (zuerst Mechanismus definieren, dann Backtest als Verifikation) ist robuster als datengetriebenes Pattern-Fitting.

### D8: "Edge muss geheim gehalten werden — publizierte Strategien funktionieren nicht" (NEU 2026-04-15)
**Status:** Dekonstruiert (Tentativ)
**Warum Dogma:** Hedge-Fund-Kultur der 1990er/2000er. Hatte Gültigkeit für statistische Arbitrage-Strategien (Pairs Trading). Nicht falsifizierbar durch Survivorship Bias.
**Was stattdessen:** Mechanik-basierte Edges sind publikationsresistent. Akademische Marktmikrostruktur-Forschung (arXiv, SSRN) ist für mechanische Edges valide Quelle ohne Arbitrage-Risiko.

### D9: "Retail-Trader sollten keine komplexen Systeme bauen — keep it simple" (NEU 2026-04-15)
**Status:** Dekonstruiert (Tentativ)
**Warum Dogma:** Reaktion auf Curve-Fitting und Overfitting in akademischer Forschung (1990er). Korrekt für zu viele freie Parameter in statistischen Modellen — falsch übertragen auf Systemkomplexität.
**Was stattdessen:** Strategie-Logik (Entry-Mechanismus) soll einfach bleiben — das System (Detektion, Filter, Execution-Support) muss komplex genug sein um kognitive Kapazitätsgrenzen zu kompensieren. Ein Retail-Trader ohne Team braucht ein komplexeres Unterstützungssystem als ein institutioneller Trader mit Team.

---
## Neue Dogmen — Session 2026-09-03-pilot

### D10: "Intraday muss aktiv gehandelt werden"
**Warum Dogma:** Aus Prop-Trading- und Chartsoftware-Kultur. Eingepreist: Jede Stunde vor dem Chart fühlt sich wie Arbeit an — Nichtstun wird nicht als Position wahrgenommen.
**Gegenthese:** Abstain ist eine Position mit positivem Erwartungswert, wenn die Kosten-Rendite-Schere (A11) die meisten Tage ausschließt. Selektivität ist der konkurrenzfreie Retail-Vorteil (A12).

### D11: "Mehr Filter = besseres System"
**Warum Dogma:** Aus der ML-/Feature-Engineering-Kultur. A16 zeigt: vier Filter, null Wirtssignale.
**Gegenthese:** Filter sind Multiplikatoren auf einen Brutto-Edge. Ohne Wirt sind sie Messtechnik.

### D12: "Edge liegt in der Signal-Generierung"
**Warum Dogma:** Gesamte Trading-Literatur fokussiert Entries.
**Gegenthese:** Für Retail liegt Edge in Kostenarchitektur, Steuerstruktur (A14), Instrumentenwahl (A15) und Verzicht — Dimensionen, die der Markt nicht als „Edge" vermarktet.

### D13: "Retail konkurriert im selben Spiel wie Institutionen"
**Warum Dogma:** Broker-Marketing („trade like the pros").
**Gegenthese:** A12 — verschiedene Zielfunktionen, verschiedene Spiele. Auf den Achsen, wo Institutionen nicht spielen können, ist Retail allein.

### D14: "Nullergebnis entwertet den Ansatz"
**Warum Dogma:** Psychologisch, nicht intellektuell verbreitet — viermal negativ fühlt sich wie vier Jahre verschwendet an.
**Gegenthese:** Vier sauber widerlegte Hypothesen mit aufgebauter Messinfrastruktur sind positives Wissen (A17: schützt künftige Test-Slots). Placebo-Methodik und Event-Studie sind der eigentliche Ertrag.

### D15: "Risiko ist der Feind"
**Warum Dogma:** Risikomanagement-Literatur; Varianz-Minimierung als Default.
**Gegenthese:** Bei 5–10k und Zeitbudget ist das eigentliche Risiko nicht Varianz, sondern das Nie-Ankommen (Opportunitätskosten der Unterkapitalisierung des Lernprozesses).

### D16: "Instrumentenwahl ist Geschmack"
**Warum Dogma:** „Handle was du kennst"-Folklore.
**Gegenthese:** A15 — Instrumentenwahl determiniert Tick-Ökonomie und Kosten-Rendite-Schere stärker als jede Entry-Logik.

---
## Runde 2 Dogmen (2026-09-04)

### D17: "Edge = informierter sein als der Markt"
**Gegenthese:** Edge kann aus der Informationslosigkeit des Gegenflows kommen (A19). Wer weiß, WER WANN handeln muss, braucht keine Information — nur einen Kalender.

### D18: "Man braucht einen Informationsvorsprung"
**Gegenthese:** Zwangsmechaniken sind öffentlich dokumentiert (Regelwerke, Vertragsbedingungen) und nicht arbitrage-zerstörbar, weil der Zwang nicht verschwindet wenn man ihn kennt — der Margin-Call kommt trotzdem.

### D19: "Mehr Beobachtung = mehr Edge"
**Gegenthese:** A21 — Validierungs-Slots sind der Engpass, nicht Beobachtung. Kalender-First, gebündelte Tests.

### D20: "Forced Flow ist HFT-only"
**Gegenthese:** HFT erntet institutionelle Zwänge (Dealer-Gamma) mit Latenzvorteil. Retail-interne Zwänge (Prop-Firm-Flat) sind für HFT zu klein und liegen genau in MES/MNQ-Größe — die Retail-Kapitalzone (A20).
