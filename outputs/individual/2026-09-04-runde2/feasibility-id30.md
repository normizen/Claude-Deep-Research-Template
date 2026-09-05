# Feasibility ID30 — Multi-Zwang-Dosis-Panel

**Idee:** Ordinaler Dosis-Test (Jonckheere-Terpstra) über kalenderöffentliche Zwänge (Index-Roll, Options-Verfall, CME-Margin-Hike-Stichtag). Hypothese: stärkere Intraday-Reversion am Zwang-Ende bei höherer Dosis (Anzahl gleichzeitig aktiver Zwänge).

**Instrument/Scope:** ES (E-mini S&P 500), Intraday, Stichprobe 2019–2026 (2015+ grundsätzlich möglich).

---

## Gate 1: Kalender-Baubarkeit — JA, in <1 Tag

| Komponente | Quelle | Status | Zugriffsweg |
|---|---|---|---|
| Opex-Tage (monatl. + Quartal) | Kalender-Logik (3. Freitag), verifizierbar via CME Expiration Calendar (`cmegroup.com/tools-information/calendars/expiration-calendar.html`) | **Ja** | Deterministisch berechenbar, kein Download nötig; QC liefert Verfallsdaten zusätzlich direkt aus den Kontraktsymbolen |
| CME-Roll-Kalender | CME "Equity Index Roll Dates" (`cmegroup.com/trading/equity-index/rolldates.html`): Roll = Montag vor dem 3. Freitag, historisch stabil | **Ja** | Deterministisch aus Opex-Daten ableitbar; zusätzlich empirisch messbar als Volumen-/OI-Umschlagstag aus QC-Daten (Front vs. Back-Kontrakt) |
| CME-Margin-Historie | (a) CME "Historical Margins" (`cmegroup.com/solutions/risk-management/margin-services/historical-margins.html`) — PDFs pro Produkt ab 2003, alle Änderungen mit Stichtag; (b) CME Advisory-Notices-Archiv (`cmegroup.com/notices.html`, vor 2008 separat); (c) >5 Jahre via CME DataMine (CSV) | **Ja** | PDF/CSV für ES herunterladen, Stichtage der Hikes extrahieren; keine Scraping-Hürde, öffentlich |

**Aufwand:** Alle drei Label-Quellen sind öffentlich, kostenlos und ohne Login (DataMine ggf. Registrierung). Konservativ < 4 Stunden inkl. QC-Validierung des Volumen-Umschlags.

## Gate 2: Power-Check — FAIL

Grobe Tageszählung 2019-01-01 bis 2026-09-05 (~1.950 Handelstage nach Feiertagsbereinigung):

- **Opex:** 92 Monats-Verfälle, davon 30 Quartals-Opex (Triple Witching).
- **Roll-Fenster:** Selbst mit großzügigem empirischem Fenster (Do der Vorwoche bis Opex-Fr, ~7 Handelstage/Quartal) = ~210 Tage — aber diese überlappen strukturell nur mit **genau den 30 Quartals-Opex-Tagen** (der Freitag liegt immer im eigenen Rollfenster; die übrigen 62 Monats-Opex liegen per Konstruktion nie in einem).
- **Margin-Hikes:** ES-Hikes seit 2019 sind auf den COVID-Cluster (Feb–Apr 2020, mehrere Stufen) plus wenige Einzelhikes (2022) beschränkt — realistisch **~8–12 Stichtage**. Zufallsüberlappung mit Opex/Roll: ~0–1 Tag.

**Ergebnis: Dosis-≥2-Tage = 30 (Roll+Opex am Quartalsfreitag) + ~0–1 (Hike-Zufall) ≈ 30–31. Dosis-3-Tage = 0–1.**

JT-Test über 3 Dosis-Stufen mit n₀≈1900, n₁≈190, n₂≈30, n₃≈1: Die Dosis-3-Zelle ist leer, Dosis-2 ist mit n≈30 ein reines Quartals-Opex-Subsample. **Nach Vola-Stratifizierung (z. B. 3 Vola-Terzile) bleiben ~10 Tage pro Dosis-2-Zelle** — für einen ordinalen Trend-Test mit Multiple-Testing-Korrektur und Intraday-Reversion als heteroskedastischer Zielgröße nicht ausreichend (Faustregel: JT braucht ≥ ~30–50 Beobachtungen je geordneter Gruppe für moderate Effekte). Der Test kollabiert faktisch auf "Quartals-Opex vs. Rest" — also auf ID29.

## Gate 3: Outright-Kanal — schwach bis konträr

- **Roll:** Literatur zeigt überwiegend **Spread-/Terminstruktur-Effekte**, keinen Outright-Druck. Irwin/Sanders/Yan (2023, *AEPP*): Index-Roll drückt den Nearby-Deferred-Spread um 30–40 bp mit voller Reversion — aber 1980–2011; **2012–2019 verschwindet der Spread-Effekt weitgehend**. Mou (2011, "Front-Running the Goldman Roll"): Rohstoffe, pre-2010, ebenfalls Spread-Kanal. Die Reversion ist also (a) altregime, (b) spread-basiert, nicht outright. Für ES-Roll ist der Outright-Kanal nicht belegt; Erwartung: nahe null, da der Roll als Exchange-for-Physical-/Spread-Trade abläuft.
- **Opex:** Golez & Jackwerth (2012, *JFE*): Pinning/Anti-Pinning am S&P-500-Future an Verfallstagen — gerichteter Verzerrungs-Kanal (Anziehung/Abstoßung zu Strikes), **keine generelle Reversion**. Henderson/Pearson/Wang (JFQA, witching days): signifikante **Reversion der Opening-Moves innerhalb von ~60 Minuten** am Witching-Tag — das ist der stärkste direkte Beleg für die Intraday-Reversions-Hypothese, allerdings im Kassa-Öffnungsprozess, nicht als Zwang-Ende-Effekt des Futures. Zenodo-Replikation (2025, 2.294 Tage): Pinning seit 2016 verschwunden, stattdessen **Gamma-Amplifikation** (16 % breitere Ranges) — Regimewechsel gegen die Reversions-Hypothese.
- **Margin-Hike:** AQR/Jylhä ("Causes and Consequences of Margin Levels in Futures", ~350 Hikes): **kein signifikanter Effekt auf das Preisniveau**, aber +50 % realisierte Varianz am Hike-Tag und anhaltend erhöht danach. Silber 2011 ist die populäre Anekdote, aber atypisch. Für ID30 fatal doppelt: kein Outright-Reversions-Kanal **und** direkter Vola-Konfounder (Hikes folgen Vola-Spikes und erzeugen selbst Vola — die Vola-Stratifizierung aus Gate 2 würde die Hike-Zelle selektiv mit Hoch-Vola-Tagen füllen).

---

## Schlussurteil: DEGRADIERT ZU ID29-KALENDER

Gate 1 besteht (Kalender in <1 Tag baubar), aber Gate 2 fällt hart (n≈30 Dosis-2-Tage, 0–1 Dosis-3-Tage, keine Power nach Vola-Stratifizierung) und Gate 3 entzieht zwei von drei Komponenten den Outright-Reversions-Kanal (Roll = Spread-Phänomen mit post-2012-Abnahme; Hike = Vola-Effekt ohne Preisniveau-Effekt). Der Dosis-Test wäre zudem intern inkonsistent: Er aggregiert Komponenten mit unterschiedlichen — teils gegenläufigen (Pinning vs. Amplifikation) — Wirkungskanälen in eine ordinale Skala, ohne dass der gemeinsame "Zwang-Ende-Reversion"-Mechanismus für Roll und Hike belegt ist.

**Empfehlung:** Kein eigenständiges Panel. Die drei Label-Serien (Roll-Fenster, Opex, Hike-Stichtage) sind billig baubar und als **Kalender-Covariaten/Exklusionsfilter für ID29** (und andere Intraday-Studien) wertvoll — insbesondere die QC-messbare Volumen-Umschlagsvariable und die Margin-Hike-Stichtage als Vola-Regime-Indikator.
