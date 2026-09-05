# Experiment-Designs — Runde 2 (2026-09-04)

## ID29 — „Prop-Close-Ernte": Konditionierte Close→Overnight-Reversion (Flat-Zwang 16:00–16:59 ET)

**Status:** GO bedingt (siehe feasibility-id29.md). Vorregistriert VOR erstem Datenkontakt (Datenfalle 5).
**Code:** `code/qc_id29_prop_close_test.py` (eine QC-Research-Notebook-Zelle).

### Axiom-Basis
- **A18 (Zwangsmechanik-Katalog):** Erzwungener Flow hat Auslöser (Prop-Regelwerk: Flat bis 16:59 ET), Zeitfenster (16:00–16:59 ET), Träger (Prop-Firm-Eval/Funded-Kohorte, MES/MNQ-Größe).
- **A19 (Erzwungener Flow ist informationslos):** Der Flat-Flow MUSS handeln, die Gegenseite KANN warten → temporäre, reversible Preisverzerrung. Handelbarer Moment: das ENDE des Zwangs (Globex-Reopen 18:00 ET).
- **A20 (Retail-Zwänge sind der konkurrenzfreieste Flow):** Prop-Regeln sind öffentlich dokumentiert, der Flow ist zu klein/schmutzig für institutionelle Ernte — die eine Achse mit strukturellem Retail-Vorteil.

### Gebrochene Dogmen
- **D17 („Edge = informierter sein"):** Gegenthese — Edge aus der Informationslosigkeit des Gegenflows; Kalender statt Information.
- **D18 („Man braucht Informationsvorsprung"):** Gegenthese — Zwangsmechanik ist öffentlich und nicht arbitrage-zerstörbar, weil der Zwang nicht verschwindet, wenn man ihn kennt.

### Mechanik-Kern
Prop-Firm-Regelwerke (Apex: flat bis 4:59 PM ET mit Auto-Liquidation; Topstep analog) zwingen die Futures-Kohorte, Positionen im ETH-Fenster 16:00–16:59 ET glattzustellen — NACH dem Cash-Close, im dünnsten Volumen des Tages. An Trendtagen kippt die Netto-Richtung der Kohorte einseitig GEGEN die Tagesbewegung (Gewinner der Tagesrichtung werden gewinnrealisiert, Verlierer gestoppt) → gerichteter Zwangsdruck 16:00–16:59 ET, der sich nach Ende des Zwangs (Globex-Reopen 18:00 ET) teilweise zurückbildet.

### Vorregistrierte Hypothese (exakt aus Feasibility)
- **Hauptzelle:** ETH-Fenster-Analyse (16:00–16:59 ET Flat-Zwang-Fenster vs. Cash-Close-MOC), konditioniert auf Tagesrichtung (RTH-Return) × Trendcharakter (letzte 30 RTH-Min verstärken vs. drehen).
- **Netto-Schwelle:** ≥ 3 bps konditionierter Effekt NACH Kosten (RT $13,50/ES, ID26-Konvention).
- **3 Attributionssignaturen (alle müssen gleichzeitig in Prop-Richtung zeigen):**
  1. **ETH-Zeitfenster:** (a) konditionierter Gegen-Trend-Drift 16:00–16:59 ET stärker als 15:30–16:00 ET (volumennormiert); (b) Reversion 18:00–19:00 ET lädt auf den ETH-Drift, nicht auf den RTH-Close-Drift. Placebo-Fenster: 14:30–15:00 und 15:00–15:30 ET.
  2. **Dosis-Ordnung (Jonckheere-Terpstra, p < 0,05):** Verfall-Freitag > Freitag > Verfall-Wochentag > normaler Wochentag.
  3. **Decay-Split (Pflicht-Falsifikator):** Effekt 2022+ ≥ Effekt 2019–2021. Die Prop-Kohorte existiert in relevanter Größe erst post-2021 — ein echter Prop-Effekt DARF 2019–2021 nicht existieren. Umgekehrte Richtung = Attribution gescheitert (KIMI-Einwand bestätigt).
- **ID30-Kalender-Labels** (Roll-Fenster, Opex, Margin-Hike-Stichtage) werden als Covariaten mitgeführt (siehe unten).

### Alpha-Vorteil (warum nicht wegarbitriert)
Der unbedingte Overnight-Effekt ist bepreist (Boyarchenko/Larsen/Whelan RFS 2023; NightShares-ETFs). Nicht bepreist: (1) Reversion nach Trend-Up-Tagen STÄRKER als Boyarchenkos unbedingte Asymmetrie impliziert; (2) Trendcharakter-Konditionierung als zweite Achse; (3) ETH-Zeitfenster-Signatur 16:00–16:59 ET (Literatur misst am Cash-Close, nicht im ETH-Fenster). Geschätzter Netto-Raum: 2–8 bps konditioniert, Break-even ~3 bps.

### Abnahmekriterien (vorregistriert)
| Kriterium | Schwelle |
|---|---|
| Cliff's d (konditioniert vs. Kontrolle) | ≥ 0,10 |
| Placebo-Perzentil (500 Fenster-Permutationen) | > 95 % |
| Dosis-Ordnung (JT-Test) | p < 0,05, vorregistrierte Ordnung |
| Decay-Split | 2022+ ≥ 2019–2021 (Pflicht) |
| Netto-Effekt | ≥ 3 bps nach RT-Kosten |

### Abbruchkriterien
- Jede der drei Signaturen schlägt fehl → Hypothese tot, KEINE Neu-Fenster-Suche im selben Datensatz (Datenfalle 5).
- Decay-Split umgekehrt (Effekt 2019–2021 > 2022+) → Prop-Attribution gescheitert, auch bei positivem Gesamteffekt: NICHT ernten (GEX-Wall-Falle: generischen Overnight-Effekt mit Prop-Etikett ernten und gegen NightShares konkurrieren).
- Netto < 3 bps nach Kosten → nicht handelbar für 5–10k-€-Konto, archivieren.

### Kosten
RT $13,50/ES all-in (Kommission + Gebühren + 1 Tick Slippage, ID26-Konvention). Daten: QC-Cloud, 0 $ (ES-Minutenbars inklusive). Weit unter 50-$-Budget.

### Datenfallen-Checkliste (im Code-Header gespiegelt)
1. Keine Preisreihen-Mischung: continuous future, OPEN_INTEREST / BACKWARDS_RATIO, dokumentiert.
2. Placebo Pflicht: 500 Fenster-Permutationen.
3. Keine geglätteten Profile: rohe Minutenbars.
4. Abstain-Zustand: FOMC/CPI/NFP + dünne ETH-Fenster ausgeschlossen UND gezählt.
5. Vorregistrierung vor Datenkontakt (dieses Dokument).
DST: strikt ET (QC liefert Exchange-Zeit), DST-Übergangswochen geflaggt, Robusta ohne sie.

---

## ID30 — Multi-Zwang-Dosis-Panel: DEGRADIERT zu Kalender-Covariaten

Gate 2 (Power) hart gefallen: Dosis-≥2-Tage ≈ 30–31 (nur Quartals-Opex im Roll-Fenster), Dosis-3 ≈ 0–1 — nach Vola-Stratifizierung ~10 Tage/Zelle, keine JT-Power. Gate 3 entzieht Roll (Spread-Phänomen, post-2012 abnehmend) und Margin-Hike (Vola-Effekt, kein Preisniveau-Effekt, direkter Vola-Konfounder) den Outright-Reversions-Kanal.

**Übernahme in ID29:** Die drei Label-Serien laufen als Covariaten im ID29-Code mit: `is_opex_friday` (3. Freitag), `is_roll_window` (Montag vor 3. Freitag bis Verfall), `is_quad_witching` (Quartals-Opex), `is_margin_hike` (Stichtage aus CME Historical Margins — extern zu befüllen, Code behandelt leere Liste sauber und warnt). Opex/Roll sind zusätzlich funktional: Sie bilden die Dosis-Stufen des Signatur-2-Tests (Verfall-Freitag / Verfall-Wochentag).

---

## ID34 — Duplikat-Befund: in ID29 aufgegangen

ID34 ist inhaltlich identisch mit ID29 (gleiche Zwangsmechanik, gleiche Fenster-Logik, gleiche Zielvariable) — kein eigenständiger Mechanismus, kein eigenes Experiment nötig. Verwaltet wird nur ID29; ID34 wird nicht separat kodiert. Vermerk in idea-outcomes.md empfohlen: „ID34 = Duplikat von ID29, konsolidiert."
