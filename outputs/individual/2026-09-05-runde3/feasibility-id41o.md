# Feasibility — ID41o: 0DTE-Close-Gamma-Reversions-Panel

**Datum:** 2026-09-05 | **Runde:** 3 | **Rolle:** Deep Researcher
**Idee:** Konditionierte Reversion am Ende des täglichen 0DTE-Gamma-Zwangs über ES+NQ+GC+ZB (~1.000 Replikate/Jahr). Messgröße: Rendite 15:45→16:00 ET (Zwangsphase) vs. 16:00→16:30 ETH (Reversionsphase), identisch kodiert über 4 Instrumente.

---

## Gate 1 — GRÖSSENORDNUNG/KANAL: Trägt der Zwang die Reversion nach Kosten?

**Ehrliche Antwort: grenzwertig — der Median-Zwang ist kleiner als die Idee annimmt, der Effekt lebt in den oberen Quantilen.**

Belegte Größenordnungen (Recherche):

| Quelle | Befund | Implikation für ID41o |
|---|---|---|
| Cboe (2023, "Much Ado About 0DTEs") | MM-Net-Gamma 0DTE SPX: Median 15:30 ET nur **+$173mm** pro 1%, IQR **−$1,1bn bis +$2,4bn**; Whisker −$5bn/+$7,7bn = 1,3–1,9% des täglichen ES-Notionalvolumens (~$400bn) | Median-Tag: Zwang ≈ 0,04–0,17% der Tagesliquidität → **kein tragbarer Flow**. Nur ~25% der Tage (oberes Quartil, \|GEX\| > ~$1–2bn/1%) haben potenziell marktbewegenden Zwang |
| Dim/Eraker/Vilkov 2023 (SSRN 4692190) | MM-Net-Gamma im Schnitt **positiv**; positives Gamma **verstärkt intraday Reversion** (negatives verstärkt Momentum) | Mechanik bestätigt: Reversion ist der konditionierte Basisfall — aber nur intraday SPX getestet |
| SSRN 4881008 (2024) | 0DTE-Hedging **dämpft** Index-Vol um 60–90 bp annualisiert; Hedging-Flow läuft über Index-Futures | Der Reversions-Kanal existiert und läuft über ES — gut für den Kanal, schlecht für die Größe (dämpfend, nicht explosiv) |
| ID26-Run (eigene Daten, ES 2019–2026) | 15:30–16:00-Fenster: Median-Range $675 (≈13,5 Pkt ES); Kostenquote 2,0%; Erst-30→Letzt-30-Min-Korrelation 2022+ = **−0,045** (Hit-Rate 48,7%) | Es existiert eine schwache Close-Reversion im ES, aber corr −0,04 ist weit unter der Cliff's-d-≥0,10-Hürde und wird von 2,0% Kostenquote nicht getragen, wenn man das volle Fenster handelt |

**Kosten-Rechnung (MES/MNQ/MGC/Micro-ZB):** RT-Kosten ≈ 1 Tick + Gebühren ≈ $3–4 pro MES-Kontrakt. Eine Reversion muss also ≥ 3–4 ES-Punkte ($30+ auf ES, 15%+ der Fenster-Range) einfangen, um break-even zu sein — das verlangt, dass der Trade **nur im oberen Gamma-Quartil** läuft (Abstain-Architektur ist nicht optional, sondern überlebensnotwendig).

**Urteil Gate 1: CONDITIONAL.** Der Median-Tag trägt nichts; der Effekt ist quantil-abhängig. ID41o ist nur als **konditionierter** Test (Gamma-Regime-Stratifizierung, wie in der Idee bereits angelegt) machbar — als unkonditioniertes Panel wäre es NO-GO.

## Gate 2 — EINPREISUNG: Was bleibt nach Dim/Eraker/Vilkov netto übrig?

- **Dim/Eraker/Vilkov (SSRN 4692190)** deckt ab: SPX, intraday, Zusammenhang MM-Gamma → Reversion/Momentum. **Nicht** abgedeckt: (a) das scharfe 16:00-Ende als Event-Fenster mit ETH/Overnight-Reversion, (b) Cross-Instrument (NQ, GC, ZB), (c) vorregistriertes Panel-Design mit Placebo-Uhrzeiten.
- **Cboe + SSRN 5113405 (Amaya/Vasquez et al. 2025)** nutzen proprietäre MM-Positionsdaten — Institutionelle sehen den Flow direkt. Das heißt: der **grobe** intraday SPX-Reversionsanteil ist bepreist (ID26 bestätigt: corr −0,045, klein).
- **Netto-Raum:** (i) ETH-Fenster 16:00→16:30 ist dünner besetzt (Prop-Firm-Flat-Flow ID29 überlagert — Risiko UND Gelegenheit), (ii) Overnight-Variante (16:00→Folgetag-Open) ist im 0DTE-Kontext kaum getestet — 0DTE-Gamma ist nach 16:00 tot, also ist Overnight-Reversion *kein* Gamma-Effekt mehr, sondern generischer Close-Effekt; die Idee muss das sauber trennen (Gate 3), sonst misst sie das eingepreiste Overnight-Reversal. (iii) GC/ZB-Beine sind unbesetzt, aber aus Gate-4-Gründen fraglich.
- **Ehrlich:** Der Retail-bekannte "buy-the-close-reversal"-Effekt ist der eingepreiste Kern; der Novelty-Check-Urteil NOVEL gilt für das **Design** (Panel + vorregistrierte Signaturen), nicht für eine neue ökonomische Kraft. Erwarteter Effekt nach Kosten: klein (Cliff's d 0,05–0,15 optimistisch).

**Urteil Gate 2: NETTO-Raum existiert, aber schmal** — hauptsächlich im ETH-Fenster und in der Regime-Konditionierung, nicht in der Overnight-Variante.

## Gate 3 — DESIGN: Trennung 0DTE-Gamma-Ende vs. generischer Close-Effekt

Vorregistriertes Test-Design (Methodik aus ID26-Run: Placebo, Cliff's d, Decay-Split):

1. **Signal:** Reversion = −sign(R_15:45→16:00) × R_16:00→16:30, pro Instrument, pro Tag.
2. **Placebo A (Uhrzeit):** gleiche Tage, 500 zufällige 15-Min-Fenster-Paare → Perzentil-Test (Konvention: >95%).
3. **Placebo B (Mechanismus-Trennung):** seit Mai 2022 hat SPX **tägliche** Verfälle (Mo–Fr); davor nur Mo/Mi/Fr. Der sauberste Placebo ist daher **Pre-2022 Nicht-Verfallstage (Di/Do) gleiche Uhrzeit** — 16:00 ohne 0DTE-Verfall. Zusätzlich Kontrollinstrument-Logik: wenn die Reversion in ES/NQ an Verfallstagen signifikant stärker ist als an Nicht-Verfallstagen, ist der Gamma-Kanal identifiziert; wenn nicht, ist es der generische Close-Effekt (eingepreist, REFUTED).
4. **Dosis-Response:** Abstand Spot↔Gamma-Flip-Level (OI-Proxy aus CME/Cboe-Daten) als Dosis; vorregistriert: Reversion-Stärke steigt mit Nähe zum Flip und mit \|GEX\|-Quantil.
5. **Decay-Split:** 2022+ als Hauptsample (0DTE-Struktur jung, tägliche Verfälle), 2019–2021 als Kontrolle; vorregistriert: Effekt 2022+ > 2019–21, sonst ist es kein 0DTE-Phänomen.
6. **Abstain:** Feiertage, halbe Tage, FOMC-CPI-Tage-Flag; Multiplizität: Holm über 4 Instrumente.
7. **Annahme-Hürde:** Cliff's d ≥ 0,10 auf dem Panel-Mittel UND >95%-Placebo-Perzentil — wie ID26, wo V1 an genau diesen Hürden scheiterte (d=0,159, Perzentil 76% → NICHT bestanden). ID41o muss dieselbe Konvention überleben.

**Urteil Gate 3: DESIGN IST MACHBAR** — das Di/Do-Pre-2022-Placebo plus Dosis-Response trennt den Gamma-Kanal sauberer als reine Uhrzeit-Placebos.

## Gate 4 — CROSS-INSTRUMENT: Sind GC und ZB echte Replikate?

**Ehrliche Antwort: nein, nicht homogen.**

- **ES/NQ:** SPX- + NDX-0DTE-Optionen verfallen täglich 16:00 ET, Dealers hedgen in ES/NQ-Futures → scharfer, identischer Endpunkt. ✓ echte Replikate.
- **GC:** COMEX-Gold-Optionen haben **wöchentliche/monatliche** Verfälle mit Settlement ~13:30 ET, kein tägliches 0DTE-Ökosystem in relevanter Größe. Es gibt kein dokumentiertes tägliches GC-Gamma-Ende um 16:00. ✗ kein homologer Zwang — höchstens Risiko-Übertrag (Korrelation zu ES im Close).
- **ZB:** Treasury-Optionen auf ZB verfallen wöchentlich/monatlich (CBOT), Settlement-Fenster ≠ 16:00 ET scharf; kein tägliches 0DTE-Analogon. ✗.

**Konsequenz:** Das Vierer-Panel ist **kein** 4-Replikat-Design, sondern ein 2-Kerne (ES/NQ, korreliert — ID53o testet genau das) + 2-Satelliten-Design. Effektive unabhängige Replikate: realistisch **~500/Jahr (ES+NQ, korrigiert eher ~350–400)**, nicht 1.000. GC/ZB bleiben als **Kontrollbeine** wertvoll (wie in ID49o konzipiert): eine Reversion, die in GC/ZB genauso stark auftritt, ist globaler Close-Flow, kein Gamma-Effekt — sie sind die *In-Sample-Falsifikatoren*, nicht die Replikate.

**Urteil Gate 4: PANEL-NEUSTRUKTURIERUNG NÖTIG** — ES/NQ als Test-Beine, GC/ZB als Kontrollbeine; Replikatzahl-Claim von 1.000 auf ~400 ehrlich nach unten korrigieren.

---

## Test-Design (verdichtet)

| Komponente | Spezifikation |
|---|---|
| Daten | QC-Minutenbars ES/NQ/GC/ZB, 2019–2026, continuous backadjusted (ID26-Konvention) |
| Fenster | Zwang 15:45→16:00, Reversion 16:00→16:30 ETH (+ explorativ Overnight) |
| Test-Beine | ES, NQ (Panel-Mittel) |
| Kontroll-Beine | GC, ZB (Falsifikator: gleiche Stärke → REFUTED als Gamma-Effekt) |
| Placebo | A: Zufalls-Uhrzeiten (n=500, >95%); B: Pre-2022 Di/Do (kein Verfall) |
| Dosis | \|GEX\|-Quantil (OI-Proxy), Flip-Level-Nähe |
| Decay-Split | 2022+ Haupt / 2019–21 Kontrolle |
| Kosten | RT 1 Tick + Gebühren pro Micro; nur \|GEX\|-Top-Quartil handeln |
| Hürden | Cliff's d ≥ 0,10 Panel-Mittel, Placebo >95%, Holm über Beine, Abstain-Regeln vorregistriert |
| n | ~400–500 effektive Replikate/Jahr (korrigiert), davon ~125 im Top-Gamma-Quartil |

## GO / NO-GO

**GO — bedingt, mit drei verbindlichen Umbauten:** (1) Panel von 4 Replikaten auf 2 Test-Beine + 2 Kontrollbeine umstrukturieren (GC/ZB haben keinen homologen 16:00-Gamma-Zwang; der 1.000-Replikate-Claim ist nicht haltbar). (2) Handel nur im oberen \|GEX\|-Quartil — Cboe-Daten zeigen, dass der Median-0DTE-Net-Gamma-Zwang (0,04–0,17% der Tagesliquidität) eine Reversion nach 1-Tick-Kosten nicht trägt; unkonditioniert wäre das NO-GO. (3) Overnight-Variante aus dem Kern-Hypothesenset streichen — nach 16:00 ist das Gamma tot; was dort revertiert, ist der eingepreiste generische Close-Effekt.

**Urteil: CONDITIONAL GO.** ID41o überlebt als konditionierter, regime-stratifizierter ES/NQ-Test mit GC/ZB als eingebautem Falsifikator — das ist immer noch das stärkste Design der Runde, aber nur halb so groß wie behauptet, und sein Erfolg hängt am noch unbewiesenen oberen Gamma-Quantil, nicht am Median-Tag.
