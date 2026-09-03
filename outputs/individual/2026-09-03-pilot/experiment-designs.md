# Experiment-Designs — Pilotlauf 2026-09-03

Erstellt: 2026-09-03 · Rolle: Implementation Designer
Abnahmekonvention (aus project-context.md): Cliff's d ≥ 0,10 · Placebo-Kontrolle Pflicht ·
Vorhersagen VOR dem Test festschreiben · Filter brauchen Abstain-Zustand · keine gemischten Preisreihen.

---

## ID24 — Instrumenten-Apoptose (6-Kriterien-Eliminierungsturnier)

### Axiom-Basis
- **A11 (Kosten-Rendite-Schere):** All-in-RT-Kosten relativ zur geerntbaren Range entscheiden über ökonomische Tragfähigkeit — das ist das harte Kriterium K1.
- **A12 (Spielfeld-Asymmetrie):** Nicht-Teilnahme kostet nichts — der Default des Turniers ist *Eliminierung*, nicht Behalten. Abstain auf Instrumenten-Ebene ist ein struktureller Retail-Vorteil.
- **A15 (Marktauswahl ist Axiomen-Entscheidung):** ES/MES vs. NQ/MNQ sind nicht austauschbar; Micros sind ein dritter Markt, keine Skalierung — deshalb werden alle vier separat bewertet.
- **A3+A17 (Constraints):** 5–10 k€ Kapital, 1–2 h/Tag → K2/K3/K6 operationalisieren genau diese Ressourcen.

### Gebrochenes Dogma
„Wähle einmal dein Instrument und bleib dabei" (Buy-and-hold auf Instrumenten-Ebene). Das Turnier ersetzt einmalige Due Diligence durch einen wiederkehrenden, regelbasierten Sterbeprozess mit Default = Tod.

### Mechanik-Kern
Zwei Klassen von Todeskriterien (aus feasibility-id24.md):
1. **Einmalige Disqualifikation** (stabile Dimensionen: Tickwert, Gebührenstruktur) — Due-Diligence-Charakter, jährlicher Re-Check.
2. **Wiederkehrende Eliminierung** (regime-abhängig: Tagesrange, Margin, Vol-Prämie, Korrelation, Liquidität) — monatliche Messung.

Das Turnier reduziert sich ehrlich auf 3 unabhängige Entscheidungen: (a) S&P- vs. Nasdaq-Familie, (b) Micro vs. Mini, (c) Gesamtklassen-Eliminierung bei Volatilitätskollaps.

### Alpha-Vorteil
Kein direktionaler Alpha — sondern **Kosten-/Ruin-Vermeidung**: Das Turnier verhindert, dass in VIX-Kompressions- oder Margin-Spike-Regimen weiter Instrumente gehandelt werden, deren Kosten die Range strukturell übersteigen (MES bei 7 % Kosten/Range ist tot, bevor der erste Trade läuft). Der Vorteil ist vermiedener negativer Erwartungswert — monetarisierbar über A11.

### Die 6 Todeskriterien (vorab registriert, Schwellwerte fixiert)

| # | Kriterium | Schwellwert | Messintervall | Datenquelle |
|---|---|---|---|---|
| K1 | Kosten-Range-Schere (hart, sofort) | All-in-RT-Kosten > 5 % der 20-Tage-Ø-Dollar-Range | monatlich | `id24_range_monitor.py` (QC-Daily-Bars) + Broker-Gebühren |
| K2 | Setup-Tragfähigkeit | Setup-Stop × Tickwert > 1 % Kapital ODER 2-%-Risiko nicht mit 1,5:1 R:R an Range erreichbar, 20-Tage-Median | monatlich | Trade-Log + Range-Daten |
| K3 | Margin-Suffokation | (Overnight-Margin × 2) > 40 % Kapital ODER (Day-Margin × Setup-Kontrakte) > 25 % Kapital | monatlich | CME-Margin-Bulletins + Broker |
| K4 | Redundanz | Rolling-60d-Korrelation Tagesreturns > 0,90 UND Vol-Prämie < 1,3× | monatlich | QC-Daily-Bars beider Familien |
| K5 | Liquiditäts-/Slippage-Bruch (hart, sofort) | Ø-Slippage > 1 Tick/RT über 20 Trades ODER Spread > 1 Tick im eigenen Fenster an > 30 % der Tage | laufend (Trade-Log) | Broker-Export / Trade-Log |
| K6 | Zeitbudget-Kompatibilität | > 60 % der 20-Tage-Range entsteht außerhalb des verfügbaren Handelsfensters | monatlich | QC-Minutenbars (Session-Aufschlüsselung) |

**Eliminierungsregel:** Verletzung von ≥ 2 Kriterien in 2 aufeinanderfolgenden Monaten → Eliminierung. Verletzung von K1 oder K5 allein → sofortige Eliminierung. Default bei Datenlücke = Eliminierung (nicht Behalten). Pro Quartal genau **ein** schriftlicher Begnadigungsantrag mit neuem Datenpunkt erlaubt.

### Monatlicher Ablauf (~1 h, letzter Handelstag)
1. [ ] `id24_range_monitor.py` auf frischen QC-Daily-Bars laufen lassen → K1-Tabelle (5 min)
2. [ ] CME-Margin-Bulletin prüfen, Overnight-/Day-Margins gegen Kapital → K3 (10 min)
3. [ ] Rolling-60d-Korrelation ES↔NQ + Vol-Prämie aus Daily-Daten → K4 (10 min)
4. [ ] Trade-Log: Slippage-Schnitt letzte 20 Trades, Spread-Quote im Fenster → K5 (10 min)
5. [ ] Session-Anteil der Range (aus Minutenbars oder geschätzt via QC) → K6 (10 min)
6. [ ] K2 mit aktuellem Setup-Stop rechnen (5 min)
7. [ ] Bewertungs-Matrix ausfüllen, Status je Instrument (lebendig/bedingt/tot), Protokoll ablegen (10 min)

### Abbruchkriterien (für die Idee selbst)
- Turnier erzeugt 6 Monate lang keine einzige Statusänderung → Prozess ist Gewohnheits-Farce, Idee als *wiederkehrender* Prozess gescheitert (Due-Diligence-Charakter bestätigt).
- Datendisziplin (Slippage-Logging) bricht zusammen → K5 nicht messbar → Turnier suspendiert, nicht geschönt.

### Kosten
- Daten: 0 $ (QuantConnect Cloud, Daily/Minutenbars ES/NQ/MES/MNQ kostenlos).
- Aufwand: ~1 h/Monat Median, ~2 h in Turniersmonaten (quartalsweise). Kein QC-Backtest nötig.

### Artefakte
- Bewertungs-Matrix: Markdown-Template unten (Abschnitt „ID24 Bewertungs-Matrix").
- Code: `code/id24_range_monitor.py` — berechnet 20-Tage-Dollar-Ranges + Kosten/Range-Ratios für ES/NQ/MES/MNQ aus QC-exportierten Daily-Bars (CSV).

---

## ID26 — Zeitfenster-System (ein vorregistriertes 30-Min-Fenster)

### Axiom-Basis
- **A16 (Filter-Wirt-Theorem):** Die Fenster-Wahl ist *kein* Wirtssignal — sie verändert nur die Kosten-/Varianz-Seite. Deshalb ist die primäre, entscheidende Hypothese die **Kostenquote-Asymmetrie** (robust, mikrostrukturell begründet, U-Form); das Momentum-Signal (Gao et al. 2018) ist explorativ mit dokumentiertem Decay-Risiko.
- **A11 (Kosten-Frequenz-Schere):** 1 Ereignis/Tag in einem Fenster mit 3–4× niedrigerer Kostenquote ist der gangbare Raum der Schere.
- **A17 (Validierungszeit):** Validierung wird auf QC-Historie (2019–2026) ausgelagert — Live-Ausprobieren wäre epistemisch unerreichbar.
- **A13:** Kein nacktes Reversion-Signal im Fenster; Richtung nur via vorregistriertem Intraday-Momentum, das selbst auf Decay geprüft wird.

### Gebrochenes Dogma
„Mehr Bildschirmzeit = mehr Edge" / „Der ganze Handelstag ist Chancenraum". Gegenentwurf: maximale Reduktion auf ein einziges, vorab fixiertes 30-Min-Fenster; der Rest des Tages ist per Konstruktion ausgeschlossen (Abstain als Default, A12).

### Mechanik-Kern
Intraday-U-Form in Volatilität, Volumen und Spread (Wood et al. 1985; Andersen/Bollerslev 1997; Örebro WP 14/2025 bis 2024 intakt): Die Kostenquote (RT-Kosten ÷ Fenster-Range) unterscheidet sich zwischen bestem und schlechtestem 30-Min-Fenster um Faktor ~3–4. Das Ziel-Fenster 15:30–16:00 ET liegt zusätzlich genau im erreichbaren Zeitbudget eines deutschen Abend-Traders (21:30–22:00 MESZ, Sommer).

### Alpha-Vorteil
1. **Primär (entscheidend):** Kosten-/Varianz-Asymmetrie — niedrigere Hürde für jedes zukünftige Wirtssignal; kein eigenständiger Erwartungswert.
2. **Explorativ (sekundär):** Market Intraday Momentum (erste 30 Min → letzte 30 Min, Gao et al. 2018, JFE). gex.live-Replikation zeigt Abflachung auf ~null ab 2022 — deshalb ist das Segment **2022+ das entscheidende**, nicht ein In-Sample-Sieg 2019–2021.

### Vorregistrierte Vorhersagen (VOR Testausführung fixiert)
1. Kostenquote (RT-Kosten / mittlere Fenster-Range) im Ziel-Fenster 15:30–16:00 ET ist **mindestens Faktor 3 niedriger** als der Median über alle RTH-30-Min-Fenster.
2. Explorativ: Erst-30-Min → letzt-30-Min Momentum ist im Segment 2022+ flach/negativ (Decay-Hypothese nach gex.live). Ein positives Ergebnis 2019–2021 bei negativem 2022+ zählt als **Bestätigung des Decays**, nicht als Signal-Erfolg.

### Abnahmekriterien (vorab)
Der Fenster-Vorteil gilt nur bei **beiden**:
- Cliff's d ≥ 0,10 (Kostenquote Ziel-Fenster vs. alle anderen Fenster)
- Ziel-Fenster liegt oberhalb des **95%-Perzentils von 500 Placebo-Fenstern** (zufällige 30-Min-Fenster gleicher Stichprobenzahl)

### Datenfallen-Behandlung (Pflicht)
1. **Preisreihen-Mix:** Nur QC continuous backadjusted ES; Adjustierungsmethode im Code dokumentiert, keine Mischung mit Roh-Kontraktserien.
2. **Placebo:** 500 Zufallsfenster — ohne Placebo kein Befund.
3. (Glättung: n/a — keine Profile, rohe Minutenbars.)
4. **Abstain-Logik:** Tage ohne ausreichende Liquidität im Fenster (Volumen-Schwelle) werden ausgeschlossen **und gezählt** — kein stilles Filtern.
5. **Vorab-Registrierung:** Hypothesen und Abnahmekriterien stehen im Header-Kommentar des Codes, vor Ausführung.
- **DST-Falle:** Alle Zeiten strikt America/New_York (ET); US/EU-Sommerzeit-Übergänge weichen 2× jährlich 2–3 Wochen ab — im Code nie in Lokalzeit rechnen, Übergangswochen werden explizit markiert.

### Test-Design (Implementiert in `code/qc_id26_fenster_test.py`)
- **Daten:** QC ES-Futures-Minutenbars (continuous, backadjusted), 2019–2026, strikt ET.
- **Treatment:** Fenster 15:30–16:00 ET; Kostenquote = RT-Kosten (ES: 1 Tick Slippage + Gebühren ≈ $12–15) ÷ mittlere Fenster-Range in $.
- **Placebo:** 500 zufällige 30-Min-Fenster (gleiche Stichprobenzahl), Perzentil-Rang des Treatments.
- **Decay-Split:** 2019–2021 vs. 2022+ — nur 2022+ ist entscheidend für das Momentum-Signal.
- **Output:** Tabelle Kostenquote pro Fenster, Cliff's d, Placebo-Perzentil, Momentum-Statistik mit Decay-Split.

### Abbruchkriterien
- Kostenquote-Vorteil < Faktor 3 oder Cliff's d < 0,10 oder ≤ 95%-Placebo-Perzentil → Fenster-Hypothese **tot** (keine Neu-Fenster-Suche im selben Datensatz — das wäre Datenfalle 5).
- Momentum 2022+ positiv, aber < Placebo-Perzentil → Signal nicht handelbar, wird dokumentiert und nicht „optimiert".

### Kosten
- 0 $ (QC-Cloud kostenlos, Minutenbars ES vorhanden). Ausführung: manuell durch User als QC-Notebook-Zelle, ~10–30 min Rechenzeit.

---

## ID24 Bewertungs-Matrix (ausfüllbares Template)

**Turnier-Monat:** ____  ·  **Kapital:** ____ €  ·  **Datum:** ____

| Instrument | K1 Kosten/Range ≤ 5 % | K2 Setup tragfähig | K3 Margin ok | K4 nicht redundant | K5 Slippage ≤ 1 Tick | K6 Fenster-Abdeckung ≥ 40 % | Verletzungen | Status |
|---|---|---|---|---|---|---|---|---|
| ES  | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | _/6 | ☐ lebendig ☐ bedingt ☐ **tot** |
| MES | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | _/6 | ☐ lebendig ☐ bedingt ☐ **tot** |
| NQ  | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | _/6 | ☐ lebendig ☐ bedingt ☐ **tot** |
| MNQ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | _/6 | ☐ lebendig ☐ bedingt ☐ **tot** |

**Messwerte dieses Monats (Datenquellen):**

| Messgröße | Wert | Quelle |
|---|---|---|
| 20-Tage-Ø-Range ES ($) | | id24_range_monitor.py |
| 20-Tage-Ø-Range MES ($) | | id24_range_monitor.py |
| 20-Tage-Ø-Range NQ ($) | | id24_range_monitor.py |
| 20-Tage-Ø-Range MNQ ($) | | id24_range_monitor.py |
| RT-Kosten all-in ES/MES/NQ/MNQ ($) | | Broker-Statement |
| Overnight-Margin ES/NQ ($) | | CME-Margin-Bulletin |
| Day-Margin MES/MNQ ($) | | Broker |
| Rolling-60d-Korrelation ES↔NQ | | Daily-Bars |
| NQ/ES-Vol-Prämie (×) | | Daily-Bars |
| Ø-Slippage letzte 20 Trades (Ticks) | | Trade-Log |
| Tage mit Spread > 1 Tick im Fenster (%) | | Trade-Log |
| Range-Anteil im eigenen Fenster (%) | | QC-Minutenbars |
| VIX-Close / Percentil | | Marktdaten |

**Entscheidungen:**
- Eliminierungen dieses Monat: ____
- Begnadigungsantrag gestellt (max. 1/Quartal): ☐ nein ☐ ja — Begründung/neuer Datenpunkt: ____
- Notizen: ____
