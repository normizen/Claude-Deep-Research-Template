# Initiate Strategic Innovation Project

Du startest ein Strategic-Innovation-Projekt. Das Ziel ist nicht Frontier-Dokumentation —
sondern genuine neue Ideen aus Grundsätzen. Durch Axiom-Extraktion, Dogmen-Dekonstruktion
und Cross-Domain-Inspiration entstehen implementierbare Ansätze die strukturell neu sind.

Lese zunächst `approaches/strategic-innovation.md` vollständig — diese Datei definiert
die Orchestrierung für alle Phasen dieses Commands.

---

## Step 0: Bestandsprüfung

Bevor du irgendetwas anderes tust — prüfe ob bereits Inhalte vorhanden sind.

**Scan folgende Verzeichnisse auf Nicht-.gitkeep-Dateien:**
- `outputs/individual/` — einzelne Outputs
- `outputs/aggregated/mk-combined/` — kombinierte Reports
- `context/from-human/` — projektspezifische Kontext-Dateien

**Vorgehen:**

1. Lies `context/from-human/` auf vorhandene Dateien
2. Lies `outputs/aggregated/mk-combined/` auf vorhandene `.md`-Dateien
3. Falls Inhalte gefunden:

```
Es gibt bestehende Inhalte in diesem Repository:

  Projekt: [Projektname]
  Datum:   [Datum]
  Thema:   [Thema]
  Dateien: [kurze Liste]

Was soll ich damit machen bevor wir starten?
  A) Archivieren — Dateien nach context/from-history/[projektname]/ verschieben
  B) Löschen — Dateien entfernen (unwiderruflich)
  C) Behalten — nichts ändern, neues Projekt startet trotzdem

Hinweis: Das neue Projekt bekommt einen eigenen Unterordner.
```

4. **Warte auf Antwort des Users**
   - **A**: Archivieren nach `context/from-history/[slug]/`, dann weiter mit Step 0.5
   - **B**: Löschen nach Bestätigung, dann weiter mit Step 0.5
   - **C**: Direkt weiter mit Step 0.5

5. **Falls keine Inhalte gefunden**: Direkt weiter mit Step 0.5

---

## Step 0.5: Explorer-Check

Bevor das Interview beginnt: prüfe ob und wie viel Frontier-Wissen sinnvoll ist.

**Scan:**
1. Prüfe ob `outputs/individual/*/hypothesis-catalogue.md` existiert (Explorer-Outputs)
2. Falls gefunden: lies die zugehörige `context/from-human/[SLUG]/project-context.md` um das Thema einzuschätzen

**Entscheidungslogik:**
```
IF hypothesis-catalogue.md gefunden AND thematisch relevant:
    → Option C anbieten (Explorer-Output laden)

IF User hat angedeutet dass er die Frontier nicht gut kennt
   OR Thema klingt nach schnell-bewegendem Feld:
    → Option B empfehlen (Explorer-Lite)

ELSE:
    → Option A (Standalone, Default)
```

**Zeige dem User:**

```
Bevor wir starten: Wie viel Frontier-Wissen soll einfließen?

  A) Standalone — du kennst die Domäne, klare Axiom-Kandidaten vorhanden
     Keine externe Recherche — direkt zum Interview
     Token-Aufwand: minimal

  B) Explorer-Lite — schneller Web-Scan (max 5–8 Quellen, kein Deep Research)
     Gibt Frontier-Kontext ohne vollständige Explorer-Run
     Token-Aufwand: niedrig

  C) Explorer-Output laden — Explorer-Session bereits vorhanden
     [Falls gefunden: "Gefundene Session: [SLUG] — [Thema], [Datum]"]
     Lese Hypothesen und Experiment-Designs als Zusatzkontext
     Token-Aufwand: minimal (nur Datei-Reads)
```

**Warte auf Auswahl.**

- **Bei A**: Direkt weiter mit Step 1
- **Bei B**: Explorer-Lite Agent spawnen (Haiku, max 5–8 Quellen, Prompt aus `approaches/strategic-innovation.md`). Warte auf Abschluss. Dann weiter mit Step 1.
- **Bei C**: Lade die gefundenen Explorer-Outputs in den Coordinator-Kontext. Dann weiter mit Step 1.

Merke den gewählten Explorer-Modus für `project-context.md` (Step 5a).

---

## Step 1: Adaptives Strategic-Interview

Das Interview für diesen Modus ist gesprächsbasiert — **keine feste Liste die auf einmal gestellt wird**.

Stelle **eine Frage zur Zeit**. Warte auf die Antwort. Entscheide dann:
- Antwort ist präzise und vollständig → nächste Kernfrage
- Antwort ist vage oder offen → Follow-up-Frage stellen
- Antwort öffnet wichtigen Thread → gezielt nachbohren
- Antwort hat Framing-Problem → sanft korrigieren und dann weiter

**Die 5 Kernfragen (müssen alle beantwortet werden):**

**Frage 1 — Problem & Domäne:**
"Was ist die Kerndomäne oder das Problem — und was ist die aktuell vorherrschende Methode zur Lösung?"

**Frage 2 — Eigenes Wissen:**
"Was weißt du bereits darüber — und wo ist die Grenze deines Wissens, wo es interessant wird?"

**Frage 3 — Vermutete Dogmen:**
"Was ist in dieser Domäne so tief verwurzelt, dass es kaum hinterfragt wird?"

**Frage 4 — Zieltyp:**
"Was soll am Ende entstehen? Eine neue Methode / ein Produkt / ein Prozess / ein Mechanismus?"

**Frage 5 — Constraints:**
"Was darf die Lösung nicht sein — technisch, ethisch, ressourcentechnisch?"

**Abschluss — Synthesis-Check:**
"Ich habe verstanden: [Zusammenfassung von X, Y, Z aus den Antworten]. Gibt es etwas Wichtiges das ich noch nicht weiß?"

---

## Step 1.5: Follow-up-Trigger-Regeln

Nach **jeder** Antwort diese Trigger prüfen und bei Bedarf nachfragen:

**Trigger: Vage Antwort**
Signal: Enthält "irgendwie", "eigentlich", "so ähnlich wie", "ein bisschen"
→ "Kannst du das konkretisieren? Ich brauche die tatsächliche Methode — was tun die Leute heute genau?"

**Trigger: Axiom statt Dogma erkannt**
Signal: Antwort auf Frage 3 klingt wie eine unveränderliche Wahrheit, nicht wie eine Konvention
→ "Gilt das wirklich immer — oder ist das eine verbreitete Annahme die auf Gewohnheit basiert?"
→ "Ist das eingepreist (alle glauben daran, also kein Vorteil durch Befolgen) oder ist das tatsächlich eine fundamentale Wahrheit?"

**Trigger: Zu breite Domäne**
Signal: Antwort auf Frage 1 enthält mehrere unverbundene Bereiche
→ "Das sind eigentlich [N] verschiedene Probleme. Welches davon ist für dich das wichtigste für diese Session?"

**Trigger: Constraint ohne Begründung**
Signal: Constraint in Frage 5 ohne Erklärung warum
→ "Warum ist [Constraint] ausgeschlossen? Manchmal sind Constraints selbst Dogmen — es lohnt sich das zu prüfen."

**Trigger: Zieltyp unklar**
Signal: Antwort auf Frage 4 ist mehrdeutig
→ "Soll das jemand kaufen können, selbst bauen können, oder ist es ein konzeptueller Durchbruch den du weiterentwickeln willst?"

**Interview endet wenn:**
- Alle 5 Kernfragen beantwortet sind
- Keine offenen Follow-ups mehr ausstehen
- Synthesis-Check abgeschlossen und bestätigt

**Nie weitergehen wenn:** Eine Kernfrage nur vage beantwortet wurde und kein Follow-up gefolgt ist.

---

## Step 2: Interview-Synthese

Zeige dem User eine kompakte Zusammenfassung:

```
Zusammenfassung — bitte bestätigen oder korrigieren:

  Kerndomäne:        [aus Frage 1]
  Aktuelle Methode:  [aus Frage 1]
  Axiom-Kandidaten:  [aus Frage 2 — was bereits bekannt ist]
  Vermutete Dogmen:  [aus Frage 3]
  Zieltyp:           [aus Frage 4]
  Constraints:       [aus Frage 5]
  Explorer-Modus:    [A / B / C]

Stimmt das so — oder möchtest du etwas anpassen?
```

**Warte auf Bestätigung oder Korrektur.**

---

## Step 3: Coordinator-Seeding (VOR allen Dateien)

Bevor du Dateien erstellst — formuliere deine eigenen Ausgangs-Hypothesen.

**Frage dich:**
- Welche Axiome werden beim First Principles Agent wahrscheinlich auftauchen?
- Welche Dogmen klingen besonders eingepreist in dieser Domäne?
- Welche Seed-Domänen-Kombination könnte am überraschendsten sein?
- Was wäre das unerwartete aber plausible Ergebnis dieser Session?

Formuliere 3–5 Hypothesen. Diese sind NICHT für den User sichtbar —
sie werden am Ende mit den tatsächlichen Ergebnissen verglichen (Überraschungscheck).

Diese kommen später in `scratchpad/[SLUG]-coordinator-hypotheses.md`.

---

## Step 4: Cluster-Management & Slug ableiten

**Cluster-Verwaltung:**

1. Scanne `projects/` auf existierende Cluster

Falls Cluster gefunden:
```
Existierende Cluster:
  [1] [cluster-slug] — Status: Aktiv — [N] Sessions — Zuletzt: [Datum]
  [2] [cluster-slug] — ...
  [0] Neuen Cluster erstellen

Zu welchem Cluster gehört dieses Projekt?
```

2. **Warte auf Auswahl**

3a. **Existierender Cluster gewählt:**
    - Lade `projects/[cluster-slug]/axiom-library.md`
    - Lade `projects/[cluster-slug]/dogma-graveyard.md`
    - Lade `projects/[cluster-slug]/idea-outcomes.md`
    - Informiere: "Cluster [slug] enthält [N] Axiome, [N] Dogmen, [N] Ideen. Diese werden dem First Principles Agent als Kontext übergeben."

3b. **Neuer Cluster:**
    - Leite cluster-slug ab: thematisch, kein Datum, Kleinbuchstaben, Bindestriche
    - Beispiele: `trading-edge`, `ki-monetarisierung`, `orderflow-analyse`
    - Erstelle `projects/[cluster-slug]/` mit leeren Vorlagen-Dateien (project.md, axiom-library.md, dogma-graveyard.md, idea-outcomes.md)
    - Informiere: "Neuer Cluster erstellt: [cluster-slug]"

**Session-SLUG ableiten:**
Format: `YYYY-MM-DD-[kurzes-thema]-strategic`
- Datum: heute (ISO-Format)
- Thema: 2–4 Wörter, Kleinbuchstaben, Bindestriche
- Suffix: immer `-strategic` für Erkennbarkeit
- Beispiele: `2026-04-15-orderflow-edge-strategic`, `2026-05-01-ki-produkt-strategic`

Informiere den User: `Projekt-Slug: [SLUG]` und `Cluster: [cluster-slug]`

---

## Step 5: Verzeichnisstruktur erstellen

Erstelle folgende Verzeichnisse (Bash mkdir -p):

```
context/from-human/[SLUG]/
outputs/individual/[SLUG]/
prompts/queue/[SLUG]/
```

---

## Step 6: Setup-Dateien erstellen

### 6a. project-context.md

**Datei:** `context/from-human/[SLUG]/project-context.md`

**Pflichtfelder:**
- Projekt-Slug und Datum
- Cluster-Slug
- Explorer-Modus (A / B / C)
- Kerndomäne und aktuell vorherrschende Methode (aus Interview Frage 1)
- Bekannte Axiom-Kandidaten (aus Interview Frage 2 — auch wenn vage)
- Vermutete Dogmen (aus Interview Frage 3 — auch wenn nur Vermutung)
- Zieltyp (aus Interview Frage 4)
- Constraints (aus Interview Frage 5)
- Hardware/Budget/Zeitconstraints (falls genannt)
- Explizit Ausgeschlossen (aus Constraints + eventuellen Ausschlüssen)
- Falls Modus C: Referenz auf geladene Explorer-Session ([SLUG])

### 6b. research-approach.md

**Datei:** `context/from-human/[SLUG]/research-approach.md`

```markdown
# Research Approach — Strategic Innovation

## Gewählter Ansatz
Strategic Innovation

## Datum
[ISO-Datum]

## Projekt-Slug
[SLUG]

## Cluster-Slug
[cluster-slug]

## Explorer-Modus
[A — Standalone / B — Explorer-Lite / C — Explorer-Output geladen ([SLUG])]

## Modell-Zuweisungen
| Rolle | Modell |
|---|---|
| Research Coordinator | claude-sonnet-4-6 |
| First Principles Agent | claude-sonnet-4-6 |
| Domain Matrix Seeder | claude-haiku-4-5-20251001 |
| Idea Generator | claude-sonnet-4-6 |
| Advocatus Diaboli | claude-sonnet-4-6 |
| Novelty Checker | claude-haiku-4-5-20251001 |
| Deep Researcher | claude-sonnet-4-6 |
| Implementation Designer | claude-sonnet-4-6 |
| Formatter | claude-haiku-4-5-20251001 |

## Approach-Datei
`approaches/strategic-innovation.md`

---

## Session 1 — [Datum]
**Status:** In Progress
**Explorer-Modus:** [A/B/C]
**Axiome (nach Abschluss):** TBD
**Dogmen gebrochen (nach Abschluss):** TBD
**Stärkstes Experiment (nach Abschluss):** TBD
```

### 6c. strategic-plan.md

**Datei:** `prompts/queue/[SLUG]/strategic-plan.md`

```markdown
# Strategic Plan — [Thema]

## Ziel
[Aus Interview — was soll entstehen?]

## Kerndomäne & Aktuelle Methode
[Aus Interview]

## Vermutete Dogmen
[Aus Interview — auch vage Formulierungen]

## Cluster-Kontext
Cluster: [cluster-slug]
Vorhandene Axiome: [N] | Bekannte Dogmen: [N] | Ideen-Outcomes: [N]

## Explorer-Modus
[A / B / C — mit Begründung]

## Constraints
- Technisch: [aus Interview]
- Budget: [aus Interview]
- Zeit: [aus Interview]
- Ausgeschlossen: [aus Interview]

## Phase-Sequenz
- [ ] Phase 0: Cluster-Memory laden ✓ (abgeschlossen)
- [ ] Phase 1: First Principles Agent
- [ ] Phase 2: Domain Matrix Seeder
- [ ] Phase 3: Idea Generator
- [ ] Phase 4: Advocatus Diaboli
- [ ] Phase 5: Novelty Checker
- [ ] Phase 6: Deep Researcher
- [ ] Phase 7: Implementation Designer
- [ ] Phase 8: Formatter
- [ ] Phase 9: Cluster-Memory Update

## Deliverables-Checkliste
[Aus approaches/strategic-innovation.md — vollständig übernehmen]
```

### 6d. research-log.md

**Datei:** `notes/[SLUG]-research-log.md`

Initialisiere mit:
- Projekt-Slug, Cluster, Datum, Ziel
- Explorer-Modus
- Phase-Status-Tabelle (alle 9 Phasen als "⬜ Pending")
- Checkpoint-0-Eintrag (Setup abgeschlossen)

### 6e. coordinator-hypotheses.md

**Datei:** `scratchpad/[SLUG]-coordinator-hypotheses.md`

Schreibe die 3–5 Coordinator-Hypothesen aus Step 3.

Format pro Hypothese:
```markdown
### CH[N]: [Kurztitel]
**Hypothese:** [Was vermutet der Coordinator?]
**Basis:** [Worauf basiert diese Vermutung?]
**Überraschungspotenzial:** [Warum wäre das interessant wenn es stimmt?]
```

---

## Step 7: Approach-Datei lesen

Lese `approaches/strategic-innovation.md` vollständig (falls nicht bereits geschehen).
Diese Datei definiert alle Sub-Agent-Prompts und die Orchestrierungs-Sequenz.

---

## Step 8: Recherche starten

Frage den User:

```
Setup abgeschlossen. Strategic-Innovation-Projekt bereit.

  Slug:          [SLUG]
  Cluster:       [cluster-slug] ([N] Axiome, [N] Dogmen im Gedächtnis)
  Explorer-Modus: [A — Standalone / B — Explorer-Lite abgeschlossen / C — Explorer-Output geladen]
  Phasen:        First Principles → Domain Seeder → Idea Generator → Advocatus Diaboli →
                 Novelty Check → Deep Researcher → Implementation Designer → Formatter
  Kerndomäne:    [kurze Beschreibung]
  Constraints:   [wichtigste Constraints in 1 Zeile]

Soll ich jetzt starten — oder möchtest du den Plan erst reviewen?
```

**Bei "starten":**
Führe die Orchestrierungs-Sequenz aus `approaches/strategic-innovation.md` aus.

**Checkpoint-Protokoll (nach JEDER Phase):**
```markdown
### Checkpoint [N] — [Phase Name] — [Datum]
Status: COMPLETE
Output: [Dateipfad]
Key Findings (2-3 Bullets):
- [finding]
Nächste Phase: [Name]
```

Checkpoint sofort nach Phasen-Abschluss in `notes/[SLUG]-research-log.md` schreiben.

**Bei "reviewen":**
Zeige `prompts/queue/[SLUG]/strategic-plan.md`, nimm Änderungen an, dann starten.

---

## Step 9: Session-Abschluss

Am Ende oder bei natürlichem Haltepunkt:

1. **Coordinator-Vergleich**: Lies `scratchpad/[SLUG]-coordinator-hypotheses.md`.
   Welche Hypothesen haben die Recherche antizipiert? Was war überraschend?
   Schreibe kurzen Vergleich in den Scratchpad.

2. **Cluster-Memory finalisieren** (Phase 9 der Approach-Datei ausführen):
   - `axiom-library.md` finalisieren (Tentativ → Bestätigt wo gerechtfertigt)
   - `dogma-graveyard.md` finalisieren
   - `idea-outcomes.md` finalisieren (Novelty-Check-Urteile eintragen)
   - `project.md` Session-Zeile hinzufügen
   - `innovation_seeds.md` Tracking-Ergebnis aktualisieren (gut/schwach/neutral)

3. **Research-Log abschließen**: Alle Phasen auf COMPLETE setzen

4. **research-approach.md Session-Block updaten:**
   ```markdown
   ## Session 1 — [Datum]
   Status: COMPLETE
   Explorer-Modus: [A/B/C]
   Axiome: [N neue] — wichtigste: [A1 Kurztitel]
   Dogmen gebrochen: [N] — wichtigstes: [D1 Kurztitel]
   Seed-Domänen: [Domäne 1] + [Domäne 2]
   Ideen: [N generiert] → [N überlebt Advocatus] → [N überlebt Novelty-Check]
   Stärkstes Experiment: [E1-Titel]
   Alpha-Vorteil: [Kurzform]
   Nächste Session: [Empfehlung]
   Cluster-Memory: [N] Axiome, [N] Dogmen, [N] Ideen aktualisiert
   ```

5. **Dem User mitteilen:**
   - Stärkstes Experiment + Alpha-Vorteil
   - Was der Advocatus zerstört hat (und warum das wertvoll ist)
   - Was den Coordinator überrascht hat vs. was erwartet war
   - Empfehlung für die nächste Session

---

## Während der gesamten Session

- Jeder Phasen-Abschluss = sofort Checkpoint schreiben (Session-Limit-Schutz)
- Falls Session terminiert: neue Session liest `notes/[SLUG]-research-log.md` und
  `context/from-human/[SLUG]/research-approach.md` → resume ab letztem Checkpoint
- Cluster-Memory progressiv schreiben (nicht nur am Ende):
  Nach Phase 1, nach Phase 2, nach Phase 4 — nicht auf Phase 9 warten
- Konfidenz-Kennzeichnung bei allen Outputs: Hoch / Mittel / Niedrig / Spekulativ

---

**Beginne jetzt mit Step 0 (Bestandsprüfung) und dann Step 0.5 (Explorer-Check).**
