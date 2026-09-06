# Feasibility: ID67o — Batch-minus-Marginal-Residual (BMR)

**Datum:** 2026-09-06 | **Novelty:** PARTIALLY (Komponenten bekannt, Formalisierung neu — siehe novelty-check-id67o.md) | **Pre-OPUS-Urteil:** ÜBERLEBT, stärkste Idee beider Felder

---

## Verifizierte Settlement-Fakten (Primärquelle)

- **ES/NQ:** CME-Settlement = VWAP aller Globex-Trades im Lead Month, **14:59:30–15:00:00 CT** (30 s), gerundet auf **nearest 0,25 Indexpunkt**. Fallback: Bid/Ask-Midpoint desselben Fensters. (CME Client Systems Wiki, E-Mini S&P 500 Futures Settlement Procedures)
- **GC:** COMEX-Settlement-Fenster 12:30–12:30:xx CT (eigenes Fenster, eigene Rundung).
- **ZB:** CBOT-Settlement ~13:59–14:00 CT, Rundung auf **1/64** (nicht 1/32 wie oft behauptet — für den Test nur als Falsifikator relevant, dort muss die eigene Rundungsregel hinterlegt werden).
- **QC/AlgoSeek Daily-Bars:** aggregierte Trades, Tagesgrenze **00:00–00:00 ET** — der Daily-Close ist der **letzte Trade des Kalendertags, NICHT das offizielle CME-Settlement**. Es gibt in QC keinen nativen offiziellen Settlement-Preis.

---

## Gate 1 — RUNDUNGSFALLE: Design-Entscheidung

**Problem (zweigeteilt):**
(a) Settlement ist auf 0,25 gerundet; ein Pseudo-Anker-Placebo aus Minutenbars ist es nicht → ein Positiv wäre von der Rundungsregel nicht unterscheidbar.
(b) Der 30-Sekunden-VWAP des Settlements ist aus Minutenbars **nicht berechenbar** → Treatment und Kontrolle können nie mit demselben Schätzer gemessen werden.

**Entscheidung 1a (Datenquelle Treatment):** Der Settlement-Preis kommt **nicht aus QC**. Er wird aus der **öffentlichen, kostenlosen CME-Settlements-Seite** (cmegroup.com/.../e-mini-sandp500.settlements.html, CSV-historisch verfügbar) pro Kontrakt und Tag gezogen und per Datum+Lead-Month auf den QC-Continuous gemappt. Das ist der einzige Weg, den echten gerundeten Batch-Preis zu bekommen, und er ist kostenlos — der A29-Anspruch („Zahlen sind öffentlich, niemand benutzt sie") bleibt intakt. Vorab-Validierung im Code: Stichprobe von 20 Tagen, CME-Settlement gegen QC-Daily-Close — die Differenz muss ≠ 0 sein und auf dem 0,25-Grid liegen (Datenfalle: falls QC-Close = Settlement geliefert würde, wäre das Feld schon gelöscht und der Test sinnlos).

**Entscheidung 1b (Schätzer-Asymmetrie):** Der marginale Preis ist **Close des Minutenbars 14:59 CT** (deckt 14:59:00–14:59:59 ab, letzter voller Bar vor dem Settlement-Fensterende) aus QC-Minutenbars. Treatment und Placebo werden dadurch symmetrisch gemacht, dass **das Placebo identisch konstruiert und identisch gerundet** wird:

- **Placebo (Pseudo-Anker):** VWAP-Proxy aus den Trades des Minutenbars 13:59 CT (Bar-typical-price (H+L+C)/3 bzw. volumengewichteter Bar-Mittelwert, was QC hergibt) am selben Tag, **danach auf nearest 0,25 gerundet** — exakt dieselbe Rundungsoperation wie das echte Settlement. Damit trägt das Placebo das gesamte Rundungsrauschen des Treatments.
- BMR = Settlement_CME − Close(Bar 14:59). Placebo-BMR = round₀.₂₅(TypicalPrice(Bar 13:59)) − Close(Bar 13:59). Beide Größen leben auf demselben 0,25-Grid, beide Differenzen enthalten denselben Rundungs-Bias.
- **Zusätzlicher Rundungs-Guard (vorregistriert):** Tage mit |ungerundetes Placebo − Close| < 0,125 (halbes Tick) werden als eigene Kohorte geflaggt, nicht gelöscht; der Haupteffekt muss auch in der Kohorte |d| ≥ 0,25 (mindestens ein volles Rundungs-Quantum) bestehen.

**Restrisiko, offengelegt:** Der 30-s-VWAP ≠ Bar-Typical-Price. Die Schätzer-Differenz ist aber **vorzeichenneutral** (sie streut den Placebo-BMR um 0, nicht systematisch), und die identische Rundung macht den gefährlichen Teil (diskretes Grid) symmetrisch. Ein verbleibendes Positiv wäre damit nicht mehr durch „CME rundet, Minutenbar nicht" erklärbar.

## Gate 2 — GUARD-ÜBERLEBENSRATE: Design-Entscheidung

**Problem:** Der ≥ 0,5-ES-Punkt-Guard schneidet den Großteil der Verteilung ab; Draft-Schätzung 40–70 % Überlebensrate ist für ES vermutlich um Faktor ~2 zu optimistisch.

**Entscheidung:** **Pflicht-Vorab-Schritt im QC-Code, vor jedem Inferenztest.** Aus den QC-Minutenbars + CME-Settlements selbst, über die volle Sample-Periode (2019–2026, analog ID26-Methodik):

1. Verteilung von |BMR_roh| = |Settlement − Close(14:59-Bar)| in ES-Punkten pro Instrument (ES, NQ) tabellieren: Anteil Tage mit |BMR| ≥ 0,5 / ≥ 1,0 / ≥ 2,0 Punkte.
2. **Vorregistrierte Abbruchregel:** Überlebensrate bei Guard 0,5 < **15 %** → Guard auf 0,25 (ein Rundungs-Quantum) senken und n_Replikate neu bewerten; Überlebensrate auch dort < 15 % → **NO-GO ohne Haupttest** (Power unmöglich). Erwartung realistisch: ES 15–35 % bei 0,5, NQ höher (größere Punkte/Vola).
3. Guard ist **instrument-spezifisch** (NQ: 1 Punkt Guard start), nicht global — NQ-BMR in NQ-Punkten, ES-BMR in ES-Punkten, keine Mischung.
4. Ausgabe der Replikatzahl pro Jahr (Ziel ≥ 100/Jahr nach Guard; Draft-Versprechen ~250/Jahr nur ohne Guard) in den Test-Header — gleiches Format wie ID26 run1.txt (Handelstage, Abstain-Tage gezählt und berichtet).

## Gate 3 — KONTROLLE: Design-Entscheidung

**Problem:** Hauptkontrolle auf Vorzeichen-Permutation + Monatsend-Dosis + Vier-Instrumenten-Falsifikator verlagern; ZB rundet anders als ES.

**Entscheidung — dreistufige Kontrollarchitektur:**

1. **Haupt-Inferenz: 500 Vorzeichen-Permutationen** (ID26-Standard: Placebo-Perzentil > 95 % gefordert). Permutiert wird das BMR-Vorzeichen über Tage **innerhalb von Monatsblöcken** (blockweise, um die Monatsend-Dosis-Struktur nicht selbst wegzupermutieren). Statistik: durchschnittlicher Folgetag-RTH-Erststunden-Return konditional auf sign(BMR), gegen die Permutationsnull.
2. **Monatsend-Dosis-Monotonie (falsifizierbar, kurvenanpassungsfest):** ES/NQ-Monatsend-Settlement IST per Regel das 15:00-CT-Fixing → vorregistrierte Vorhersage: Effektstärke monoton in {Monatsend-Tage > übrige Monatswoche-Tage > Rest}. Getestet als Jonckheere-Terpstra-Trend über die drei Ordinalstufen. Ein Kurvenfit kann keine kalenderfeste Regel-Monotonie erzeugen.
3. **Vier-Instrumenten-Falsifikator:** ES/NQ = Testinstrumente; GC = Placebo-Anker (12:30 CT, ZB-Sparse-Phase irrelevant — ein Effekt in GC = globales Risiko-Muster, kein BMR); ZB = **Rundungs-Falsifikator mit eigener Rundungsregel**: ZB-Settlement rundet auf 1/64, der Pseudo-Anker-Guard muss deshalb **1/64-Rundung** verwenden, nicht 0,25. Vorregistriert: der ES-Effekt darf in ZB **nicht** auf dem ES-Grid erscheinen; erscheint ein „Effekt" in ZB nur, wenn man fälschlich 0,25-Punkt-Rundung anwendet, ist das der Nachweis, dass die Rundungsfalle real war und der Guard korrekt funktioniert. Erscheint der volle Effekt in GC oder ZB auf eigenem Grid → Idee falsifiziert (generischer Settlement-Gap-Effekt, kein batch-minus-marginal-Mechanismus).

---

## Test-Design (komplett, ID26-Methodik-Format)

- **Daten:** QC-Minutenbars ES/NQ/GC/ZB continuous (backadjusted, mapping OPEN_INTEREST — ID26-Standard), 2019-01–2026-08; CME/CBOT/COMEX offizielle Settlements aus öffentlichen Settlement-Seiten, per Lead-Month gemappt.
- **Messgrößen:** BMR = Settlement_offiziell − Close(Minutenbar vor Ankerende): ES/NQ Bar 14:59 CT, GC Bar 12:29 CT, ZB Bar 13:59 CT. Alle Größen auf instrumenteigenem Grid.
- **Zielgröße:** Return der ersten RTH-Stunde des Folgetags (Open → Open+60 min), vorzeichenbehaftet.
- **Signal:** Entry Folgetag-Open in Richtung sign(BMR) bei |BMR| ≥ Guard; Abstain sonst (gezählt und berichtet). Ausführung MES/MNQ-tauglich, Klasse II (Kosten unkritisch, Netto/Kosten ≈ 4× laut Pre-OPUS).
- **Strata:** Monatsend / Monatswoche / Rest; FOMC-Tage als eigenes Stratum (nicht gelöscht); DST-Flag-Tage gezählt.
- **Abfolge im Code:** (1) Settlement-Datenvalidierung (20-Tage-Stichprobe, Grid-Check) → (2) Guard-Überlebensraten-Tabelle + Abbruchregel → (3) Haupttest 500 Permutationen → (4) Dosis-Monotonie → (5) GC/ZB-Falsifikatoren → (6) Output im run1.txt-Format.
- **Vorregistrierte Erfolgskriterien:** Placebo-Perzentil > 95 %, Jonckheere p < 0,05, GC-Effekt nicht signifikant, ZB-Effekt nicht auf ES-Grid, Hit-Rate > 52 % bei n ≥ 500 Replikate gesamt.

## GO / NO-GO

**GO — mit zwei harten Vorbedingungen im Code.** (1) Die CME-Settlement-Daten müssen sich sauber auf den QC-Continuous mappen lassen und der Grid-Check muss zeigen, dass QC-Daily-Close ≠ Settlement ist (sonst ist das Feld in der QC-Repräsentation schon gelöscht und der A29-Vorsprung faktisch weg). (2) Die Guard-Überlebensrate muss nach Vorab-Messung ≥ 15 % bei Guard 0,5 (ES) bzw. 1,0 (NQ) liegen; darunter Guard auf ein Rundungs-Quantum senken, darunter NO-GO.

---

## Abschluss (3 Sätze + Urteil)

ID67o ist testbar, aber nur mit externem Settlement-Feed: QC-Daily-Bars liefern den letzten Trade, nicht den gerundeten 30-s-VWAP-Batch-Preis, also ist die CME-Settlements-Seite Pflicht-Datenquelle — was den A29-Repräsentations-Vorsprung sogar stützt. Die Rundungsfalle wird nicht durch bessere Schätzer gelöst, sondern durch Symmetrie: identische 0,25-Rundung aufs Pseudo-Anker-Placebo, instrumenteneigene Rundung (ZB 1/64) im Falsifikator, plus Guard-Kohorte |d| ≥ 0,25. Der entscheidende verbleibende Risikopunkt ist nicht die Methodik, sondern die Power: die Guard-Überlebensrate wird als erster Code-Schritt gemessen, und bei < 15 % auf einem Rundungs-Quantum ist der Test ohne Inferenz NO-GO.

**Urteil: GO (konditional auf Daten-Mapping + Überlebensrate ≥ 15 %).**
