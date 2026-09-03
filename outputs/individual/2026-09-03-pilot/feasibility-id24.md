# Feasibility — ID24 Instrumenten-Apoptose

## Antwort auf den Advocatus-Einwand

Der Einwand trifft die zentrale Schwachstelle, aber er ist **beantwortbar** — wenn auch mit einer Einschränkung: Die Instrumenten-Apoptose ist *nicht* eine einmalige Due Diligence, aber auch nicht der radikal wiederkehrende Prozess, als den die Idee sich vielleicht verkauft. Die ehrliche Antwort lautet: **Ein Teil der Unterscheidungsdimensionen ist strukturell stabil (Kontraktspezifikationen, Gebühren relativ zum Tickwert), ein anderer Teil ist nachweislich regime-abhängig (Volatilitäts-/Range-Profile, Overnight-Margin, ES/NQ-Korrelation, relative Handelbarkeit der Micros vs. Minis bei gegebener Kontogröße).** Damit ergeben sich zwei Klassen von Todeskriterien:

1. **Einmalige Disqualifikation** (stabile Dimensionen): Ein Instrument, dessen Kosten-Rendite-Schere bei realistischen Stops/Zielen strukturell negativ ist (z. B. 1-Tick-Scalping auf MES), wird *einmal* gestrichen — hier ist der Einwand berechtigt: das ist Due Diligence, kein Turnier.
2. **Wiederkehrende Eliminierung** (regime-abhängige Dimensionen): Volatilitätskompression (VIX-Percentile → Tagesrange in $), Margin-Anhebungen der CME (nachweislich asymmetrisch prozyklisch: schnell rauf, langsam runter), und das Zusammenbrechen der instrumentenspezifischen Volatilitätsprämie (NQ liefert normalerweise 1,8–2,2× die ES-Bewegung — bricht diese Prämie ein, ist NQ/MNQ für ein gegebenes Setup redundant, teurer und riskanter als ES/MES). Diese Dimensionen verändern sich auf Monats- bis Quartalszeitskalen und *erzwingen* eine nicht-triviale Neubewertung.

Damit das Turnier nicht zur Gewohnheits-Farce wird, müssen die Todeskriterien **vorab mit numerischen Schwellwerten und Messintervallen registriert** werden, sodass die Regel die Entscheidung trifft — nicht der Händler. Die Nicht-Trivialität entsteht dadurch, dass der Default-Zustand "Eliminierung bei Nichterfüllung" ist, nicht "Weiter so". Genau das unterscheidet Apoptose von Due Diligence: Bei Due Diligence ist der Default "behalten", hier ist der Default "sterben".

Ehrliche Einschränkung: Bei nur 4 hochkorrelierten Index-Instrumenten (ES/NQ/MES/MNQ) sind MES↔ES und MNQ↔NQ per Konstruktion funktional identisch (gleicher Preis, Faktor 10). Das Turnier reduziert sich damit realistisch auf 3 unabhängige Entscheidungen: (a) S&P-Familie vs. Nasdaq-Familie, (b) Micro vs. Mini innerhalb der gehandelten Familie(n), (c) Eliminierung der Gesamtklasse bei Volatilitätskollaps. Das ist ein kleineres Turnier als die Idee suggeriert — aber ein echtes, wiederkehrendes.

## Regime-abhängige vs. stabile Dimensionen

| Dimension | Wert (typisch 2025/26) | Stabil / Regime-abhängig | Relevanz für Apoptose |
|---|---|---|---|
| Tickwert / Multiplikator | ES $12,50 · MES $1,25 · NQ $5,00 · MNQ $0,50 | **Stabil** (Kontraktspezifikation) | Einmalige Due Diligence; kein Todeskriterium nötig |
| Explizite Kosten pro RT in Ticks | ES ~0,36 Ticks · NQ ~0,90 Ticks · MES ~1,68 Ticks · MNQ ~1,3–2,6 Ticks (brokerabhängig) | **Semi-stabil** (Gebühren ändern sich selten, Brokerwahl verschiebt stark) | Einmal-Kriterium mit jährlichem Re-Check; bei Micros strukturell kritisch |
| Tagesrange in $/Kontrakt | MES $50–100 · MNQ $400–800 · ES $2.000–4.000 · NQ $4.000–8.000 | **Regime-abhängig** (VIX-regimegetrieben) | Kern des wiederkehrenden Prozesses |
| Kosten als % der Tagesrange | MES-RT ~2–4 % der Range · MNQ ~0,3–0,8 %; verschlechtert sich in VIX-Kompression | **Regime-abhängig** | Direktes Todeskriterium ("Range trägt die Kosten nicht mehr") |
| Overnight-Margin (CME SPAN) | ES ~$12–15k · NQ ~$17–22k · Micros 1/10 davon | **Regime-abhängig**, asymmetrisch: schnelle Erhöhung bei Vol-Spike, träge Senkung | Todeskriterium für 5–10k-Konten: Overnight-Haltbarkeit |
| Day-Trading-Margin | MES $50–100 · MNQ $100–300 (brokerabhängig) | Semi-stabil (Brokerpolitik, folgt VIX mit Verzögerung) | Schwellwert: Margin/Kapital-Ratio |
| ES/NQ-Korrelation & Vol-Prämie | NQ ≈ 1,8–2,2× ES-Volatilität; Korrelation 0,85+, bricht in Regimewechseln | **Regime-abhängig** | Redundanz-Todeskriterium: zwei Instrumente, ein Trade |
| Liquidität/Book-Tiefe Micros vs. Minis | MES 1,5–2,5 Mio. Kontrakte/Tag, dünnere Book-Tiefe, Spreadweitung in Fast Markets | **Regime-abhängig** (verschlechtert sich in Stressphasen) | Todeskriterium: Spread/Slippage-Budget |

**Konsequenz:** Mindestens 5 der 8 Dimensionen sind messbar regime-abhängig. Damit ist der wiederkehrende Prozess faktisch begründet — nicht nur rhetorisch.

## Vorgeschlagene Todeskriterien (vorab registrierbar, mit Schwellwerten)

Registriert am Turnier-Start, Messung monatlich (letzter Handelstag), Datenquellen: Broker-Statement, CME-Margin-Bulletins, VIX-Close, eigene Trade-Log-Daten. Verletzung von ≥2 Kriterien in 2 aufeinanderfolgenden Monaten = Eliminierung; Verletzung von K1 oder K5 allein = sofortige Eliminierung.

**K1 — Kosten-Range-Schere (hart, sofort):**
`All-in-RT-Kosten > 5 % der 20-Tage-Durchschnittsrange (in $)` → Instrument trägt die Kosten ökonomisch nicht mehr. Beispiel MES: RT $2,10 vs. Range $50 → 4,2 % (grenzwertig lebendig); fällt die Range auf $30 (VIX < 13-Regime), ist MES bei 7 % **tot**.

**K2 — Setup-Tragfähigkeit (Kapital-Constraint):**
`Vom Setup geforderte Stop-Weite × Tickwert × 2 % Risiko-Regel > 1 % des Kapitals` über 20 Handelstage im Median. Konkret bei 7.500 $ Kapital: Setup-Stop > 15 NQ-Punkte macht selbst **1 MNQ** untragbar, wenn 2-%-Risiko ($150) nicht mindestens 1,5:1 R:R an der aktuellen Range erreichbar ist.

**K3 — Margin-Suffokation (Konto-Constraint):**
`(Overnight-Margin × 2) > 40 % des Kapitals` → Instrument für Swing-/Overnight-Komponente tot; `(Day-Trade-Margin × Mindestkontrakte für das Setup) > 25 % des Kapitals` → auch intraday tot. Bei 5–10k tötet dieses Kriterium ES/NQ-Overnight automatisch und MNQ-Daytrading bei CME-Margin-Erhöhungszyklen (nachweislich: CME erhöht schnell, senkt langsam — ein Spike-Regime kann ein Instrument für Monate disqualifizieren).

**K4 — Redundanz/Diversifikations-Verlust:**
`Rolling-60-Tage-Korrelation der Tagesreturns zum Primärinstrument > 0,90 UND Volatilitätsprämie < 1,3×` → das schwächere Instrument liefert keinen eigenständigen Edge und wird eliminiert (üblicherweise: NQ/MNQ fällt, ES/MES bleibt). Invertiert in Tech-dominierten Trendregimes — dann muss die Entscheidung aktiv neu getroffen werden, was die Wiederkehr erzwingt.

**K5 — Liquiditäts-/Slippage-Bruch (hart, sofort):**
`Gemessene Ø-Slippage pro RT > 1 Tick über 20 Trades` ODER `Spread > 1 Tick während des eigenen Handelsfensters (1–2 h/Tag) an > 30 % der Tage`. Tötet Micros in Stressregimen (Overnight-Session, Fast Markets), in denen das Micro-Book klafft, während das Mini-Book trägt.

**K6 — Zeitbudget-Kompatibilität (1–2 h/Tag):**
`Anteil der 20-Tage-Range, der außerhalb des verfügbaren Handelsfensters stattfindet, > 60 %` → das Instrument lebt in einer Session, die der Trader nicht abdeckt (typisch: Bewegung im Asien-/Europa-Überhang) → tot für diesen Trader, unabhängig vom Markt selbst. Direkt aus den Real-Constraints abgeleitet, nicht aus Markteigenschaften.

**Registrierungsformalismus:** Jedes Kriterium wird mit Schwellwert, Datenquelle, Messdatum und *Default = Eliminierung* vorab schriftlich fixiert. Der Händler darf pro Quartal genau einen "Begnadigungsantrag" stellen, der eine schriftliche Begründung mit neuem Datenpunkt erfordert — das macht die Entscheidung nicht-trivial und verhindert Gewohnheits-Weiterhandel.

## Betriebsaufwand

- **Täglich (0 min Zusatz):** K5/K6 werden als Nebenprodukt des Trade-Logs erfasst (Slippage je Trade, Session-Anteil der Range) — automatisierbar aus Broker-Export.
- **Monatlich (~30–45 min):** K1–K4 auswerten: 20-Tage-Range, VIX-Regime, CME-Margin-Bulletin prüfen, Korrelation/Vol-Prämie aus Daily-Daten (eine Tabellenkalkulation oder ein 30-Zeilen-Skript). Das ist kompatibel mit 1–2 h/Tag, frisst aber einen sichtbaren Anteil des Wochenbudgets.
- **Quartallich (~1 h):** Formales Turnier mit Protokoll: Status je Instrument (lebendig/bedingt/tot), ggf. Re-Registration der Schwellwerte (nur bei strukturellem Marktwechsel, nicht zur Begnadigung).
- **Gesamt:** ~1 h/Monat Median, ~2 h in Turniermonaten. **Machbar** innerhalb der Constraints — der eigentliche Engpass ist Datendisziplin (konsequentes Slippage-Logging), nicht Analyseaufwand.
- **Re-Evaluations-Frequenz:** monatlich ist das sinnvolle Minimum; wöchentlich wäre Rauschen (Margin- und VIX-Regime ändern sich auf Wochen-Monats-Skalen), quartalsweise wäre zu träge für CME-Margin-Spikes (K3).

## Quellen

- NexusFi Academy — Futures Trading Costs (RT-Kosten in Ticks: ES 0,36 / MES 1,68 / NQ 0,90; Slippage-Dominanz; CME-Overnight-Margins ES ~$12–15k, NQ ~$17–22k): https://nexusfi.com/a/risk-management/futures-trading-costs
- NexusFi Academy — Micro E-mini Futures Guide (Tickwerte, Fungibilität Micro↔Mini, Book-Tiefe, Kosten-Problem bei Micros): https://nexusfi.com/a/instruments/micro-e-mini-futures
- x-trade.ai — MES vs MNQ (Daily-Dollar-Range: MNQ $400–800 vs. MES $50–100; Drawdown-Mathematik): https://x-trade.ai/blog/mes-vs-mnq-prop-firm
- CME Group — Understanding Margin Changes & Margin Model (volatilitätsgetriebene, asymmetrische Margin-Anpassung; SPAN/SPAN2; Lookback-Methodik): https://www.cmegroup.com/education/articles-and-reports/understanding-margin-changes ; https://www.cmegroup.com/solutions/risk-management/performance-bonds-margins/futures-and-options-margin-model.html
- Fed Paper 2014-86 — Determinants of CME Margin Changes (empirisch: schnelle Erhöhung bei Vol-Spikes, träge Senkung — Prozyklizität): https://www.federalreserve.gov/econresdata/feds/2014/files/201486pap.pdf
- YMI — ES/NQ Pairs Trading (NQ ≈ 1,8–2,2× ES-Volatilität; Cointegration bricht in Regimewechseln; Korrelation > 0,85 Regime-abhängig): https://youngmoneyinvestments.com/blog/pairs-trading-strategy-futures-explained
- Finaur — VIX Time Band Strategy (VIX-Percentil als Regime-Schalter; Range-Kompression tötet intraday Setups): https://finaur.com/blog/en/free-strategies/vix-strategy-futures/
- TradeAlgo — ES/MES/NQ/MNQ Complete Guide (Kontraktspezifikationen, Margin-Tabellen, Kontogrößen-Empfehlungen): https://www.tradealgo.com/trading-guides/futures/e-mini-micro-e-mini-futures
- JustinTrading — Micro-Futures-Kommissionsfalle (MES/MNQ: RT-Gebühr relativ zum Tickwert strukturell kritisch; Mindest-Target-Anforderungen): https://justintrading.com/the-hidden-trap-of-micro-futures-commissions-why-scalping-mes-is-a-losing-game/
- Derivatives Journal — NQ vs MNQ (Kosten pro Notional 10× höher bei Micros; Margin-Vergleich): https://derivativesjournal.com/indices/nq-vs-mnq-which-contract
