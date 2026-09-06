# Experiment-Designs — Runde 4 (2026-09-06)

**Status:** ID67o test-fertig (Code vorliegend), ID61o + ID63o zurückgestellt (Redesign nötig).

---

## ID67o — Batch-minus-Marginal-Residual (BMR)

### Axiom-Basis & Dogmen

- **A28 (Axiom):** Märkte mit pflichtgehandeltem Batch-Preis (CME-Settlement = 30-s-VWAP,
  gerundet auf 0,25 ES-Punkte) erzeugen eine messbare, kalenderfeste Diskrepanz zwischen
  dem Batch-Preis und dem letzten marginalen Preis davor.
- **A29 (Axiom):** Die Settlement-Zahlen sind öffentlich und kostenlos, aber in keinem
  Retail-Datenfeed (QC Daily-Close = letzter Trade des Kalendertags, NICHT das Settlement)
  repräsentiert — der Repräsentations-Vorsprung ist real und bleibt durch die Pflicht-
  Datenquelle (CME-Settlements-Seite) sogar gestützt.
- **D25 (Dogma, dekonstruiert):** „Der Settlement-Preis ist nur ein administrativer
  Buchungspreis ohne Informationsgehalt." — Wenn der Batch-Preis systematisch vom
  marginalen Preis abweicht und die Abweichung Folgetag-RTH-Open-Richtung vorhersagt,
  ist D25 widerlegt.
- **D26 (Dogma, dekonstruiert):** „Intraday-Preisdifferenzen unter einem Tick sind
  Rundungsrauschen ohne Struktur." — Die Rundung selbst ist deterministisches
  Marktdesign (0,25-Grid), kein Rauschen; symmetrisch konstruierte Placebos tragen
  dasselbe Grid.

### Mechanik-Kern

Der CME-Batch-Prozess (VWAP 14:59:30–15:00:00 CT, gerundet auf nearest 0,25) fixiert
einen Preis, der von der letzten marginalen Notierung (Close des Minutenbars 14:59 CT)
abweichen kann. Diese Abweichung — **BMR = Settlement_CME − Close(Bar 14:59 CT)** —
ist kein Zufallsfehler, sondern aggregiert die Batch-Nachfrage des Settlement-Fensters.
Hypothese: sign(BMR) bei |BMR| ≥ Guard enthält gerichtete Information über die
RTH-Erststunde des Folgetags ( institutionelle Settlement-Flüsse setzen sich fort).

### Die 3 Gate-Lösungen (exakt umgesetzt)

**Gate 1 — Rundungsfalle (Symmetrie):**
- Treatment: Settlement aus der **öffentlichen CME-Settlements-Seite** (CSV oder
  QC-Settlement-Field falls vorhanden), per Datum+Lead-Month auf den QC-Continuous
  gemappt. Defensive Abfrage mit **Fallback auf Daily-Close mit Warnung**.
- NICHT aus Minutenbars approximieren (30-s-VWAP nicht berechenbar).
- Placebo (Pseudo-Anker): Typical-Price (H+L+C)/3 des Minutenbars **13:59 CT**,
  danach auf nearest 0,25 gerundet — **identische Rundungsoperation** wie das echte
  Settlement. Beide Größen leben auf demselben 0,25-Grid.
- Vorab-Validierung: 20-Tage-Stichprobe, CME-Settlement gegen QC-Daily-Close,
  Differenz muss ≠ 0 sein und auf dem 0,25-Grid liegen.

**Gate 2 — Überlebensrate-Gate VOR Haupttest:**
- **Erster Analyseschritt im Code** (vor jeder Inferenz): Verteilung von
  |BMR| = |Settlement − Close(Bar 14:59)| in instrumenteigenen Punkten.
- Abbruchregel: Überlebensrate bei Guard 0,5 (ES) / 1,0 (NQ) < **15 %** → Eskalation
  auf Guard = ein Rundungs-Quantum (0,25 ES). Dort < 15 % → **NO-GO ohne Haupttest**,
  klare Ausgabe.
- Guard ist instrument-spezifisch (ES ≠ NQ, keine Punktemischung).

**Gate 3 — Kontrolle (dreistufig):**
1. **Haupt-Inferenz:** 500 blockweise Vorzeichen-Permutationen (Monatsblöcke, um die
   Monatsend-Dosis-Struktur nicht wegzupermutieren), Placebo-Perzentil > 95 % gefordert.
2. **Jonckheere-Monotonie:** Effektstärke monoton über Monatsend-Strata
   {Monatsend-Tage > übrige Monatswoche > Rest} — kalenderfest, kurvenanpassungsfest.
3. **GC/ZB-Falsifikator:** GC = Placebo-Anker (12:30 CT, Effekt = generisches
   Risiko-Muster, kein BMR); ZB = Rundungs-Falsifikator mit **eigener 1/64-Rundung**
   — ein „Effekt" in ZB darf nur auf dem ZB-Grid erscheinen, nicht auf dem ES-Grid.
   Erscheint er nur bei falscher 0,25-Rundung, ist die Rundungsfalle als real
   nachgewiesen und der Guard als korrekt bestätigt.

### Alpha-Vorteil

- Kalenderfest (jeden Handelstag, keine Event-Abhängigkeit), ausführbar MES/MNQ
  (Klasse II, Kosten unkritisch, Netto/Kosten ≈ 4× laut Pre-OPUS).
- A29-Repräsentations-Vorsprung: QC liefert keinen nativen Settlement-Preis — wer nur
  QC-Daten nutzt, sieht das Feld nicht.

### Abnahmekriterien (vorregistriert)

| Kriterium | Schwelle |
|---|---|
| Daten-Mapping | 20-Tage-Grid-Check bestanden (CME ≠ QC-Close, auf 0,25-Grid) |
| Überlebensrate (Abbruchregel) | ≥ 15 % bei Guard 0,5 ES / 1,0 NQ; sonst Guard 0,25; sonst NO-GO ohne Haupttest |
| Haupttest | Placebo-Perzentil > 95 % (n = 500), Cliff's d ≥ 0,10 |
| Monotonie | Jonckheere p < 0,05 über Monatsend-Strata |
| Falsifikatoren | GC nicht signifikant; ZB-Effekt nicht auf ES-Grid |
| Power | Hit-Rate > 52 % bei n ≥ 500 Replikate gesamt |
| Decay-Split | 2022+ vs. davor berichtet (2022+ entscheidend) |

### Kosten

≤ 50 $ (CME-Settlements-CSV öffentlich/kostenlos; QC-Cloud-Compute inklusive;
manuelles CSV-Loading durch User ~1 h).

---

## ID61o — Anker-Staffel-Kaskade — ZURÜCKGESTELLT

**Grund:** Vortex Capital Group (2026, „The 1PM Echo") hat die Auction-Echo-Variante
bereits publiziert (1.370 Sessions, t ≈ +8 auf SPY/QQQ/IWM). Nicht novel als
Auction-Echo. **Redesign nötig zur Staffelungs-Variante:** ZB ist ab 14:00 CT
verankert, ES/NQ erst 15:00 CT — das tägliche 14:00–15:00-CT-Fenster als
kalenderfestes Lead-Lag (nicht auktionsgebunden) ist die novel verbleibende Hypothese.
Advocatus-Einwand (Vorzeichen-Regime-Instabilität) verschärft sich dort. Neues
Feasibility-Dokument erforderlich, bevor Code geschrieben wird.

## ID63o — Post-Anker-Sparse-Fenster — ZURÜCKGESTELLT

**Grund:** Hängt am selben Settlement-Mechanismus wie ID67o (15:00-CT-Verankerung als
Startpunkt des Sparse-Fensters 15:00–15:15 CT). Sinnvolle Reihenfolge: erst ID67o
(validiert Settlement-Datenpipeline + Mapping), dann ID63o als Folgetest auf derselben
Infrastruktur. Earnings-Kontamination (15:00 CT = 16:00 ET = US-Earnings-Zeit) bleibt
dominanter Risikofaktor; print-freie Kohorte ist Pflicht-Umbau im Redesign.
