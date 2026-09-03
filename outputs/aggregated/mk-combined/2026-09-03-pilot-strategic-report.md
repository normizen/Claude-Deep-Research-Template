# Strategic Innovation Report — 2026-09-03-pilot (Hermes Pilotlauf)

## Executive Summary

Ausgangslage: Vier mechanik-basierte Signale (VPIN-Regime, GEX-Walls, GEX-Topologie, Gamma-Regime) wurden auf ~1.400 Handelstagen NDX 2021–2026 wissenschaftlich geprüft — alle negativ (Cliff's d ≤ 0,073 gegen Kriterium 0,10). Einziger belastbarer positiver Befund: NDX kehrt intraday robust zurück (VR 0,86–0,91), ist aber nach Kosten nicht ernte-fähig. Der Pilotlauf hat daraufhin die Suchrichtung gedreht: weg von Entry-/Filter-Verbesserung, hin zu Struktur-Achsen (Steuer, Instrumentenwahl, Zeitfenster, Abstain). Aus 8 generierten Ideen überlebten 3 die Advocatus-Prüfung; davon wurde 1 (ID23 Steuer-Viskosität) durch Recherche zur Rechtslage getötet — die 20k-Verrechnungsgrenze für Termingeschäfte ist seit Dezember 2024 gefallen. Verbleiben 2 testfähige Designs: ID24 (Instrumenten-Apoptose) und ID26 (Zeitfenster-System). Beide sind kostenlos auf QuantConnect replizierbar; beide liefern keine direktionalen Signale, sondern schließen strukturelle Kosten-/Ruin-Fallen, bevor weiteres Validierungsbudget verbrannt wird.

---

## 1. Neue Axiome und Dogmen

### Neue Axiome (A10–A17)

| ID | Kernaussage (1 Zeile) |
|---|---|
| A10 | Mechanik ≠ Erntbarkeit: ein wahrer Marktmechanismus impliziert keinen handelbaren Effekt — die Ableitung muss getrennt falsifiziert werden. |
| A11 | Kosten-Rendite-Schere: bei n Trades/Tag wächst die Mindesteffektstärke mit n; Retail mit 1–2 h/Tag ist axiomatisch auf 1–5 Ereignisse/Tag mit d ≥ 0,2 eingegrenzt. |
| A12 | Retail und Institutionen spielen dasselbe Markt-, aber nicht dasselbe Gewinn-Spiel — Retail gewinnt nur auf Achsen ohne institutionellen Wettbewerb (Geduld, Abstain, kleines Volumen). |
| A13 | Mean-Reversion ist ein Symmetrie-Theorem: der Maker hat die Reversion als Vergütung eingepreist; der Taker kauft sie zum Spread-Preis — nicht erntbar. |
| A14 | Steuer ist Teil der Marktstruktur, nicht Buchhaltung: die Verlustverrechnungsarchitektur verändert den Netto-Erwartungswert deterministisch und selektiert Strategien. |
| A15 | Marktauswahl ist Axiomen-Entscheidung: ES/NQ/MES/MNQ unterscheiden sich in Tick-Ökonomie, Teilnehmermix und Zeitfenster-Fit — nicht austauschbar. |
| A16 | Filter ohne Wirtssignal ist Messgerät, keine Strategie: E[R|F] > 0 erfordert E[R] > 0; Filter multiplizieren, sie addieren nicht. |
| A17 | Selbst-Validierungszeit ist eine harte Ressource: Tage bis Signifikanz ≈ (z/d)² / r; bei d = 0,1 und r = 1/Tag sind das ~4 Jahre — epistemisch unerreichbar. |

### Neue Dogmen (D10–D16)

| ID | Dogma | Warum eingepreist / gebrochen |
|---|---|---|
| D10 | „Der Tag ist die Einheit des Erfolgs — täglich handeln" | Widerspricht A11/A12/A13; Aktivitäts-Pflicht ist im Broker-/Prop-Firm-Modell eingepreist. |
| D11 | „Mehr Filter = besseres System" | Widerspricht A16; viermal empirisch widerlegt (VPIN, GEX-Regime, Topologie, Gamma). |
| D12 | „Edge liegt im Entry" | Widerspricht A5/A13; Entry ist die dichtest besetzte Achse, Kosten/Steuer/Instrument sind dünn besetzt. |
| D13 | „Retail konkurriert im selben Spiel mit schlechterer Ausrüstung" | Widerspricht A12; strukturelle, nicht graduelle Lücke (Co-Location, Rebates, Netting). |
| D14 | „Nullergebnis = weitersuchen ohne Struktur" | Widerspricht A10/A17; Negativbefunde sind Cluster-Vermögen, schließen Familien strukturell. |
| D15 | „Risiko minimieren ist das Ziel" | Bei 5–10k € und 1–2 h/Tag ist Erwartungswert-Dichte pro Risiko + Validierungstag die Zielgröße, nicht Varianz-Minimierung. |
| D16 | „Instrumentenwahl ist Geschmack" | Widerspricht A15/A14; Tick-Ökonomie, Margin, Steuerklasse und Zeitfenster machen die Wahl abgeleitet, nicht preferenziell. |

---

## 2. Seed-Domänen und Kombinationslogik

| | |
|---|---|
| **Domäne 1** | **Apoptose** (Cluster 2 — Biologische Systeme): programmierter Zelltod als Systemfunktion; das Opfer des Teils rettet das Ganze. |
| **Domäne 2** | **Glasübergang** (Cluster 4 — Strukturen & Materialien): Flüssigkeit wird unendlich viskos ohne Phasenübergang; Verhalten wird durch das Verhältnis τ_relax/τ_beobachtung bestimmt. |

**Kombinationslogik:** Glasübergang diagnostiziert den Zustand (Verglasung durch Zeitbudget-/Kosten-Reibung), Apoptose liefert die Therapie (programmierte Eliminierung als Systemfunktion mit eigenen Auslösern), die Kerndomäne Futures-Daytrading liefert das Testfeld. Beide Seeds zwingen zu Brutto-Entscheidungen über *was nicht getan wird* — entlang der vier Achsen Selektivität, Kosten, Instrument, Zeitbudget — statt zu Entry-/Filter-Verbesserung.

---

## 3. Ideenfeld und Advocatus-Urteile

| ID | Idee | Urteil | Hauptgrund |
|---|---|---|---|
| ID20 | Verglasungs-Diagnostik / Relaxationszeit-Audit | **ELIMINIERT** | A16-Verstoß: Gate ohne Wirtssignal; Test reproduziert nur A11 (eingepreist). |
| ID21 | Apoptose-Kalender / vorregistrierte Setup-Sterbefälle | **ELIMINIERT** | Alter Wein: vorregistrierte Abbruchkriterien sind Standard-Evaluation, kein Edge. |
| ID22 | Abstain-Quote als Leistungsmerkmal | **ELIMINIERT** | A16-Zirkularität: Abstain-Precision misst Rauschen, solange kein Brutto-Wirt existiert. |
| ID23 | Steuer-Viskosität als Strategie-Selektor | **ÜBERLEBT** (später getötet) | Axiom-konform (A14), konkurrenzfrei (A12), sofort testbar — aber Rechtslage gekippt. |
| ID24 | Instrumenten-Apoptose (ES/NQ/MES/MNQ-Eliminierungsturnier) | **ÜBERLEBT** | A15-Pflichtaufgabe, beantwortet den NQ-Konfounder des Clusters, handlungsrelevant egal wie es ausfällt. |
| ID25 | Unterkühltes Setup-Reservoir | **ELIMINIERT** | A16 + A10: Filter-Apparat in Thermodynamik-Kostüm; einziger Mechanismus aus vierfach negativer Familie. |
| ID26 | Zeitfenster-Reduktion / 30-Minuten-Organismus | **ÜBERLEBT** | Billig falsifizierbar, A17-kompatibel, bricht D10 mit registrierbarer Hypothese. |
| ID27 | Gegenfaktual-Buchhaltung / tote Tage als Datenpunkte | **ELIMINIERT** | Umbenanntes Shadow-Trading: Gegenfaktual-Buchung ist Default-Output jedes Backtests. |

---

## 4. Überlebende im Detail

### ID24 — Instrumenten-Apoptose

**Kern:** Die Marktauswahl (ES/MES/NQ/MNQ) wird nicht getroffen, sondern als wiederkehrender Eliminierungsprozess betrieben. Alle vier Kandidaten starten als lebende Hypothesen mit vorab registrierten Todeskriterien; Default ist Eliminierung, nicht Behalten. Das Turnier reduziert sich ehrlich auf 3 unabhängige Entscheidungen: (a) S&P- vs. Nasdaq-Familie, (b) Micro vs. Mini, (c) Gesamtklassen-Eliminierung bei Volatilitätskollaps.

**Todeskriterien-Übersicht (6 Kriterien, vorab registriert):**

| # | Kriterium | Schwellwert | Messintervall |
|---|---|---|---|
| K1 | Kosten-Range-Schere (hart, sofort) | All-in-RT-Kosten > 5 % der 20-Tage-Ø-Dollar-Range | monatlich |
| K2 | Setup-Tragfähigkeit | Setup-Stop × Tickwert > 1 % Kapital ODER 2-%-Risiko nicht mit 1,5:1 R:R erreichbar | monatlich |
| K3 | Margin-Suffokation | (Overnight-Margin × 2) > 40 % Kapital ODER (Day-Margin × Kontrakte) > 25 % Kapital | monatlich |
| K4 | Redundanz | Rolling-60d-Korrelation > 0,90 UND Vol-Prämie < 1,3× | monatlich |
| K5 | Liquiditäts-/Slippage-Bruch (hart, sofort) | Ø-Slippage > 1 Tick/RT über 20 Trades ODER Spread > 1 Tick im Fenster an > 30 % der Tage | laufend |
| K6 | Zeitbudget-Kompatibilität | > 60 % der 20-Tage-Range entsteht außerhalb des verfügbaren Handelsfensters | monatlich |

**Eliminierungsregel:** ≥ 2 Kriterien in 2 aufeinanderfolgenden Monaten → Eliminierung. K1 oder K5 allein → sofort. Default bei Datenlücke = Eliminierung. Pro Quartal genau 1 schriftlicher Begnadigungsantrag erlaubt.

**Aufwand:** ~1 h/Monat Median, ~2 h in Turniersmonaten (quartalsweise). Kein QC-Backtest nötig; Daten: QC-Daily-Bars (kostenlos), CME-Margin-Bulletins, Broker-Statement.

---

### ID26 — Zeitfenster-System

**Kern:** Komplettes Handelssystem um ein einziges vorab fixiertes 30-Minuten-Fenster (15:30–16:00 ET). Fenster-Wahl ist die vorregistrierte Hypothese, nicht eine Lifestyle-Entscheidung. Der Rest des Tages ist per Konstruktion ausgeschlossen (Abstain als Default).

**Hypothese (vorregistriert):**
1. Die Kostenquote (RT-Kosten / mittlere Fenster-Range) im Ziel-Fenster 15:30–16:00 ET ist **mindestens Faktor 3 niedriger** als der Median über alle RTH-30-Min-Fenster.
2. Explorativ: Erst-30-Min → letzt-30-Min Momentum (Gao et al. 2018) ist im Segment 2022+ flach/negativ (Decay-Hypothese nach gex.live-Replikation).

**Abnahmekriterien (beide müssen erfüllt sein):**
- Cliff's d ≥ 0,10 (Kostenquote Ziel-Fenster vs. alle anderen Fenster)
- Ziel-Fenster oberhalb des **95%-Perzentils von 500 Placebo-Fenstern** (zufällige 30-Min-Fenster gleicher Stichprobenzahl)

**Zeitzone-Constraint (deutscher Trader, abends, 1–2 h/Tag):** US-RTH 9:30–16:00 ET = 15:30–22:00 MESZ (Sommer). Erreichbare Fenster: 21:00–21:30 MESZ (Power Hour-Beginn) und 21:30–22:00 MESZ (letzte 30 Min) — **nur in Sommerzeit**. Im Winter (MEZ) liegt das letzte Fenster bei 22:30–23:00 → Winter-Problem. DST-Asymmetrie (US/EU wechseln an verschiedenen Wochenenden) erzeugt 2× jährlich 2–3 Wochen mit verschobenen Fenstern — im Test strikt in ET rechnen, nie in Lokalzeit.

---

### ID23 — Steuer-Viskosität: Tod durch Rechtslage

> **Wichtig für den User als Trader:** Die 20.000-€-Verrechnungsgrenze für Termingeschäftsverluste (§ 20 Abs. 6 Satz 5 EStG a.F.) existiert seit Dezember 2024 nicht mehr. BVerfG 31.07.2024 (2 BvL 7/22) hat sie für verfassungswidrig erklärt; das JStG 2024 (in Kraft 06.12.2024) hat die Sätze 5 und 6 ersatzlos gestrichen — **rückwirkend für alle offenen Fälle**, wirksam ab Veranlagungszeitraum 2024. Für Futures-/CFD-/Options-Trader gilt seitdem: volle Verrechnung mit allen Kapitalerträgen im allgemeinen Topf, keine 20k-Grenze, kein separater Termingeschäftstopf.

**Was noch gilt:** Der Aktien-Verlustverrechnungstopf (§ 20 Abs. 6 Satz 4 EStG) ist weiterhin aktiv. BVerfG-Verfahren 2 BvL 3/21 ist anhängig; Entscheidung wird im Verlauf 2026 oder Anfang 2027 erwartet. Bescheide mit Aktienverlust-Topf ergehen vorläufig.

**Implikation:** ID23 in der ursprünglichen Form (Termingeschäfts-20k als struktureller Friktionseffekt) ist **tot**. In stark abgewandelter Form („Aktien-Topf-Arbitrage vor BVerfG-Entscheidung 2 BvL 3/21") noch lebendig, aber mit explizitem Risikohinweis auf das erwartete Urteil 2026/2027.

---

## 5. Nächste Schritte / Test-Anleitung

### Sofort (diese Woche)

- [ ] **ID24 Range-Monitor starten:** `outputs/individual/2026-09-03-pilot/code/id24_range_monitor.py` auf QC-Daily-Bars (ES/MES/NQ/MNQ) laufen lassen → erste K1-Tabelle. Datenquelle: QC Cloud (kostenlos). Ausgabe: CSV mit 20-Tage-Dollar-Ranges + Kosten/Range-Ratios.
- [ ] **ID26 Fenster-Test vorbereiten:** `outputs/individual/2026-09-03-pilot/code/qc_id26_fenster_test.py` in ein QC-Notebook kopieren. Vorab im Header: Hypothesen und Abnahmekriterien stehen lassen (vorregistriert). Daten: ES-Minutenbars 2019–2026, strikt ET.

### Monatlich (letzter Handelstag, ~1 h)

- [ ] ID24 Bewertungs-Matrix ausfüllen (Template in `experiment-designs.md` Abschnitt „ID24 Bewertungs-Matrix")
- [ ] CME-Margin-Bulletin prüfen (K3)
- [ ] Rolling-60d-Korrelation + Vol-Prämie aus Daily-Daten (K4)
- [ ] Trade-Log: Slippage-Schnitt letzte 20 Trades, Spread-Quote im Fenster (K5)
- [ ] Session-Anteil der Range (K6)
- [ ] Status je Instrument festlegen, Protokoll ablegen

### Quartalsweise

- [ ] Formales ID24-Turnier: Status-Review, ggf. Begnadigungsantrag (max. 1/Quartal)
- [ ] ID26: Falls Kostenquote-Hypothese bestätigt → Momentum-Exploration mit Decay-Split (2019–2021 vs. 2022+)

### Dateien liegen hier

| Datei | Pfad |
|---|---|
| ID24 Range-Monitor (Python) | `outputs/individual/2026-09-03-pilot/code/id24_range_monitor.py` |
| ID26 Fenster-Test (QC-Notebook) | `outputs/individual/2026-09-03-pilot/code/qc_id26_fenster_test.py` |
| Bewertungs-Matrix (Template) | `outputs/individual/2026-09-03-pilot/experiment-designs.md` (Abschnitt unten) |
| Vollständige Todeskriterien | `outputs/individual/2026-09-03-pilot/feasibility-id24.md` |
| Rechtscheck § 20 EStG | `outputs/individual/2026-09-03-pilot/rechtscheck-estg.md` |

---

## Anhang: Datei-Index

| Datei | Inhalt |
|---|---|
| `scratchpad/2026-09-03-pilot-axioms.md` | 8 neue Axiome A10–A17 + Vergleich mit Axiom-Library A1–A9 |
| `scratchpad/2026-09-03-pilot-dogma-break.md` | 7 neue Dogmen D10–D16 mit axiomatischer Prüfung |
| `scratchpad/2026-09-03-pilot-domain-selection.md` | Anti-Anchor-Protokoll, 30-Domänen-Tracking, Auswahl Apoptose + Glasübergang |
| `scratchpad/2026-09-03-pilot-discovery-draft.md` | 8 Ideen ID20–ID27 mit axiomatischer Basis und Seed-Einfluss |
| `scratchpad/2026-09-03-pilot-feasibility-pre.md` | Advocatus Diaboli: Urteile zu allen 8 Ideen, 3 Überlebende, 5 Eliminierte |
| `outputs/individual/2026-09-03-pilot/feasibility-id24.md` | ID24: Todeskriterien, Regime-abhängige Dimensionen, Betriebsaufwand, Quellen |
| `outputs/individual/2026-09-03-pilot/feasibility-id26.md` | ID26: Intraday-Asymmetrien, Nach-Kosten-Rechnung, Zeitzone-Constraint, Test-Design, Quellen |
| `outputs/individual/2026-09-03-pilot/rechtscheck-estg.md` | Rechtslage § 20 Abs. 6 EStG: BVerfG, JStG 2024, Implikation für ID23 |
| `outputs/individual/2026-09-03-pilot/experiment-designs.md` | Vorregistrierte Test-Designs für ID24 und ID26, Bewertungs-Matrix, Abnahmekriterien |
| `outputs/individual/2026-09-03-pilot/code/id24_range_monitor.py` | Python-Skript: 20-Tage-Dollar-Ranges + Kosten/Range-Ratios für ES/MES/NQ/MNQ |
| `outputs/individual/2026-09-03-pilot/code/qc_id26_fenster_test.py` | QC-Notebook: Fenster-Kostenquote, Placebo-Test, Decay-Split |
