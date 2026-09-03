# Feasibility — ID26 Zeitfenster-System

**Datum:** 2026-09-03 | **Idee:** Komplettes Handelssystem um ein einziges festes tägliches 30-Min-Fenster; Fenster-Wahl ist die vorregistrierte Hypothese.

## Antwort auf den Advocatus-Einwand

Der Einwand trifft zu, wo es um **direktionale Edge** geht, aber er trifft die Idee nicht in voller Breite — die ehrliche Antwort ist zweigeteilt:

1. **Direktionale Asymmetrie: Ja, es gibt einen dokumentierten, handelbaren Kandidaten — genau einen.** Das „Market Intraday Momentum"-Paper (Gao, Han, Li, Zhou, JFE 2018): Die erste halbe Stunde (RTH) prognostiziert die letzte halbe Stunde mit predictive R² ~1.6–2.6% (out-of-sample 1.4–2.0%). Das ist ökonomisch signifikant und wurde über Asset-Klassen repliziert (Zhang/Jacobs/Da: „Hedging demand and market intraday momentum", Sharpe 0.87–1.73). Der Effekt ist aber **ab 2022–2026 laut gex.live-Replikation (1.085 Sessions) auf Null abgeflacht** — Public-Decay ist real und dokumentiert. Das ist das ehrliche Kernrisiko: Das bekannteste Fenster-Signal ist möglicherweise bereits gehandelt/arbitriert worden.
2. **Volatilitäts-/Kosten-Asymmetrie: Ja, und die ist robust, weil mikrostrukturell begründet, nicht anomalie-basiert.** Die U-Form in Volumen, Volatilität und Spread ist seit Wood/McInish/Ord (1985) und Andersen/Bollerslev (1997) dokumentiert und wird bis 2024 bestätigt (Örebro WP 14/2025 auf ES/NQ 2016–2024: U-Form intakt, plus volumengetriebene Verstärkung; arXiv 2508.06788: 15-Min-Intervalle mit stark unterschiedlichen Spreads/Impacts). Diese Asymmetrie hebt kein Wirtsignal in den Brutto-Raum, aber sie verändert die **Kosten- und Varianz-Seite** der Gleichung um Faktoren (siehe Rechnung unten) — das ist ein echter, nicht-filternder Vorteil der Fenster-Reduktion.

Fazit zum Einwand: Die nach-Kosten-Asymmetrie zwischen 30-Min-Fenstern existiert, ist groß (Vola-Faktor ~2–3x, Spread-Verhältnis-Ratio noch größer) und robust — aber sie ist primär eine **Risiko/Kosten-Asymmetrie**. Eine **Brutto-Ertrags-Asymmetrie** (Signal) ist nur für das Open→Close-Momentum-Paar dokumentiert und dessen Post-Publikations-Decay ist belegt. Die Idee ist daher nur dann lebensfähig, wenn die Hypothese auf der Kosten/Varianz-Seite oder auf einem neuen, noch nicht publizierten Fenster-Signal aufbaut — nicht auf nahem Re-Trading von Gao et al. 2018.

## Dokumentierte Intraday-Asymmetrien (ES/NQ)

| Dimension | Befund | Quelle |
|---|---|---|
| Volatilität | U-Form über RTH: Open- und Close-30-Min ca. 2–3x Mittags-Vola; globex-weit mit Spikes 8:30 ET (Makro-News) und 14:55–15:00 | Andersen/Bollerslev 1997/98; Örebro WP 14/2025 (ES/NQ 2016–2024) |
| Volumen | U-Form; Power Hour & Open dominieren; Overnight-Session segmentiert (extrem dünn) | Wood et al. 1985; „Daytime vs. Overnight Trading in Equity Index Futures" |
| Spread/Liquidität | Spreads am weitesten rund um News/Illiquiditätsphasen; letzte 5 Min: enge Spreads, hohe Depth; Price Impact am höchsten 8:30–9:15 ET | arXiv 2508.06788 (1-Sekunden-BBO, ES) |
| Direktionale Prognose | Erste 30 Min → letzte 30 Min, R²_OOS ~1.4–2.9%; verstärkt an High-Vola-/High-Volume-/News-Tagen; getrieben von Hedging/Negative-Gamma + LETF-Rebalancing | Gao et al. 2018 (JFE); Zhang/Jacobs/Da (Hedging demand) |
| Decay | Letzte-30-Min-Fortsetzung 2022–2026 flach/null in jeder Jahreskohorte | gex.live Replikation |

## Nach-Kosten-Rechnung

Kostenannahmen (Round-Trip, inkl. Kommission + Gebühren, 1-Tick-Spread):

- MES: ~4–5 USD/RT. Tick = 1,25 USD. Kosten ≈ 3,5–4 Ticks ≈ 4–5 ES-Punkte-Äquivalent auf MES-Ebene... korrekt gerechnet: **Kosten in Punkten ≈ 1,0–1,25 ES-Punkte** (4–5 USD ÷ 5 USD/Punkt MES).
- MNQ: ~4–5 USD/RT. Tick = 0,50 USD (0,25 Pkt × 2 USD). Kosten ≈ **2–2,5 NQ-Punkte**.
- ES: ~12–15 USD/RT → ≈ 1 ES-Punkt (Tick 12,50 USD). NQ: ~12–15 USD/RT → ≈ 3 NQ-Punkte (Tick 5 USD).

Typische 30-Min-Ranges (RTH, ES, Normalregime): Open-30-Min ~15–25 Punkte, Mittag ~5–8 Punkte, letzte 30 Min ~10–15 Punkte.

**Kosten-Quote (Kosten ÷ Median-Range des Fensters):**

| Fenster | ES-Range | Kostenquote MES | Kostenquote ES |
|---|---|---|---|
| Open 9:30–10:00 | ~20 Pkt | ~6% | ~5% |
| Mittag 12:00–12:30 | ~6 Pkt | ~20% | ~17% |
| Close 15:30–16:00 | ~12 Pkt | ~10% | ~8% |

Ehrliche Lesart: Selbst im besten Fenster frisst der Round-Trip 5–10% der gesamten Fenster-Range — ein Trendfolge-/Momentum-System, das realistisch 10–30% der Range erntet, muss also ein Signal mit Trefferquote deutlich über 50% bei Payoff ~1:1 haben, nur um breakeven zu kommen. **Die Fenster-Wahl verändert die Kostenlast um Faktor ~3–4 zwischen bestem und schlechtestem Fenster** — das ist die starke, robuste Asymmetrie. Aber: Ein Kosten-Vorteil allein erzeugt keinen positiven Erwartungswert; er senkt nur die Hürde. Die Gao-et-al.-Regression (R² ~2%) impliziert eine Brutto-Edge von wenigen Basispunkten pro Trade — nach 1 Punkt Kosten auf ES-Niveau ist das **bestenfalls marginal, nach Decay-Daten (2022–2026) vermutlich negativ**.

## Zeitzone-Constraint (deutscher Trader, abends, 1–2 h/Tag)

US-RTH 9:30–16:00 ET = **15:30–22:00 MESZ** (Sommer; 16:30–23:00 MEZ im Winter). Erreichbare 30-Min-Fenster für 20:00–22:00 MESZ Feierabend-Trading:

- **21:00–21:30 MESZ = 15:00–15:30 ET** („Power Hour"-Beginn) — Sommer erreichbar.
- **21:30–22:00 MESZ = 15:30–16:00 ET** (letzte 30 Min, **das** dokumentierte Momentum-Fenster) — Sommer gerade noch erreichbar, im Winter (MEZ) erst 22:30–23:00 → **Winter-Problem**.
- 20:00–21:00 MESZ = 14:00–15:00 ET — Nachmittags-Session, moderate Vola, FOMC-Tage aktiv.

Konsequenz: Der harte Constraint zwingt faktisch auf **14:30–16:00 ET** (20:30–22:00 MESZ). Das Open (15:30 MESZ) ist abends nicht erreichbar. Glücklicherweise liegt das am besten dokumentierte Fenster (letzte 30 Min) genau im erreichbaren Bereich — **nur in der Sommerzeit**. Die DST-Asymmetrie (US/EU wechseln an verschiedenen Wochenenden) erzeugt 2× im Jahr 2–3 Wochen mit verschobenen Fenstern — muss im Testdesign explizit behandelt werden (alles in ET rechnen, nie in lokaler Zeit).

## Test-Design für QuantConnect (vorregistriert)

**Vorregistrierte Hypothese (Beispiel):** „Das Fenster 15:30–16:00 ET hat nach Kosten (MES, 1-Tick-Spread + 4,50 USD/RT) einen positiven Erwartungswert unter der Regel: Richtung = Vorzeichen der RTH-Return bis 15:30 ET (Intraday-Momentum); alle anderen Fenster sind per Konstruktion ausgeschlossen."

1. **Daten:** QC-Minutenbars ES (continuous, mapped), 2010–2025. Zeitzonen strikt America/New_York; DST-Gap-Wochen separat flaggen.
2. **Treatment:** Fester Entry 15:30 ET, Exit 15:55–16:00 ET (Market), Richtung nach Vorregistrierung. Kostenmodell: `ImmediateFillModel` mit fester Slippage = 1 Tick + Fee 4,50 USD (MES-bzw. ES-skaliert). Zusätzlich pessimistische 2-Tick-Slippage als Robustheit.
3. **Placebo (entscheidend):** Gleiche Regel, gleiche Länge (30 Min), aber Entry gleichverteilt über alle anderen RTH-30-Min-Slots (10:00–15:00 ET), n = 500 Bootstrap-Ziehungen von Placebo-Fenster-Mengen; plus „Random-Time-Placebo": gleiche Anzahl Trades an uniform zufälligen Minuten. Nullhypothese: Fenster-Edge ≤ Placebo-Verteilung. Bestehen nur, wenn Treatment > 95. Perzentil der Placebo-Sharpe-Verteilung **nach Kosten**.
4. **Multiple-Testing-Kontrolle:** Genau **ein** Fenster + eine Regel wird vorregistriert; jede weitere getestete Kombination wird mit Bonferroni/FDR markiert und zählt nicht als Bestätigung.
5. **Out-of-Sample/Decay:** Split 2010–2017 (Paper-Replikation), 2018–2021, 2022–2025 (Post-Publikations-/gex.live-Decay-Periode). Erwartung laut Literatur: drittes Segment flach → Design muss definieren, welches Segment entscheidend ist (Empfehlung: nur 2022+ zählt).
6. **Erfolgskriterium (vorregistriert):** Nach-Kosten-Sharpe > 0,5 in 2022–2025 UND > 95%-Placebo-Perzentil UND max. Drawdown < 3× Jahresvolatilität des Fensters.

## Quellen

1. Gao, Han, Li, Zhou (2018): *Market Intraday Momentum*, Journal of Financial Economics 129(2). https://www.sciencedirect.com/science/article/abs/pii/S0304405X18301351
2. Zhang, Jacobs et al. (Da): *Hedging Demand and Market Intraday Momentum*. https://academicweb.nd.edu/~zda/intramom.pdf
3. Örebro University WP 14/2025: *Volume-driven time-of-day effects in intraday volatility models* (ES/NQ/Euro/WTI, 2016–2024). https://www.oru.se/globalassets/oru-sv/institutioner/hh/workingpapers/workingpapers2025/wp-14-2025.pdf
4. *Returns and Order Flow Imbalances: Intraday Dynamics and Macroeconomic News Effects* (ES, 1-Sek-BBO). https://doi.org/10.48550/arxiv.2508.06788
5. *Intraday Trading Invariance in the E-mini S&P 500 Futures Market* (Kyle/Obizhaeva-Schule). https://pages.nes.ru/aobizhaeva/ABKO-intradayinv.pdf
6. *Daytime vs. Overnight Trading in Equity Index Futures Markets*. https://doi.org/10.5430/afr.v1n2
7. gex.live Research: *Is intraday momentum still alive?* (Replikation 2022–2026, n=1.085). https://gex.live/research/is-intraday-momentum-still-alive
