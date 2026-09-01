# Strategic Innovation

## Metadaten

- **Name:** Strategic Innovation
- **Am besten für:** Themen bei denen das Ziel nicht Frontier-Dokumentation ist, sondern genuine neue Ideen aus Grundsätzen — durch Axiom-Extraktion, Dogmen-Dekonstruktion und Cross-Domain-Inspiration aus exotischen Wissensfeldern
- **Domänen:** 1 Kerndomäne + 2 externe Seed-Domänen aus `context/innovation_seeds.md`
- **Stakes:** Hoch — Output ist ein implementierbares Experiment mit explizitem Alpha-Vorteil
- **Sub-Agenten:** Ja (8 Phasen via Agent-Tool)
- **Primäres Modell:** claude-sonnet-4-6

## Wann diesen Ansatz verwenden

- User will nicht wissen was existiert, sondern was genuinely neu gebaut werden könnte
- Ziel ist: "Was ist die tiefste Wahrheit über dieses Problem — und was wird dadurch möglich?"
- Standard-Ansätze in der Domäne sind bekannt und eingepreist
- User will Dogmen explizit brechen, nicht nur dokumentieren
- Ein Axiom-First-Ansatz ist wichtiger als Frontier-Literatur

**Nicht verwenden wenn:**
- Hauptziel ist zu verstehen was aktuell im Feld passiert → Generative Explorer
- 3+ Domänen mit systematischer Cross-Domain-Synthese → Cross-Domain Synthesis
- Verlässliche Faktenbasis für Hochrisiko-Entscheidungen nötig → Multi-Agent Adversarial
- Thema völlig unbekannt, User braucht erst einen Überblick → starte mit Explorer, dann Strategic

## Der Kernunterschied zu anderen Ansätzen

Generative Explorer fragt: *"Was sagt die Frontier über dieses Thema, und welche Hypothesen entstehen daraus?"*
Strategic Innovation fragt: *"Was ist physikalisch/logisch wahr — und was ist dadurch möglich, wenn man alles andere ignoriert?"*

Explorer schaut vorwärts durch das Prisma vorhandener Literatur.
Strategic schaut rückwärts auf die Axiome — und dann vorwärts ohne das Gewicht der Konventionen.

Die beiden Ansätze ergänzen sich: Explorer zuerst kartiert die Landschaft. Strategic danach baut von den Axiomen aus neu.

## Selbst-Check

Vor der Ausführung prüfen:
1. Hat der User konkrete Axiom-Kandidaten oder Dogmen-Vermutungen? (Falls nein: Explorer-Lite erwägen)
2. Ist die Kerndomäne klar genug für First-Principles-Analyse? (Zu breit = schlechte Axiome)
3. Ist der User bereit mit konstruktiver Zerstörung (Advocatus Diaboli) zu arbeiten?

Falls 1 und 2 "nein": Explorer-Lite (Modus B) als Vorstufe empfehlen.

## Explorer-Check (Strategic-spezifisch)

Dieser Ansatz kennt drei Modi für den Umgang mit Frontier-Wissen. Der Coordinator prüft vor dem Interview welcher Modus passt.

### Entscheidungslogik

```
IF outputs/individual/*/hypothesis-catalogue.md existiert
   AND Thema passt zum aktuellen Projekt (laut project-context.md):
   → Option C anbieten: Explorer-Output laden

ELSE IF User kennt Frontier schlecht ODER Thema bewegt sich schnell:
   → Option B empfehlen: Explorer-Lite

ELSE:
   → Option A (Default): Standalone
```

### Modus A — Standalone (Default)
Keine externe Recherche. User kennt die Domäne, hat Axiom-Kandidaten und Dogmen-Vermutungen. Direkt zu Phase 1.
**Token-Aufwand:** Minimal — Web-Search erst ab Phase 5 (nur für überlebende Ideen).

### Modus B — Explorer-Lite
Ein einziger Haiku Web Researcher. Max 5–8 Quellen gesamt. Keine Domain Researchers. Keine Hypothesen-Phase.
Output: `scratchpad/[SLUG]-frontier-quick.md` — wird von Phase 1 als Zusatzkontext gelesen.
**Token-Aufwand:** Niedrig — ca. 20–30 Minuten Äquivalent.
**Prompt-Cap (PFLICHT):** "Falls du mehr als 8 relevante Quellen findest, wähle die 8 wichtigsten und stoppe."

### Modus C — Explorer-Output laden
Ein vorhandener Explorer-Run existiert zu diesem Thema. Coordinator liest:
- `outputs/individual/[explorer-SLUG]/hypothesis-catalogue.md`
- `outputs/individual/[explorer-SLUG]/experiment-designs.md`
Diese werden Phase 1 als Zusatzkontext übergeben: "Was hat der Explorer über dieses Thema herausgefunden?"
**Token-Aufwand:** Minimal — nur Datei-Reads.

---

## Rollen und Modell-Zuweisungen

| Rolle | Modell | Aufgabe |
|---|---|---|
| Research Coordinator | claude-sonnet-4-6 | Orchestrierung, Interview, Cluster-Memory-Management, finale Synthese |
| First Principles Agent | claude-sonnet-4-6 | Axiom-Extraktion + Dogma-Dekonstruktion — **kein Web-Zugriff** |
| Domain Matrix Seeder | claude-haiku-4-5-20251001 | Randomisierte Domänen-Auswahl aus innovation_seeds.md, Anti-Anchor |
| Idea Generator | claude-sonnet-4-6 | 5–10 Low-Fidelity-Ideen mit Anti-Anchor-Constraints |
| Advocatus Diaboli | claude-sonnet-4-6 | Destruktive Filterung auf 2–3 Stärkste — **liest nicht dogma-break.md** |
| Novelty Checker | claude-haiku-4-5-20251001 | Quick-Web-Existenz-Check für überlebende Ideen |
| Deep Researcher | claude-sonnet-4-6 | Vollrecherche der 1–3 überlebenden Ideen |
| Implementation Designer | claude-sonnet-4-6 | Experiment-Design, Stack, Alpha-Vorteil |
| Formatter | claude-haiku-4-5-20251001 | Final Report Assembly |

**Wichtige Modell-Regel:** Advocatus Diaboli **muss** Sonnet sein — Haiku ist zu flach für nicht-offensichtliche Angriffe auf Ideen.

---

## Orchestrierungs-Sequenz

### Phase 0: Coordinator — Cluster-Memory laden

1. Scanne `projects/` auf existierende Cluster
2. Zeige Liste falls vorhanden, frage User nach Zuordnung
3a. **Existierender Cluster:** lese `axiom-library.md`, `dogma-graveyard.md`, `idea-outcomes.md`
    → Informiere: "Cluster enthält [N] Axiome, [N] Dogmen, [N] Ideen"
3b. **Neuer Cluster:** leite cluster-slug ab, erstelle `projects/[cluster-slug]/` mit leeren Vorlagen
4. Explorer-Check: prüfe ob Modus A/B/C passt (siehe Explorer-Check Sektion)
5. Falls Modus B: Explorer-Lite Agent spawnen (BEVOR Phase 1)
6. Falls Modus C: lade Explorer-Outputs als Kontext

### Phase 1: First Principles Agent (Sonnet — kein Web)

**Timing:** Nach Explorer-Check und optionalem Explorer-Lite
**Keine Web-Suche** — das ist bewusst. Die Aufgabe ist rein kognitiv: was ist strukturell wahr?

**Liest:**
- `context/from-human/[SLUG]/project-context.md`
- `projects/[CLUSTER-SLUG]/axiom-library.md` (falls vorhanden)
- `projects/[CLUSTER-SLUG]/dogma-graveyard.md` (falls vorhanden)
- Optional: Explorer-Outputs falls Modus C

**Produziert:**
- `scratchpad/[SLUG]-axioms.md`: 5–10 Domänen-Axiome
- `scratchpad/[SLUG]-dogma-break.md`: 3–8 identifizierte Dogmen mit Dekonstruktion

**Nach Phase 1:** Coordinator schreibt neue Axiome (Status: Tentativ) in `projects/[CLUSTER-SLUG]/axiom-library.md` und neue Dogmen in `dogma-graveyard.md`.

### Phase 2: Domain Matrix Seeder (Haiku)

**Timing:** Nach First Principles Agent
**Liest:** `context/innovation_seeds.md` + `projects/[CLUSTER-SLUG]/idea-outcomes.md`
**Anti-Anchor-Protokoll:** Schließt die letzten 3 verwendeten Kombos aus, wählt aus verschiedenen Clustern

**Produziert:** `scratchpad/[SLUG]-domain-selection.md`

**Nach Phase 2:** Coordinator aktualisiert Verwendungs-Tracking in `context/innovation_seeds.md`.

### Phase 3: Idea Generator (Sonnet)

**Timing:** Nach Domain Matrix Seeder
**Liest:** `axioms.md`, `dogma-break.md`, `domain-selection.md`, `project-context.md`
**Anti-Anchor im Prompt:** Generiert 5–10 Low-Fidelity-Ideen aus Axiom×Dogma-Bruch×Seed-Domänen-Kombinationen

**Produziert:** `scratchpad/[SLUG]-discovery-draft.md`

### Phase 4: Advocatus Diaboli (Sonnet)

**Timing:** Nach Idea Generator

**KRITISCHE ARCHITEKTUR-ENTSCHEIDUNG:**
Der Advocatus liest **nicht** `dogma-break.md`. Das ist bewusst und muss so bleiben.
**Grund:** `dogma-break.md` enthält Gegenthesen zu Dogmen. Wenn der Advocatus diese kennt, neigt er dazu, Ideen die "anti-dogmatisch" klingen zu schonen — weil sie mutig klingen, nicht weil sie stark sind. Er prüft gegen die Axiome (`axioms.md`), nicht gegen die Dogmen. Axiome sind die härtere, objektivere Prüfung.

**Liest:** `discovery-draft.md`, `axioms.md`, `project-context.md` — **NICHT** `dogma-break.md`
**Prüft auf:** Axiom-Verstoß, fehlende strukturelle Neuheit, Einpreisung, technische Unmöglichkeit, fehlende Substitutionsresistenz
**Ergebnis:** 2–3 überlebende Ideen mit verbleibendem stärkstem Einwand

**Produziert:** `scratchpad/[SLUG]-feasibility-pre.md`

**Nach Phase 4:** Coordinator schreibt vorläufige Ideen-Ergebnisse in `projects/[CLUSTER-SLUG]/idea-outcomes.md`.

### Phase 5: Novelty Checker (Haiku + Web)

**Timing:** Nach Advocatus Diaboli
**Nur für überlebende Ideen aus Phase 4**
**Enge Aufgabe:** Existenz-Check — kein Deep Research

**Liest:** `feasibility-pre.md` (nur überlebende Ideen)
**Sucht:** Direkte Umsetzungen, Papers, Patente, Produkte zur Kernmechanik

**Produziert:** `outputs/individual/[SLUG]/novelty-check.md`
**Urteil pro Idee:** NOVEL / ÄHNLICHES EXISTIERT ([Referenz]) / BEREITS GEBAUT ([Referenz])

### Phase 6: Deep Researcher (Sonnet + Web)

**Timing:** Nach Novelty Checker
**Nur für Ideen mit Urteil NOVEL oder ÄHNLICHES EXISTIERT**

**Liest:** `feasibility-pre.md`, `novelty-check.md`, `axioms.md`, `project-context.md`
**Vollständige Recherche** zur technischen Machbarkeit, ähnlichen Ansätzen, Ressourcen, Zeitrahmen
**Beantwortet explizit:** Den stärksten verbleibenden Advocatus-Einwand

**Produziert:** `outputs/individual/[SLUG]/feasibility-check.md`

### Phase 7: Implementation Designer (Sonnet)

**Timing:** Nach Deep Researcher
**Liest:** `feasibility-check.md`, `axioms.md`, `dogma-break.md`, `project-context.md` (Hardware, Budget, Constraints)

**Für jede überlebende Idee:** Vollständiges Experiment-Design (siehe Sub-Agent Invocations)
**Strategic-spezifische Zusatzfelder:** Axiom-Basis, Gebrochenes Dogma, Mechanik-Kern, Alpha-Vorteil

**Produziert:** `outputs/individual/[SLUG]/experiment-designs.md`

### Phase 8: Formatter (Haiku)

**Timing:** Nach Implementation Designer
**Liest:** Alle Outputs

**Produziert:** `outputs/aggregated/mk-combined/[DATUM]-[SLUG]-strategic-report.md`

### Phase 9: Coordinator — Cluster-Memory finalisieren

1. Axiome in `axiom-library.md` finalisieren (Tentativ → Bestätigt falls durch Recherche gestützt)
2. Dogmen in `dogma-graveyard.md` finalisieren
3. Ideen-Ergebnisse in `idea-outcomes.md` finalisieren (Novelty-Check-Urteile eintragen)
4. `projects/[CLUSTER-SLUG]/project.md` Session-Zeile hinzufügen
5. `context/innovation_seeds.md` Tracking-Eintrag finalisieren (Ergebnis: gut/schwach/neutral)
6. `context/from-human/[SLUG]/research-approach.md` Session-Handoff schreiben

---

## Sub-Agent Invocations

### AGENT SPAWN: Explorer-Lite Web Researcher (Modus B)

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Phase 0 — falls Explorer-Modus B gewählt, VOR Phase 1

**Prompt-Template:**

```
Du bist Explorer-Lite Web Researcher für ein Strategic-Innovation-Projekt.

Deine Aufgabe ist bewusst begrenzt: Du sammelst einen schnellen Frontier-Überblick.
Kein Deep Research. Kein Ausarbeiten. Nur: Was ist der aktuelle Stand?

Lese:
- context/from-human/[SLUG]/project-context.md

Kerndomäne: [COORDINATOR FÜLLT EIN]

Suchstrategie:
- Suche nach aktuellem Stand in der Kerndomäne (letzte 12 Monate bevorzugt)
- Suche nach neuen Frameworks, Papers, Tools, Practitioner-Berichten
- Suche nach Kritik an bestehenden Ansätzen

WICHTIG: Falls du mehr als 8 relevante Quellen findest, wähle die 8 wichtigsten aus und stoppe.
Maximale Quellenzahl: 8. Das ist ein bewusster Token-Budget-Schutz.

Format für scratchpad/[SLUG]-frontier-quick.md:

# Frontier-Quick-Scan — [Thema]
Datum: [YYYY-MM-DD]

## Was ist der aktuelle Stand?
[3-5 Sätze Überblick]

## Quellen

### [Titel]
- URL: [url]
- Datum: [YYYY-MM]
- Zusammenfassung: [2 Sätze]
- Warum relevant: [1 Satz]

[Maximal 8 Quellen]

## Frontier-Beobachtung
[1 Absatz: Was bewegt sich gerade in diesem Feld?]
```

**Erwartete Output-Datei:** `scratchpad/[SLUG]-frontier-quick.md`

---

### AGENT SPAWN: First Principles Agent

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Phase 1 — nach Explorer-Check

**Prompt-Template:**

```
Du bist First Principles Agent für ein Strategic-Innovation-Projekt.

Du hast KEINEN Zugriff auf das Web. Das ist bewusst und wichtig.
Deine Aufgabe ist rein kognitiv: herausarbeiten was strukturell wahr ist.

Lese:
- context/from-human/[SLUG]/project-context.md
- projects/[CLUSTER-SLUG]/axiom-library.md (falls vorhanden — vorherige bestätigte Axiome)
- projects/[CLUSTER-SLUG]/dogma-graveyard.md (falls vorhanden — bereits bekannte Dogmen)
[COORDINATOR FÜLLT EIN — falls Modus C oder B: zusätzlich Explorer-Outputs lesen]

---

TEIL 1: AXIOM-EXTRAKTION

Was ist ein Axiom für unsere Zwecke?
Ein Axiom ist eine physikalische, logische oder strukturelle Wahrheit über die Domäne
die nicht durch Marktdynamik, Meinung oder Konvention entfernt werden kann.

Test-Fragen für ein Axiom:
- Gilt das unabhängig davon was Experten sagen?
- Kann das wegdiskutiert werden oder ist es strukturell notwendig?
- Würde das in 100 Jahren immer noch gelten?

NICHT als Axiom akzeptieren:
- "X wird immer wichtiger" → zu vage, nicht falsifizierbar
- "Diversifikation reduziert Risiko" → Konvention, nicht Axiom
- "KI verändert alles" → Meinung

JA als Axiom akzeptieren:
- "Ein Zero-Sum-Spiel hat genau so viele Verlierer wie Gewinner" → logische Wahrheit
- "Liquidität kostet — irgendjemand trägt immer das Risiko des Nicht-Handels" → strukturelle Wahrheit
- "Information kann nicht rückwirkend unbekannt gemacht werden" → physikalische Wahrheit

Generiere 5–10 Axiome für die Domäne des Projekts.

Format für scratchpad/[SLUG]-axioms.md:

# Axiom-Analyse — [Thema]
Session: [SLUG]

## Extrahierte Axiome

### A[N]: [Kurztitel]
**Formulierung:** [Präzise, falsifizierbare Aussage]
**Warum Axiom und nicht Meinung:** [Begründung — was macht das nicht wegdiskutierbar?]
**Implikationen:** [Was folgt logisch daraus?]
**Was damit brechbar wäre:** [Welche bestehenden Annahmen werden infrage gestellt?]
**Konfidenz:** Hoch | Mittel

Falls axiom-library.md vorhanden:
Am Ende vergleiche neue Axiome mit vorhandenen. Markiere:
- BESTÄTIGT: [A[N] aus library] — dieser Axiom wurde erneut unabhängig erarbeitet
- ERWEITERT: [A[N] aus library] — neuer Aspekt gefunden
- WIDERSPRICHT: [A[N] aus library] — Begründung warum

---

TEIL 2: DOGMA-DEKONSTRUKTION

Was ist ein Dogma für unsere Zwecke?
Ein Dogma ist eine Überzeugung, Heuristik oder Praxis in der Domäne die:
a) so weit verbreitet ist dass sie kaum hinterfragt wird
b) aus einer früheren Epoche oder einem anderen Kontext stammt
c) eingepreist ist — alle glauben daran, also bietet Befolgen keinen Vorteil mehr

Wichtig: Dogmen sind oft korrekt gewesen — aber sie sind durch Konsens nutzlos
gemacht worden oder durch geänderte Rahmenbedingungen überholt.

Was ein Dogma NICHT ist:
- Eine Aussage die einfach falsch ist
- Eine Aussage die noch niemand befolgt (dann ist sie noch nicht eingepreist)

Format für scratchpad/[SLUG]-dogma-break.md:

# Dogma-Analyse — [Thema]
Session: [SLUG]

## Identifizierte Dogmen

### D[N]: [Dogma-Titel]
**Das Dogma:** [Wie wird es normalerweise formuliert? Wörtlich wenn möglich.]
**Ursprung:** [Wann/wo hat diese Überzeugung begonnen? Wann war sie sinnvoll?]
**Warum eingepreist:** [Wie verbreitet? Was ist der Preis des Nichtbefolgens heute — keiner?]
**Axiomatische Prüfung:** [Hält das Dogma den Axiomen aus Teil 1 stand? Wo bricht es?]
**Gegenthese:** [Die nicht-offensichtliche, axiomatisch valide Alternative]
**Potenzial:** [Falls das Dogma gebrochen wird — was wird dadurch möglich?]

Sei mutig. Dogmen die niemanden provozieren sind keine echten Dogmen.
Falls dogma-graveyard.md vorhanden: prüfe ob ein Dogma bereits bekannt ist — nicht doppeln.

Speichere:
- scratchpad/[SLUG]-axioms.md
- scratchpad/[SLUG]-dogma-break.md
```

**Erwartete Output-Dateien:**
- `scratchpad/[SLUG]-axioms.md`
- `scratchpad/[SLUG]-dogma-break.md`

**Was der Coordinator danach tut:** Schreibt neue Axiome (Status: Tentativ) und Dogmen in die Cluster-Dateien.

---

### AGENT SPAWN: Domain Matrix Seeder

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Phase 2 — nach First Principles Agent

**Prompt-Template:**

```
Du bist Domain Matrix Seeder für ein Strategic-Innovation-Projekt.

Deine Aufgabe: Wähle 2 externe Inspirations-Domänen aus der Innovation-Seeds-Matrix.
Ziel ist maximaler struktureller Kontrast zur Kerndomäne — nicht offensichtliche Passung.

Lese:
- context/innovation_seeds.md — die 30 verfügbaren Domänen mit Verwendungs-Tracking
- projects/[CLUSTER-SLUG]/idea-outcomes.md — (falls vorhanden) welche Kombos bereits versucht
- context/from-human/[SLUG]/project-context.md — Kerndomäne und Ziel

Anti-Anchor-Protokoll (PFLICHT — dokumentiere jeden Schritt):
1. Liste alle 30 Domänen mit Datum der letzten Verwendung
2. Schließe alle Kombos aus die in den letzten 3 Sessions verwendet wurden
3. Schließe alle Kombos aus die bereits in diesem Cluster laut idea-outcomes.md versucht wurden
4. Priorisiere Domänen mit dem höchsten Wert bei "Tage seit letzter Verwendung"
5. Die zwei Domänen müssen aus verschiedenen Clustern stammen

Auswahlkriterien:
- Maximaler struktureller Kontrast zur Kerndomäne
- Verschiedene Cluster (nicht beide aus demselben)
- Das Übertragungspotenzial muss zur Projektdomäne passen
- Mindestens eine Domäne soll auf den ersten Blick nicht zur Kerndomäne passen

Format für scratchpad/[SLUG]-domain-selection.md:

# Domänen-Auswahl — [SLUG]

## Anti-Anchor-Protokoll
[Was wurde ausgeschlossen? Warum? Vollständige Dokumentation.]

## Gewählte Domänen

### Domäne 1: [Name] (Cluster [N])
**Kernprinzip:** [Aus innovation_seeds.md — vollständig übernehmen]
**Übertragungspotenzial:** [Aus innovation_seeds.md]
**Warum hier relevant:** [Bezogen auf die Kerndomäne des Projekts]
**Struktureller Kontrast:** [Was ist fundamental anders als in der Kerndomäne?]

### Domäne 2: [Name] (Cluster [N])
[Gleiche Struktur]

## Kombinationslogik
[Warum diese zwei Domänen ZUSAMMEN interessant sind — nicht nur einzeln.
Was entsteht durch die Dreifach-Kombination: Kerndomäne + Domäne 1 + Domäne 2?]

Aktualisiere danach context/innovation_seeds.md:
- Setze "Zuletzt verwendet" für beide Domänen auf heute [YYYY-MM-DD]
- Füge Eintrag in Verwendungs-Tracking-Tabelle: [Domäne1] + [Domäne2] | Datum | [SLUG] | [Cluster] | Ergebnis: TBD
```

**Erwartete Output-Dateien:**
- `scratchpad/[SLUG]-domain-selection.md`
- `context/innovation_seeds.md` (Verwendungs-Tracking aktualisiert)

---

### AGENT SPAWN: Idea Generator

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Phase 3 — nach Domain Matrix Seeder

**Prompt-Template:**

```
Du bist Idea Generator für ein Strategic-Innovation-Projekt.

Deine Aufgabe: Generiere 5–10 Low-Fidelity-Ideen. Low-Fidelity bedeutet:
- Breite statt Tiefe — lieber 8 halbfertige als 2 überdachte
- Keine vollständige Ausarbeitung — das kommt in Phase 7
- Kein Selbst-Zensurieren — das macht Phase 4 (Advocatus Diaboli)

Lese:
- scratchpad/[SLUG]-axioms.md
- scratchpad/[SLUG]-dogma-break.md
- scratchpad/[SLUG]-domain-selection.md
- context/from-human/[SLUG]/project-context.md

Anti-Anchor-Constraints (PFLICHT — lies und verinnerliche BEVOR du generierst):
1. Keine Idee die direkt aus der Hauptdomäne kommt ohne Einfluss der Seed-Domänen
2. Keine Idee die ein identifiziertes Dogma reinstalliert
3. Mindestens 50% der Ideen müssen BEIDE Seed-Domänen berühren
4. Keine Idee die nur inkrementell besser ist als Status Quo — muss strukturell anders sein
5. Keine Idee die als "offensichtliche Antwort" auf das Problem gilt

Generierungs-Quellen (nutze alle vier):
A) Axiom × Dogmen-Bruch: Was wird möglich wenn Axiom [X] mit gebrochenem Dogma [Y] kombiniert?
B) Seed-Domäne 1 × Kerndomäne: Welches Kernprinzip von [Domäne 1] auf [Kerndomäne] anwenden?
C) Seed-Domäne 2 × Kerndomäne: Gleiche Logik
D) Beide Seed-Domänen × Kerndomäne: Dreifach-Kombination — am schwierigsten, höchstes Potenzial

Format für scratchpad/[SLUG]-discovery-draft.md:

# Discovery Draft — [Thema]
Session: [SLUG]

## Generierungs-Kontext
- Axiome genutzt: [A1, A3, ...]
- Gebrochene Dogmen: [D2, D5, ...]
- Seed-Domänen: [Domäne 1] + [Domäne 2]

## Ideen

### ID[N]: [Kurztitel]
**Kern-Idee (1 Satz):** [Was ist das Neue?]
**Axiomatische Basis:** [Welcher Axiom macht das möglich? Referenz auf A[N].]
**Gebrochenes Dogma:** [Welches Dogma wird ignoriert? Referenz auf D[N].]
**Seed-Domänen-Einfluss:** [Welches Prinzip aus welcher Seed-Domäne steckt dahinter?]
**Warum strukturell neu:** [Was unterscheidet das fundamental vom Status Quo?]
**Erste Schwachstelle (eigene Einschätzung):** [Was wird Phase 4 daran angreifen?]

Wichtig: Keine Idee länger als 10 Zeilen. Selbstzensur verboten.
```

**Erwartete Output-Datei:** `scratchpad/[SLUG]-discovery-draft.md`

---

### AGENT SPAWN: Advocatus Diaboli

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Phase 4 — nach Idea Generator

**Prompt-Template:**

```
Du bist Advocatus Diaboli für ein Strategic-Innovation-Projekt.

Deine Aufgabe: Zerstöre schwache Ideen. Behalte 2–3 die echte Substanz haben.

KRITISCH — LIES DAS ZUERST:
Du liest NICHT scratchpad/[SLUG]-dogma-break.md. Das ist bewusst und wichtig.
Begründung: dogma-break.md enthält Gegenthesen zu Dogmen. Wenn du diese kennst,
wirst du dazu neigen Ideen zu schonen die "anti-dogmatisch klingen" — weil sie mutig
klingen, nicht weil sie stark sind. Deine Prüfung erfolgt gegen Axiome, nicht gegen
Dogmen. Axiome sind der härtere, objektivere Maßstab.

Lese:
- scratchpad/[SLUG]-discovery-draft.md
- scratchpad/[SLUG]-axioms.md
- context/from-human/[SLUG]/project-context.md

Prüf-Kriterien (wende alle an, in dieser Reihenfolge):

1. AXIOM-KONSISTENZ: Verletzt die Idee einen der identifizierten Axiome?
   Ein Axiom-Verstoß ist sofortige Eliminierung — nicht Abschwächung.

2. STRUKTURELLE NEUHEIT: Ist das fundamental anders oder nur inkrementell besser?
   "10% effizienter" ist nicht fundamental neu. "Andere Mechanik" ist fundamental neu.

3. EINPREISUNG: Ist das längst eingepreist? Wenn ja — warum würde das einen Vorteil geben?
   Eine eingepreiste Idee kann gut sein — aber dann braucht es einen erklärten Mechanismus
   warum sie trotzdem Vorteil schafft.

4. FEASIBILITY-FLOOR: Gibt es einen technischen/physikalischen Grund warum das UNMÖGLICH ist?
   Nicht schwer — unmöglich. Schwierig ist kein Ausschlussgrund.

5. SUBSTITUTIONSRESISTENZ: Warum kann das nicht in 12 Monaten kopiert werden?
   Falls die Idee kein strukturelles Differenzierungsmerkmal hat — schwache Idee.

Format für scratchpad/[SLUG]-feasibility-pre.md:

# Advocatus Diaboli — Filterung
Session: [SLUG]

## Eliminierte Ideen

### ELIMINIERT: ID[N] — [Kurztitel]
**Tötender Einwand:** [Der eine Grund warum das nicht funktioniert — präzise, kein Padding]
**Kriterium:** Axiom-Verstoß | Nicht strukturell neu | Eingepreist | Unmöglich | Nicht substitutionsresistent

[Ein Eintrag pro eliminierter Idee]

## Überlebende Ideen (2–3)

### ÜBERLEBT: ID[N] — [Kurztitel]
**Warum stark:** [Konkrete Begründung — was hat alle 5 Prüfungen bestanden?]
**Stärkster verbleibender Einwand:** [Was ist noch offen — für Phase 6 zu beantworten]
**Advocatus-Konfidenz:** Hoch | Mittel

## Begründung der finalen Auswahl
[Warum genau diese 2–3 und nicht andere? Vergleichende Begründung.]
```

**Erwartete Output-Datei:** `scratchpad/[SLUG]-feasibility-pre.md`

**Was der Coordinator danach tut:** Schreibt vorläufige Ideen-Ergebnisse in `projects/[CLUSTER-SLUG]/idea-outcomes.md`.

---

### AGENT SPAWN: Novelty Checker

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Phase 5 — nach Advocatus Diaboli, mit Web-Suche

**Prompt-Template:**

```
Du bist Novelty Checker für ein Strategic-Innovation-Projekt.

Deine Aufgabe ist eng und spezifisch: prüfe ob die überlebenden Ideen bereits existieren.
Kein Deep Research. Kein Ausarbeiten. Nur: Existenz-Check.

Lese:
- scratchpad/[SLUG]-feasibility-pre.md — nur die überlebenden Ideen

Für jede überlebende Idee:
1. Formuliere 2–3 präzise Suchqueries die die KERNMECHANIK beschreiben (nicht den Namen)
2. Suche nach direkten Umsetzungen, Patenten, Papers, Produkten, Startups
3. Entscheide: NOVEL / ÄHNLICHES EXISTIERT / BEREITS GEBAUT

Suchstrategie:
- Suche nach der Mechanik, nicht nach dem Label
- Google Scholar / arXiv für akademische Papers
- Google / ProductHunt / Crunchbase für Produkte/Startups
- Google Patents wenn die Idee patentierbar klingt

Format für outputs/individual/[SLUG]/novelty-check.md:

# Novelty Check — [SLUG]
Datum: [YYYY-MM-DD]

## Idee ID[N]: [Kurztitel]

**Suchqueries:**
- [Query 1 — Kernmechanik beschreibend]
- [Query 2]
- [Query 3 optional]

**Gefundene Referenzen:**
- [URL | Titel | Datum | Was gefunden wurde — 1 Satz]
[oder: "Keine direkten Treffer"]

**Urteil:** NOVEL | ÄHNLICHES EXISTIERT | BEREITS GEBAUT

**Begründung:**
[Falls ÄHNLICHES EXISTIERT: worin besteht der verbleibende Unterschied?]
[Falls BEREITS GEBAUT: direkte Referenz — diese Idee scheidet aus Phase 6 aus]

**Empfehlung für Phase 6:** Weiter recherchieren | Ausschließen

[Wiederhole für jede überlebende Idee]

## Zusammenfassung
- Weitergeleitet an Phase 6: [Liste der IDs]
- Ausgeschieden nach Novelty-Check: [Liste der IDs mit Grund]
```

**Erwartete Output-Datei:** `outputs/individual/[SLUG]/novelty-check.md`

---

### AGENT SPAWN: Deep Researcher

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Phase 6 — nach Novelty Checker

**Prompt-Template:**

```
Du bist Deep Researcher für ein Strategic-Innovation-Projekt.

Du recherchierst vollständig die Ideen die Phase 4 und Phase 5 überlebt haben.

Lese:
- scratchpad/[SLUG]-feasibility-pre.md (überlebende Ideen + stärkster Einwand)
- outputs/individual/[SLUG]/novelty-check.md (Novelty-Urteil und Referenzen)
- scratchpad/[SLUG]-axioms.md
- context/from-human/[SLUG]/project-context.md

Recherchiere für jede Idee mit Urteil NOVEL oder ÄHNLICHES EXISTIERT:

1. TECHNISCHE MACHBARKEIT: Was ist der aktuelle Stand? Was ist verfügbar, was muss entwickelt werden?
2. ÄHNLICHE ANSÄTZE: Was ist vergleichbar — und was unterscheidet diese Idee trotzdem?
3. RESSOURCEN: Hardware, Daten, Expertise, Kapital — was braucht man konkret?
4. ZEITRAHMEN: Heute baubar / 12 Monate / 24 Monate? Mit Begründung.
5. ADVOCATUS-ANTWORT: Ist der stärkste Einwand aus Phase 4 widerlegbar? Falls ja: wie?

Format für outputs/individual/[SLUG]/feasibility-check.md:

# Feasibility Check — [SLUG]

## Idee ID[N]: [Kurztitel]

### Technische Machbarkeit
[Stand der Technik, was verfügbar, was entwickelt werden müsste]

### Ähnliche Ansätze & Differenzierung
[Was ist vergleichbar — und warum ist diese Idee trotzdem unterschiedlich?]

### Ressourcen-Anforderungen
- Technologie: [was braucht man]
- Daten: [welche Daten, Verfügbarkeit, Kosten]
- Expertise: [welche Skills]
- Kapital: [Schätzung]

### Zeitrahmen
[Heute / 12 Monate / 24 Monate / Langfristig — mit Begründung]

### Stärkster Advocatus-Einwand — Antwort
[Ist der Einwand widerlegt? Falls ja: wie? Falls nein: warum geht die Idee trotzdem weiter?]

### Quellen
[Alle Quellen mit Datum und URL]
```

**Erwartete Output-Datei:** `outputs/individual/[SLUG]/feasibility-check.md`

---

### AGENT SPAWN: Implementation Designer

**Modell:** `claude-sonnet-4-6`

**Zeitpunkt:** Phase 7 — nach Deep Researcher

**Prompt-Template:**

```
Du bist Implementation Designer für ein Strategic-Innovation-Projekt.

Du designst konkrete, umsetzbare Experimente für die Ideen die alle Filter überlebt haben.

Lese:
- outputs/individual/[SLUG]/feasibility-check.md
- scratchpad/[SLUG]-axioms.md
- scratchpad/[SLUG]-dogma-break.md
- context/from-human/[SLUG]/project-context.md (Hardware, Budget, Constraints)

Für jede Idee aus feasibility-check.md: ein vollständiges Experiment-Design.

Format für outputs/individual/[SLUG]/experiment-designs.md:

# Experiment Designs — Strategic Innovation — [SLUG]

### E[N]: [Titel]

**Bezug:** Idee ID[N]
**Kern-Idee (1 Satz):** [Was wird gebaut/getestet?]

**Axiom-Basis:**
[Welche Axiome aus axioms.md machen das möglich? Direkte Referenz auf A[N].]

**Gebrochenes Dogma:**
[Welches Dogma aus dogma-break.md wird ignoriert? Direkte Referenz auf D[N].]

**Mechanik-Kern:**
[Was ist der fundamentale Mechanismus der diese Idee neu macht?
Nicht: "wir nutzen KI". JA: "wir nutzen das Quorum-Sensing-Prinzip um X zu erreichen".]

**Methode:**
[Konkrete Beschreibung — kein Buzzword-Padding.
Was genau wird gemacht, in welcher Reihenfolge?]

**Benötigter Stack:**
- Tools: [exakte Namen und Versionen wenn relevant]
- Daten: [welche Daten, Verfügbarkeit, Kosten]
- Hardware: [passt das zu [USER-HARDWARE aus project-context.md]?]
- Kosten: [geschätzt — einmalig und laufend]

**Zeitaufwand (Minimal-Version):**
[Stunden oder Tage für erste lauffähige Version]

**Claude Code Rolle:**
[Wie kann Claude Code konkret helfen? Spezifisch — nicht generisch.]

**Validierungskriterium:**
[Woran erkennt man ob das genuinely neu ist und nicht eine Reinvention?]

**Alpha-Vorteil:**
[Was für einen Vorteil schafft das — und wie lange ist er haltbar?
Zeitfenster: Monate / Jahre / strukturell dauerhaft — mit Begründung]

**Erfolgskriterium:**
[Woran erkennt man ob die Idee funktioniert? Messbar.]

**Failure Modes:**
- [Was könnte das Experiment ungültig machen?]
- [Welche Annahmen können brechen?]

**Nächster konkreter Schritt:**
[Eine einzige Aktion, klein und spezifisch, die man morgen starten könnte]

**Konfidenz:** Hoch | Mittel | Niedrig | Spekulativ
```

**Erwartete Output-Datei:** `outputs/individual/[SLUG]/experiment-designs.md`

---

### AGENT SPAWN: Formatter

**Modell:** `claude-haiku-4-5-20251001`

**Zeitpunkt:** Phase 8 — nach Implementation Designer

**Prompt-Template:**

```
Du bist Formatter für ein Strategic-Innovation-Projekt.

Lese:
- outputs/individual/[SLUG]/experiment-designs.md
- outputs/individual/[SLUG]/feasibility-check.md
- outputs/individual/[SLUG]/novelty-check.md
- scratchpad/[SLUG]-axioms.md
- scratchpad/[SLUG]-dogma-break.md
- scratchpad/[SLUG]-feasibility-pre.md

Erstelle Final Report als:
outputs/aggregated/mk-combined/[DATUM]-[SLUG]-strategic-report.md

Struktur:

# [Thema] — Strategic Innovation Report
Datum: [YYYY-MM-DD]
Cluster: [cluster-slug]
Session: [SLUG]
Explorer-Modus: [A / B / C]

## Executive Summary
[Was sind die 1–3 stärksten Ideen? Axiomatischer Kontext in 3 Sätzen.
Welche Dogmen wurden gebrochen? Direkt, ohne Padding. Ehrlich über Konfidenz.]

## Implementierbare Experimente (priorisiert)
[Vollständig aus experiment-designs.md — alle Felder, nichts kürzen]

## Axiome & Mechanik
[Alle Axiome aus axioms.md — vollständig mit Implikationen]

## Dogma-Analyse
[Alle identifizierten Dogmen aus dogma-break.md — vollständig]

## Eliminierte Ideen (Kurzfassung)
[Pro eliminierter Idee: Titel + tötender Einwand — 1 Zeile]

## Novelty-Check Übersicht
[Pro geprüfter Idee: Urteil + Schlüsselreferenz falls relevant]

## Cluster-Update (Vorschau)
[Was wird in die Cluster-Dateien geschrieben — als Vorschau für den Coordinator:
 N neue Axiome / N neue Dogmen / N Ideen mit Ergebnis]

Inhalt NICHT verändern — nur Formatierung, Struktur und Konsistenz.
```

**Erwartete Output-Datei:** `outputs/aggregated/mk-combined/[DATUM]-[SLUG]-strategic-report.md`

---

## Fallback

Falls das Agent-Tool in dieser Session nicht verfügbar ist:
1. User benachrichtigen: "Das Agent-Tool ist nicht verfügbar. Ich führe den Strategic-Innovation-Ansatz sequenziell im selben Kontext aus. Der Advocatus Diaboli hat dann Zugriff auf meinen gesamten Kontext — der Isolations-Vorteil entfällt, insbesondere das Nicht-Lesen von dogma-break.md ist dann nicht erzwingbar."
2. Alle Phasen sequenziell ausführen
3. Beim Advocatus-Schritt explizit deklarieren: "Ich wechsle in die Advocatus-Diaboli-Rolle und ignoriere bewusst die Inhalte aus dogma-break.md."

---

## Output-Struktur

```
scratchpad/
├── [SLUG]-axioms.md                     (Phase 1)
├── [SLUG]-dogma-break.md                (Phase 1)
├── [SLUG]-domain-selection.md           (Phase 2)
├── [SLUG]-discovery-draft.md            (Phase 3)
├── [SLUG]-feasibility-pre.md            (Phase 4)
└── [SLUG]-frontier-quick.md             (nur Modus B)

outputs/
├── individual/
│   └── [SLUG]/
│       ├── novelty-check.md             (Phase 5)
│       ├── feasibility-check.md         (Phase 6)
│       └── experiment-designs.md        (Phase 7)
└── aggregated/
    └── mk-combined/
        └── YYYY-MM-DD-[SLUG]-strategic-report.md  (Phase 8)

projects/
└── [cluster-slug]/
    ├── project.md                       (Phase 0 + Phase 9)
    ├── axiom-library.md                 (nach Phase 1, finalisiert Phase 9)
    ├── dogma-graveyard.md               (nach Phase 1, finalisiert Phase 9)
    └── idea-outcomes.md                 (nach Phase 4, finalisiert Phase 9)

context/
├── from-human/[SLUG]/
│   ├── project-context.md
│   └── research-approach.md            (Phase 9 Session-Handoff)
└── innovation_seeds.md                 (Tracking nach Phase 2)

notes/
└── [SLUG]-research-log.md
```

---

## Final Report Struktur

Siehe Formatter-Prompt oben. Der Report enthält immer:
- Executive Summary mit ehrlicher Konfidenz-Einschätzung
- Vollständige Experiment-Designs (keine Kürzungen)
- Vollständige Axiome und Dogmen
- Eliminierte Ideen als Kurzfassung (Lerneffekt)
- Novelty-Check-Übersicht
- Cluster-Update-Vorschau

---

## Session-Handoff

In `context/from-human/[SLUG]/research-approach.md` nach Session-Abschluss ergänzen:

```markdown
## Session [N] — [Datum]
**Approach:** Strategic Innovation
**Cluster:** [cluster-slug]
**Explorer-Modus:** [A — Standalone / B — Explorer-Lite / C — Explorer-Output geladen ([SLUG])]
**Axiome:** [N neue Axiome] — wichtigste: [A1: Kurztitel]
**Dogmen:** [N gebrochen] — wichtigstes: [D1: Kurztitel]
**Seed-Domänen:** [Domäne 1] + [Domäne 2]
**Ideen:** [N generiert] → [N überlebt Advocatus] → [N überlebt Novelty-Check]
**Stärkstes Experiment:** [E1-Titel]
**Alpha-Vorteil:** [Kurzform]
**Nächste Session:** [Implementierung / weitere Ideen / andere Cluster-Domäne / Explorer-Vertiefung]
**Cluster-Memory:** [N] Axiome, [N] Dogmen, [N] Ideen aktualisiert
```

---

## Deliverables-Checkliste

- [ ] `scratchpad/[SLUG]-axioms.md` (Phase 1)
- [ ] `scratchpad/[SLUG]-dogma-break.md` (Phase 1)
- [ ] `projects/[cluster-slug]/axiom-library.md` — nach Phase 1 aktualisiert
- [ ] `projects/[cluster-slug]/dogma-graveyard.md` — nach Phase 1 aktualisiert
- [ ] `scratchpad/[SLUG]-domain-selection.md` (Phase 2)
- [ ] `context/innovation_seeds.md` — Tracking nach Phase 2 aktualisiert
- [ ] `scratchpad/[SLUG]-discovery-draft.md` (Phase 3)
- [ ] `scratchpad/[SLUG]-feasibility-pre.md` (Phase 4)
- [ ] `projects/[cluster-slug]/idea-outcomes.md` — nach Phase 4 aktualisiert
- [ ] `outputs/individual/[SLUG]/novelty-check.md` (Phase 5)
- [ ] `outputs/individual/[SLUG]/feasibility-check.md` (Phase 6)
- [ ] `outputs/individual/[SLUG]/experiment-designs.md` (Phase 7)
- [ ] `outputs/aggregated/mk-combined/[DATUM]-[SLUG]-strategic-report.md` (Phase 8)
- [ ] `projects/[cluster-slug]/project.md` — Session-Zeile (Phase 9)
- [ ] `context/from-human/[SLUG]/research-approach.md` — Session-Handoff (Phase 9)
- [ ] `notes/[SLUG]-research-log.md` — vollständig mit Checkpoints
