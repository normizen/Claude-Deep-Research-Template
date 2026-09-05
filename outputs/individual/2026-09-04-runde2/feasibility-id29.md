# Feasibility ID29 — „Prop-Close-Ernte"

**Idee:** Konditionierte Close→Overnight-Reversion (Tagesrichtung × Trendcharakter der letzten 30 RTH-Min → erste 60 Overnight-Min, ES/NQ). Kausalnarrativ: Prop-Firm-Eval/Funded-Flat-Zwang (alle Positionen müssen vor Tagesende glattgestellt werden — Apex: 4:59 PM ET, Auto-Liquidation als Fail-safe; Topstep analog).
**Status der Advocati:** OPUS = ÜBERLEBT (einzige unbedingte Überlebende der Runde), KIMI = ELIMINIERT als eigenständige Idee (Einpreisung + nicht trennbarer Konfunder). Diese Feasibility beantwortet die drei Pflicht-Gates beider Gutachten.
**Methodik-Referenz:** ID26-Run (2019–2026, 1.978 Handelstage, 71 Abstain-Tage gezählt, Placebo-Perzentile n=500, Cliff's d, Decay-Split 2019–2021 vs. 2022+). Genau diese Schablone ist für ID29 wiederverwendbar.

---

## GATE 1 — Größenordnungs-Rechnung (vorregistriertes Go/No-Go)

### Öffentliche Eingangsgrößen (recherchiert, mit Quellenlage)

| Größe | Wert | Quelle / Qualität |
|---|---|---|
| Pass-Rate Evaluations (Topstep 2025) | 16,8 % der Combines; 51,8 % der Personen mind. 1× funded; 33,3 % der Funded mit Payout; 0,71 % XFA→Live | Topstep-Eigenangabe (Risk Disclosure), via propfirmscompare/proptradingvibes — unauditiert, aber firmenpubliziert |
| Funded-Trader gesamt (Branche) | ~2,1 Mio (2026), ~120–150 aktive Firmen, Top-5 = 62 % | Track360-Schätzung, unauditiert; Chart Whisperer nennt „2 Mio+ über 2.000+ Firmen" (inkonsistente Firmenzahl → Vorsicht) |
| Futures-relevante Kohorte | Apex 100–180k funded (größte Futures-Firma), Topstep 50–150k, dazu Tradeify/MFFU/Bulenox/Earn2Trade u. a. | kenmacro/Track360-Schätzungen. **Wichtig:** Der Großteil der 2,1 Mio ist FX/CFD (FTMO, FundedNext, 5%ers) und handelt NICHT ES/NQ am CME-Close — für ID29 zählt nur die Futures-Kohorte |
| Flat-Zwang | Apex: flat bis 4:59 PM ET, Auto-Flatten als Fail-safe; Topstep analog (EOD-Trailing, kein Overnight) | Firmen-Regelwerke, öffentlich |
| Kontraktlimits | 25K: 2–3 Mini / 15–25 Micro; 50K: 5–10 Mini / 25–50 Micro; Apex: Halb-Positionsregel pre-lock; realistische Bestandsgröße 1–5 MES/MNQ pro Konto (Risikobudget 1–2 % des Drawdowns) | bestprops/damnpropfirms/proptradingvibes — konsistent |
| ES-Volumen | ~1,3–1,5 Mio Kontrakte/Tag (65d-avg 1,34M, MarketWatch); letzte 30 RTH-Min ≈ 10–15 % → **~130–220k ES** im Zielfenster | CME/MarketWatch + übliche Intraday-Volumenverteilung |

### Szenario-Rechnung (ES-Äquivalente; 1 ES = 10 MES)

| Szenario | Aktive Futures-Konten | Anteil mit Position 15:30–16:59 ET | Ø ES-Äq/Konto | **Brutto-Flat-Flow** | Anteil am Close-Volumen (130–220k) |
|---|---|---|---|---|---|
| Konservativ | 150.000 | 25 % | 0,15 (1,5 MES) | **5.625 ES-Äq** | **2,6–4,3 %** |
| Basis | 300.000 | 40 % | 0,25 | **30.000 ES-Äq** | **13,6–23,1 %** |
| Großzügig | 600.000 | 60 % | 0,50 | **180.000 ES-Äq** | 82–138 % — **intern falsifiziert** |

**Obere Schranke durch Volumen-Konsistenz:** Das großzügige Szenario ist unmöglich — ein täglicher Flat-Flow dieser Größe würde das Close-Fenster-Volumen dominieren und als auffällige tägliche Volumenspitze sichtbar sein. Die plausible Bandbreite ist damit konservativ bis Basis: **Brutto ~5,6k–30k ES-Äq ≈ 2,6–23 % des Close-Fenster-Volumens.**

**Netto-Imbalance (die eigentlich preiswirksame Größe):** Die Kohorte ist heterogen gerichtet (Long UND Short); nur an Trendtagen kippt die Netto-Richtung einseitig gegen die Tagesbewegung (Gewinner der Tagesrichtung glattgestellt + Verlierer gestoppt → Netto-Flow GEGEN die Tagesbewegung). Annahme 60/40-Richtungsasymmetrie an Trendtagen ⇒ Netto = 40 % × Brutto:

| Szenario | Netto-Flat-Flow | Anteil Close-Vol | In Einheiten der Boyarchenko-Referenz (1 SD Close-Imbalance ≈ 1.500 ES → ~1,2–2,6 bps Overnight-Reaktion) |
|---|---|---|---|
| Konservativ | ~2.250 ES-Äq | 1,0–1,7 % | ~1,5 SD → **~2–4 bps konditioniert** |
| Basis | ~12.000 ES-Äq | 5,5–9,2 % | ~8 SD → 10–20 bps (oben gedeckelt: ein so großer Effekt wäre längst arbitriert → realistisch eher 4–8 bps) |

**Ergebnis Gate 1:** Der geschätzte Prop-Anteil liegt im plausiblen Band **ÜBER der Nachweisgrenze von 1–2 %** (brutto klar, netto-konditioniert im konservativen Szenario knapp darüber, im Basis-Szenario deutlich darüber). Damit ist KIMIs Promille-Einwand („Flow-Anteile im Promille-Bereich") durch die Arithmetik **nicht bestätigt**: Selbst 150k Konten × 25 % × 1,5 MES ergeben 2,6–4,3 % des Close-Volumens. Der Engpass ist nicht die Größenordnung, sondern (a) die **Richtungs-Heterogenität** der Kohorte (unbekannt, nicht öffentlich) und (b) die **zeitliche Konzentration**: Da die Frist 4:59 PM ET ist — also NACH dem Cash-Close 16:00 ET —, fällt der Großteil des Zwangs-Flows in das ETH-Fenster 16:00–16:59 ET, wo das Volumen dünn ist (~1–2 % des Tages). Dort kann der Prop-Anteil 20–50 % des Fenster-Volumens erreichen — das ist die schärfste beobachtbare Signatur. **Gate 1: bestanden (knapp, mit dokumentierter Unsicherheit über die Netto-Richtung).**

---

## GATE 2 — Einpreisungs-Abgrenzung

**Bereits bepreist (harte Faktenlage):**
- Overnight-vs.-Intraday-Dekomposition: Cliff/Cooper/Gulen (2008), Kelly/Clark (2011), Lou/Polk/Skouras (2019, „Tug of War" — Retail früh vs. Institutionell spät, exakt das Muster „später Flow reversiert overnight").
- Boyarchenko/Larsen/Whelan (RFS 2023, „The Overnight Drift"): Close-Order-Imbalance → Overnight-Reversion, **asymmetrisch**: Selloffs → robuste positive Reversion; Rallyes → nur schwache. 1 SD Close-Imbalance (6,55 % RSV) → ~1,15–2,6 bps. **Die Tagesrichtungs-Konditionierung ist damit in ihrer UNBEDINGT-asymmetrischen Form bereits akademisch besetzt.**
- Kommerziell bepreist: NightShares-ETFs (seit Juni 2022) ernten explizit den Overnight-Drift; die Prop-Firm-Erklärung des Close-Musters ist in Trading-Communities Common Knowledge.

**Netto-Raum der bedingten Variante (was NICHT bepreist ist):**
1. **Reversion NACH TREND-UP-TAGEN:** Boyarchenko findet Reversionen nach Rallyes „much more modest". Das Prop-Flat-Narrativ sagt das Gegenteil voraus: An starken Trend-Up-Tagen sitzt die Kohorte netto long (Momentum-Follower im Plus) und MUSS in den Close verkaufen → Overnight-Reversion nach UNTEN, stärker als die bekannte Asymmetrie impliziert. Das ist eine falsifizierbare Abweichung von der RFS-Referenz, kein Re-Run.
2. **Trendcharakter-Konditionierung (≠ Tagesrichtung):** „Letzte 30 Min verstärken die Tagesbewegung" (Trendtag) vs. „letzte 30 Min drehen gegen" ist eine zweite, von der Literatur nicht besetzte Achse.
3. **Zeitliche Signatur 16:00–16:59 ET (ETH):** Die Literatur misst Close-Imbalance am Cash-Close; der Prop-Flat-Zwang (Frist 16:59 ET) wirkt NACH dem Cash-Close im dünnen ETH-Fenster. Ein bedingter Drift 16:30–16:59 ET mit Reversion 18:00–19:00 ET ist in keiner der genannten Arbeiten separat identifiziert.

**Ergebnis Gate 2:** Der unbedingte Effekt ist tot (bepreist). Der bedingte Effekt (Trend-Up-Reversion + ETH-Fenster-Signatur) hat einen echten, kleinen Netto-Raum — geschätzt 2–8 bps konditioniert, gegen RT-Kosten von ~2–3 % der Fenster-Range (ID26: 2,0 % im 15:30–16:00-Fenster). **Zum Break-even braucht der Test ≥ ~3 bps konditionierten Effekt.** Knappe, aber nicht hoffnungslose Kosten-Effekt-Relation.

---

## GATE 3 — Attributions-Design (Prop-Flat vs. generischer Overnight-Effekt)

Drei ineinandergreifende Trennmechanismen (alle mit QC-Minutenbars + ID26-Codebasis realisierbar, ~250 Ereignisse/Jahr, rückblickend 2019+ sofort):

1. **ETH-Zeit-Signatur (Haupt-Attribution):** Der Prop-Flat-Zwang hat eine harte Frist 16:59 ET und wirkt daher konzentriert in 16:00–16:59 ET; institutioneller MOC/Rebalancing-Flow wirkt VOR/AM Cash-Close 16:00 ET. Vorregistrierte Doppelprognose: (a) konditionierter Drift 16:30–16:59 ET in Richtung „gegen Tagestrend" stärker als der Drift 15:30–16:00 ET relativ zu dessen Volumen; (b) Reversion 18:00–19:00 ET (Globex-Reopen) proportional zum ETH-Drift, nicht zum RTH-Close-Drift. Placebo-Fenster: 14:30–15:00 ET (gleiche Tagesphase, keine Frist) und 15:00–15:30 ET.
2. **Dosis-Varianz Wochentag/Verfall:** Bei echtem Flat-Zwang muss der Effekt freitags (Wochenend-Flat ist bei manchen Firmen strikter / Risiko-Aversion über Wochenende) und an Verfallstagen (Roll-Flat-Zwang am Front-Kontrakt) stärker ausfallen; ein generischer Overnight-Effekt prognostiziert diese Ordnung nicht. Vorregistrierte Ordnung: Verfall-Freitag > Freitag > Verfall-Wochentag > normaler Wochentag.
3. **Statistik-Rahmen (ID26-kompatibel):** Cliff's d ≥ 0,1 als Effektgrößen-Schwelle; Placebo-Perzentil n=500 > 95 %; Abstain-Tage (FOMC/CPI/NFP als Informations-Konfunder) ausgeschlossen UND gezählt; Decay-Split 2019–2021 vs. 2022+ (der Prop-Boom ist post-2021 — bei echter Prop-Kausalität muss der Effekt 2022+ STÄRKER sein als 2019–2021; ein abklingender oder konstanter Effekt falsifiziert die Prop-Attribution und bestätigt KIMIs Einwand). **Dieser Decay-Split ist die schärfste einzelne Falsifikation: Der Träger (Prop-Kohorte) existiert in relevanter Größe erst seit ~2021–2022.**

**Verbleibende ehrliche Lücke:** Die Netto-Richtungs-Heterogenität der Kohorte ist nicht öffentlich beobachtbar; das Design ersetzt die fehlende Kohorten-Beobachtung durch die doppelte konditionierte Prognose (Zeit-Fenster × Dosis × Decay). Drei unabhängige Signaturen, die alle gleichzeitig in die Prop-Richtung zeigen müssen — das ist stärker als ID26s einzelne Fenster-Hypothese, aber schwächer als direkte Flow-Daten.

---

## Test-Design-Skizze (vorregistrierbar)

- **Instrumente:** ES (primär), NQ (Replikation), MES/MNQ als Flow-Näherung (Sekundäranalyse).
- **Fenster:** Signal = Return 15:30–16:00 ET UND 16:00–16:59 ET, konditioniert auf Tagesrichtung (RTH-Return) × Trendcharakter (Verhältnis letzte-30-Min-Return zu RTH-Return). Ziel = Return 18:00–19:00 ET (erste 60 Min nach Globex-Reopen; alternative Spezifikation: erste 60 Min nach 17:00 ET für durchgehende Sessions).
- **Vorregistrierte Richtung:** Nach Trend-Up-Tagen mit Close-Verstärkung: negativer Overnight-Return im Ziel-Fenster; nach Trend-Down: positiver (Boyarchenko-konsistent, aber stärker als deren unbedingte Asymmetrie).
- **Kosten:** RT $13,50/ES (ID26-Konvention); Break-even ≥ ~3 bps.
- **Go-Kriterien:** Cliff's d ≥ 0,1 im konditionierten Subsample; Placebo-Perzentil > 95 %; Dosis-Ordnung (Jonckheere-Terpstra über Wochentag/Verfall) p < 0,05; **Decay-Split 2022+ ≥ 2019–2021 (Pflicht, umgekehrte Richtung = Attribution gescheitert)**; Netto-Effekt ≥ 3 bps nach Kosten.

---

## Urteil

Die Größenordnungs-Rechnung widerlegt den Promille-Einwand: Selbst konservative Annahmen (150k Futures-Konten, 25 % im Fenster, 1,5 MES/Konto) ergeben 2,6–4,3 % des Close-Fenster-Volumens brutto und ~1–1,7 % netto-konditioniert — an der Nachweisgrenze, im Basis-Szenario deutlich darüber, wobei die Konzentration des Zwangs ins ETH-Fenster 16:00–16:59 ET (Frist 16:59 ET, dünnes Volumen) die Messbarkeit zusätzlich verbessert. Einpreisung trifft nur den unbedingten Effekt; der konditionierte Netto-Raum (Trend-Up-Reversion stärker als Boyarchenkos Asymmetrie + ETH-Zeit-Signatur) ist real, aber klein (~3 bps Break-even). Die Attribution ist ohne Kohorten-Daten nur indirekt möglich, aber das Drei-Signaturen-Design (Zeit × Dosis × Decay-Split 2022+, wo der Prop-Träger erst existiert) ist falsifizierbar und mit der ID26-Schablone in ~1–2 Tagen umsetzbar.

**GO — bedingt.** Bedingungen: (1) Vorregistrierung VOR erstem Datenkontakt inkl. Break-even-Schwelle ≥ 3 bps und Decay-Split als Pflicht-Falsifikator; (2) kein Ernten bei bestandenem Effekt ohne bestandene Attribution (sonst exakt die GEX-Wall-Falle: generischen Overnight-Effekt mit Prop-Etikett ernten und gegen NightShares & Co. konkurrieren); (3) ID30-Kalender-Labels (Verfall/Wochentag) werden von Anfang an mitgeführt, da sie als Dosis-Varianz Teil des Attributions-Tests sind.
