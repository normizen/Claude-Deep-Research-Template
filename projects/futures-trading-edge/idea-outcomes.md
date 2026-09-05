# Idea-Outcomes — futures-trading-edge

## Format
Jede Idee: Titel | Session | Advocatus-Urteil | Novelty-Check | Status | Nächste Schritte

---

## Ideen — Session 2026-04-15-futures-day-edge-strategic

### ID1: GEX-Feld-Topologie-Karte
**Session:** 2026-04-15-futures-day-edge-strategic
**Advocatus-Urteil:** ÜBERLEBT
**Novelty-Check:** NOVEL
**Kern:** Monopol/Dipol/Vortex-Klassifikation der GEX-Strike-Landschaft als struktureller Kontext-Layer
**Status:** Experiment E2 — nach GTZI-Validierung implementieren
**Daten:** Intraday Options-Chain (ThetaData $25/Mo oder IBKR TWS API)
**Alpha-Vorteil:** Strukturelle Feldkonfiguration sagt voraus wo Dealer-Zwang am stärksten wirkt — kein reines Level-Trading

### ID3: Strike-Gradient-Momentum (SGM)
**Session:** 2026-04-15-futures-day-edge-strategic
**Advocatus-Urteil:** ÜBERLEBT
**Novelty-Check:** NOVEL
**Kern:** GEX-Gradient zwischen benachbarten Strikes als Entry-Signal VOR Wall-Berührung
**Status:** Experiment E3 — nach Topologie-Karte implementieren
**Daten:** ThetaData Standard ($25/Mo) für Intraday-Updates nötig
**Alpha-Vorteil:** Früherer Entry durch mechanischen Dealer-Hedge-Druck — nicht reaktiv sondern antizipatorisch

### ID10: GEX-Topo-Zeitinvarianz-Signal (GTZI)
**Session:** 2026-04-15-futures-day-edge-strategic
**Advocatus-Urteil:** ÜBERLEBT
**Novelty-Check:** NOVEL
**Kern:** Persistente GEX-Konfigurationen über mehrere Tage als Regime-Filter für höhere Edge-Wahrscheinlichkeit
**Status:** Experiment E1 — ERSTER SCHRITT, kein neuer Daten-Feed nötig
**Daten:** EOD CBOE-Daten (bereits vorhanden)
**Alpha-Vorteil:** Regime-Filter der keine Daten-Subscription erfordert — 4-6 Tage Implementierung, sofort testbar

---

## Eliminierte Ideen (Advocatus Phase 4)

| Titel | Eliminierungsgrund |
|---|---|
| ID2: Anfänger-Protokoll | K2+K3+K4 — operationell nicht definierbar |
| ID4: Regime-Morphogenese | K2 — Metapher für bestehenden VPIN_Regime_Detector |
| ID5: Experten-Blindfleck-Index | K4 — Referenzmodell aller Experten-Strategien nicht baubar mit 10k |
| ID6: Preis-als-Morphogen | K2 — identisch mit bekannten GEX-Regime-Beschreibungen |
| ID7: Kognitive Kapazitäts-Arbitrage | K3+K5 — Event-Driven massiv arbitriert |
| ID8: Laterale Inhibitions-Stop | K2 — Metapher oder identisch mit Standard-Orderflow-Stop |
| ID9: Beginner's Random Walk | K1 — verstößt gegen Zero-Sum-Axiom (strukturell negativer EW) |


---

## Prüfphase 2026-08-30 bis 2026-09-02 — Ergebnisse zu den drei Überlebenden

Alle drei Ideen aus Session 2026-04-15 wurden geprüft oder als nicht prüfbar erkannt.
Datenbasis: QuantConnect NDXP, 2021–2026, 1.410 Handelstage, Gamma und Open Interest.
Vollständige Auswertung siehe `project.md`, Abschnitt STAND.

### ID10: GTZI — nicht eigenständig prüfbar

**Als Messgröße funktioniert es:** Persistenz des GEX-Profils auf absolutem Strike-Raster,
Streuung 0,26 bis 0,50 je nach Ära, 12 bis 33 % der Tagesübergänge unter Korrelation 0,5.
Es diskriminiert also.

**Aber es ist ein Filter ohne eigenen Gegenstand.** Der April-Entwurf sagt das selbst:
*„Liefert kein Entry-Signal, sondern eine binäre Aussage."* Ein Filter braucht ein
Wirtssignal, das er filtert. Da keines der geprüften Signale einen Effekt zeigte, gab es
nichts zu filtern.

**Zusätzlich:** Die Ereignisrate von GTZI-Brüchen liegt bei 0,08 je Tag. Für die nötigen
2.000 Ereignisse je Gruppe bräuchte es rund 50.000 Handelstage — etwa zweihundert Jahre.
Als eigenständiges Ereignis ist GTZI strukturell zu selten.

**Kritischer Nebenbefund:** Auf geglätteten Profilen ist GTZI **nutzlos** — Persistenz
1,000 in 87 von 87 Intraday-Vergleichen, Streuung 0,002. Nur auf Strike-Ebene
diskriminiert es. Der April-Entwurf hätte es auf ein normiertes Gitter interpoliert und
damit das Signal vollständig zerstört, ohne dass es aufgefallen wäre.

### ID1: GEX-Feld-Topologie-Karte — geprüft, negativ

Vorhersagen vorab festgeschrieben, 1.387 Tage, drei Typen sauber getrennt
(792 / 436 / 174). **2 von 4 ordinalen Vorhersagen getroffen** — unter der Null wären
1,67 zu erwarten. Effektstärken Cliff's d zwischen −0,004 und +0,051 gegen ein Kriterium
von 0,10.

Die beiden Trending-Vorhersagen für Vortex trafen richtungsmäßig, die Kreuzungs- und
Range-Vorhersagen nicht — letztere sogar in der Gegenrichtung.

**Der Klassifikator selbst ist brauchbar** (91 % gegen synthetische Wahrheit, trennt
echte Tage in drei besetzte Gruppen). Er trennt nur nicht nach etwas, das sich im
Kursverhalten niederschlägt.

### ID3: SGM — teilweise mitgeprüft, negativ

Als Wall-Kontakt operationalisiert und im Placebo-Test mitgeprüft: Ein GEX-Wall ist von
einem beliebigen Kursniveau gleichen Abstands nicht unterscheidbar (Cliff's d < 0,03 bei
1.430 gegen 1.459 Ereignissen).

**Einschränkung:** Das ist nicht die vollständige SGM-Idee. Der Entwurf beschreibt einen
Einstieg über den **Gradienten**, *bevor* der Kurs den Wall erreicht — nicht über die
Berührung. Eine eigene Operationalisierung über die Feldsteigung steht aus.

**Aber:** Auf Strike-Ebene ist die Gradienten-Variabilität hoch (Median 51), es gäbe also
etwas zu messen. Auf dem geglätteten Profil wäre der Gradient nahezu konstant und die
Idee gegenstandslos — dieselbe Falle wie bei GTZI.

### Was für eine Wiederaufnahme spräche

Nur eine Sache: **Das Fenster war mit ±0,8 % zu eng.** Die Walls, über die Praktiker
reden, liegen oft bei ±1 bis 3 %. Diese haben wir per Konstruktion nie gesehen. Das ist
die einzige identifizierte Schwäche, die eine erneute Messung rechtfertigen würde — und
sie wäre eine geänderte Zeile.

---

## Session 2026-09-03-pilot (Hermes-Pilotlauf)

8 Ideen generiert (ID20–ID27) aus Apoptose (12) × Glasübergang (22). Advocatus: 3 Überlebende. Novelty+Recherche: 2 testfähig, 1 Rechts-Tod.

### ID23: Steuer-Viskosität als Strategie-Selektor
**Advocatus:** ÜBERLEBT | **Novelty:** ÄHNLICHES EXISTIERT
**Status:** TOT — Rechtslage. BVerfG 31.07.2024 (2 BvL 7/22): 20.000-€-Grenze verfassungswidrig; JStG 2024 (i.K. 06.12.2024) strich § 20 Abs. 6 S. 5 EStG ersatzlos, rückwirkend für offene Fälle. Regelungsanker existiert nicht mehr.
**Vermächtnis:** Wichtige Info für den User — Termingeschäftsverluste sind wieder uneingeschränkt verrechenbar. Aktien-Verlusttopf bleibt (2 BvL 3/21, Entscheidung 2026/27).

### ID24: Instrumenten-Apoptose (ES/NQ/MES/MNQ-Eliminierungsturnier)
**Advocatus:** ÜBERLEBT | **Novelty:** NOVEL
**Status:** IN BETRIEB — K1 (Kosten/Range) run1 bestanden: ES 0,6 %, MES 2,0 %, NQ 0,2 %, MNQ 0,8 % (Schwelle 5 %). Kein Instrument eliminiert. Verbleibend: K2–K6 (Matrix monatlich).
**Deliverables:** experiment-designs.md (6 Todeskriterien, Schwellwerte, ~1 h/Monat), code/id24_range_monitor.py (getestet, Exit 0)
**Caveat (ehrlich dokumentiert):** MES↔ES, MNQ↔NQ fungibel → reales Turnier = 3 Entscheidungen.

### ID26: 30-Minuten-Zeitfenster-System
**Advocatus:** ÜBERLEBT (bedingt) | **Novelty:** NOVEL
**Status:** TESTED-REFUTED (run1, 2026-09-04)
**Ergebnis:** V1 Kostenquote-Asymmetrie 1,16× (vorregistriert >= 3×), Placebo-Perzentil 76 % (vorregistriert > 95 %) — nicht bestanden. V2 Momentum: Decay repliziert, 2022+ corr −0,045. Nach eigener Regel keine Neu-Suche (Datenfalle 5).
**Nebenbefund (bleibt als Messgröße):** Kostenquote-Tabelle ES: Open 1,5 % vs. Mittag 2,8 % — U-Form, Common Knowledge, kein Edge.
**Deliverables:** code/qc_id26_fenster_test.py (vorregistrierte Hypothesen, Placebo-Bootstrap 500 Fenster, Decay-Split 2022+, DST-Behandlung, Abstain-Zählung)
**Bedingung:** Lebt nur als Kosten-/Risiko-Mechanik oder mit eigenem vorregistriertem Fenster-Signal — naive Momentum-Variante hat dokumentierten Decay.

### Eliminierte (Advocatus)
| ID | Grund |
|---|---|
| ID20 Verglasungs-Diagnostik | A16: Gate ohne Wirtssignal |
| ID21 Apoptose-Kalender | Alter Wein: vorregistrierte Abbruchkriterien = Standard |
| ID22 Abstain-Quote | A16-Zirkularität: misst Rauschen ohne Brutto-Wirt |
| ID25 Unterkühltes Setup-Reservoir | A16+A10: Filter im Thermodynamik-Kostüm |
| ID27 Gegenfaktual-Buchhaltung | Umbenanntes Shadow-Trading |

---

## Session 2026-09-04-runde2 (Zwangsmechanik)

7 Ideen (ID28–ID34) aus Topologische Defekte (5) × Nischen-Konstruktion (10). Dual-Advocatus: Kimi (ID30+34) vs. Opus 5 (ID29+30) — Opus-Fund: Roll=Kalender-Spread kein Outright; ID34=Duplikat von ID29. Konsolidiert: Union mit Opus-Struktur.

### ID29: Prop-Close-Ernte
**Advocatus:** ÜBERLEBT (Opus; Kimi eliminierte — Coordinator folgt Union+Opus) | **Novelty:** NOVEL
**Größenordnungs-Gate:** BESTANDEN (knapp): konservativ 2,6–4,3 % des Close-Volumens; Apex-Frist 16:59 ET NACH Cash-Close → Prop-Anteil im dünnen ETH-Fenster 20–50 %.
**Status:** awaiting-manual-test — QC-Zelle qc_id29_prop_close_test.py bereit (TODO: ABSTAIN_DATES + MARGIN_HIKE_DATES befüllen)
**Abnahme:** 3 bps netto + 3 Attributionssignaturen; Pflicht-Falsifikator: Decay-Split (Effekt darf 2019–2021 NICHT existieren).

### ID30: Multi-Zwang-Dosis-Panel
**Advocatus:** ÜBERLEBT (beide, bedingt) | **Novelty:** NOVEL
**Status:** DEGRADIERT zu ID29-Kalender-Covariaten. Power-Rechnung: Dosis-≥2 nur ~30 Quartals-Opex-Freitage 2019–2026, JT+ Vola-Stratifizierung unmöglich. Opus-Fallback-Klausel exakt eingetreten.

### Eliminierte (Konsens beider Modelle)
| ID | Grund |
|---|---|
| ID28 Trailing-Drawdown-Karte | Kohorten-Kontur nicht beobachtbar (keine öffentlichen Positionsdaten) |
| ID31 Roll-Annihilation | Opus: Roll=Kalender-Spread, kein Outright-Kanal; ~40 Ereignisse |
| ID32 Margin-Hike | Selbst als nicht-einzeltestbar deklariert; Outright-Kanal unbelegt (nur Vola-Effekt) |
| ID33 Regelwerk-Stichtage | Kein beobachtbarer Treatment-Arm; Ereignisrate ~0 |
| ID34 Defekt-Replikat-Kohorte | Opus: formales Duplikat von ID29 (gleicher Test) |

---

## Session 2026-09-05-runde3 — GENERATOR-A/B: Opus 5 > Kimi (erste Runde Dual-Generator)

15 Ideen (8 Kimi-Feld ID40k–54k, 7 Opus-Feld ID41o–53o) aus Metamaterialien (4) × Bet-Hedging (11). Kreuz-Matrix-Advocatus.

**Konsens-Überlebende (2/2 Advocati):** ID41o, ID52k
**Union (Coordinator):** ID41o, ID52k, ID43o, ID53o (letztere 2 nur Kimi-Adv, aber mit produktivem Verwender ID41o). Geparkt als Module: ID45o, ID47o.

**Evidence Log:** Opus-Feld-Überlebensrate 57% (Kimi-Adv) / 29% (Opus-Adv) vs. Kimi-Feld 25%/25%. Kein Eigenfeld-Bias (Opus-Adv härter gegen eigenes Feld). → Generator-Override zu Opus 5 evaluieren.

### Überlebende → Phase 5/6
- **ID41o:** 0DTE-Close-Gamma-Reversions-Panel (A23, ~1.000 Replikate/Jahr über 4 Instrumente)
- **ID52k:** [Kimi-Feld, Konsens]
- **ID43o:** Settlement-Echo als Array-Dispersions-Kovariate (A22)
- **ID53o:** Flip-Kohärenz-Test (empirische Prüfung A25-Unabhängigkeit)
