# Initiate Generative Explorer Project

Du startest ein Generative-Explorer-Projekt. Das Ziel ist nicht, zu dokumentieren was bereits
existiert — sondern neue Möglichkeiten zu entdecken, Hypothesen zu entwickeln und konkrete
Experimente zu designen. Spekulieren ist ausdrücklich erlaubt wenn als solches gekennzeichnet.

Lese zunächst `approaches/generative-explorer.md` vollständig — diese Datei definiert
die Orchestrierung für alle Schritte dieses Commands.

---

## Step 0: Bestehende Inhalte prüfen

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
   - **A**: Archivieren nach `context/from-history/[slug]/`, dann weiter mit Step 1
   - **B**: Löschen nach Bestätigung, dann weiter mit Step 1
   - **C**: Direkt weiter mit Step 1

5. **Falls keine Inhalte gefunden**: Direkt weiter mit Step 1

---

## Step 1: Explorer-Interview

Das Interview für diesen Modus ist anders als bei `/initiate-research`.
Die Fragen zielen auf Entdeckung, nicht auf Dokumentation.

**Stelle folgende Fragen:**

1. **Thema & Ausgangspunkt**: Was ist das Thema — und was weißt du bereits darüber?
   *(Nicht: "Was willst du wissen?" — sondern: "Was ist die Grenze deines Wissens wo es interessant wird?")*

2. **Entdeckungsziel**: Was erhoffst du dir zu entdecken, entwickeln oder kombinieren?
   Was wäre das aufregendste Ergebnis dieser Exploration?

3. **Ausgangs-Hypothesen**: Hast du schon Ideen oder Vermutungen die du testen möchtest?
   *(Auch vage oder spekulative Gedanken sind wertvoll — das ist kein Problem.)*

4. **Domänen & Verbindungen**: Welche Felder oder Bereiche sollen einbezogen werden?
   Gibt es Bereiche die du explizit ausschließen möchtest?

5. **Technologien & Tools**: Welche aktuellen Tools, Frameworks oder Modelle sollen
   berücksichtigt werden? Gibt es spezifische neue Entwicklungen die du berücksichtigt
   haben möchtest?

6. **Umsetzbarkeit**: Was soll am Ende konkret nutzbar oder baubar sein?
   Gibt es Hardware-, Budget- oder Zeitconstraints die relevant sind?

7. **Recency-Modus**: Wie sollen Quellen gewichtet werden?
   - Standard: Neueres bevorzugt, Älteres wenn relevant *(Modus A — Default)*
   - Recency-Strong: Mindestens 80% der Quellen aus den letzten 6 Monaten *(Modus B)*

8. **Konfidenz-Toleranz**: Wie spekulativ darf es werden?
   Sollen nur gut belegte Ansätze im Output erscheinen — oder auch
   "vielversprechend aber ungetestet" und "reine Hypothese"?

---

## Step 1.5: Recency-Modus & Konfidenz-Toleranz festhalten

Aus den Antworten auf Fragen 7 und 8:

- **Recency-Modus**: A (Default) oder B (Strong) → ins project-context.md übernehmen
- **Konfidenz-Toleranz**: "Nur belegt" / "Belegt + Hypothetisch" / "Alles inkl. Spekulativ"
  → ins project-context.md übernehmen — bestimmt wie der Hypothesis Generator filtert

Informiere den User kurz:
```
Recency-Modus: [A — Standard-Gewichtung / B — Recency-Strong (80% <6 Monate)]
Konfidenz-Toleranz: [Nur belegt / Belegt + Hypothetisch / Alles inkl. Spekulativ]
```

---

## Step 2: Koordinator-Hypothesen-Seeding (VOR allen Dateien)

Bevor du irgendwelche Dateien erstellst — formuliere deine eigenen Ausgangs-Hypothesen.

**Frage dich:**
- Was klingt aus den Interview-Antworten besonders vielversprechend?
- Welche Verbindungen zwischen genannten Domänen sind nicht offensichtlich?
- Was fehlt wahrscheinlich in der bekannten Literatur zu diesem Thema?
- Was wäre das überraschendste aber plausible Ergebnis?

Formuliere 3–5 Hypothesen. Diese sind NICHT für den User sichtbar im Setup —
sie werden erst am Ende mit den generierten Hypothesen verglichen (Überraschungscheck).

Diese Hypothesen kommen später in `scratchpad/[SLUG]-coordinator-hypotheses.md`.

---

## Step 3: Projekt-Slug ableiten

Format: `YYYY-MM-DD-[kurzes-thema]`
- Datum: heute (ISO-Format)
- Thema: 2–4 Wörter, Kleinbuchstaben, Bindestriche statt Leerzeichen, keine Sonderzeichen
- Beispiele: `2026-03-30-agentic-trading-explorer`, `2026-04-10-musik-ki-monetarisierung`

Informiere den User: `Projektordner: [SLUG]`

---

## Step 4: Verzeichnisstruktur erstellen

Erstelle folgende Verzeichnisse (Bash mkdir -p):

```
context/from-human/[SLUG]/
context/from-internet/
outputs/individual/[SLUG]/          ← für hypothesis-catalogue + experiment-designs
prompts/queue/[SLUG]/
```

Domänen-Verzeichnisse (aus Interview-Antwort 4):
```
outputs/individual/[domäne-1]/
outputs/individual/[domäne-2]/
[weitere je nach Anzahl der Domänen]
```

---

## Step 5: Setup-Dateien erstellen

### 5a. project-context.md

**Datei**: `context/from-human/[SLUG]/project-context.md`

**Pflichtfelder:**
- Thema und Entdeckungsziel (aus Interview 1+2)
- Ausgangs-Hypothesen des Users (aus Interview 3) — auch wenn vage
- Domänen-Liste mit Slugs (aus Interview 4)
- Technologien/Tools die berücksichtigt werden sollen (aus Interview 5)
- Umsetzbarkeits-Constraints: Hardware, Budget, Zeit (aus Interview 6)
- **Recency-Modus**: A oder B (aus Step 1.5)
- **Konfidenz-Toleranz**: Einstellung (aus Step 1.5)
- Projekt-Slug: `[SLUG]`
- Was explizit ausgeschlossen ist

### 5b. research-approach.md

**Datei**: `context/from-human/[SLUG]/research-approach.md`

```markdown
# Research Approach — Generative Explorer

## Gewählter Ansatz
Generative Explorer

## Datum
[ISO-Datum]

## Projekt-Slug
[SLUG]

## Recency-Modus
[A — Standard / B — Strong (80% <6 Monate)]

## Konfidenz-Toleranz
[Nur belegt / Belegt + Hypothetisch / Alles inkl. Spekulativ]

## Identifizierte Domänen
[Liste mit Slugs]

## Modell-Zuweisungen
| Rolle | Modell |
|---|---|
| Research Coordinator | claude-sonnet-4-6 |
| Web Researcher (Recency-Fokus) | claude-haiku-4-5-20251001 |
| Domain Researcher × [N] | claude-sonnet-4-6 |
| Hypothesis Generator | claude-sonnet-4-6 |
| Experiment Designer | claude-sonnet-4-6 |
| Formatter | claude-haiku-4-5-20251001 |

## Approach-Datei
`approaches/generative-explorer.md`

---

## Session 1 — [Datum]
**Status:** In Progress
**Agents geplant:** [Liste]
**Stärkste Coordinator-Hypothesen (nach Abschluss):** [TBD]
**Top-Experimente (nach Abschluss):** [TBD]
```

### 5c. explorer-plan.md

**Datei**: `prompts/queue/[SLUG]/explorer-plan.md`

```markdown
# Explorer Plan — [Thema]

## Entdeckungsziel
[Aus Interview]

## Domänen (mit Spawn-Reihenfolge)
1. [Domäne 1] — Slug: [slug]
2. [Domäne 2] — Slug: [slug]
[...]

## Agent-Spawn-Sequenz
- [ ] Web Researcher (Haiku) — Modus [A/B]
- [ ] Domain Researcher: [domäne-1]
- [ ] Domain Researcher: [domäne-2]
[...]
- [ ] Hypothesis Generator
- [ ] Experiment Designer
- [ ] Formatter

## Fokus-Fragen pro Domäne
### [Domäne 1]
- [Frage 1]
- [Frage 2]

[Für jede Domäne]

## Ausgangs-Hypothesen des Users
[Aus Interview — auch vage Formulierungen]

## Constraints
- Hardware: [aus Interview]
- Budget: [aus Interview]
- Konfidenz-Toleranz: [Einstellung]

## Deliverables-Checkliste
- [ ] context/from-internet/sources-[DATUM].md
- [ ] outputs/individual/[domäne-x]/YYYY-MM-DD-[domäne]-findings.md (× N)
- [ ] outputs/individual/[SLUG]/hypothesis-catalogue.md
- [ ] outputs/individual/[SLUG]/experiment-designs.md
- [ ] outputs/aggregated/mk-combined/[DATUM]-[SLUG]-explorer-report.md
```

### 5d. research-log.md

**Datei**: `notes/[SLUG]-research-log.md`

Initialisiere mit:
- Projekt-Slug, Datum, Entdeckungsziel
- Agent-Status-Tabelle (alle Agents als "⬜ Pending")
- Checkpoint-0-Eintrag (Setup abgeschlossen)

### 5e. coordinator-hypotheses.md

**Datei**: `scratchpad/[SLUG]-coordinator-hypotheses.md`

Schreibe die 3–5 Coordinator-Hypothesen aus Step 2 hier hinein.
Format pro Hypothese:

```markdown
### CH[N]: [Kurztitel]
**Hypothese:** [Was vermutet der Coordinator?]
**Basis:** [Worauf basiert diese Vermutung?]
**Überraschungspotenzial:** [Warum wäre das interessant wenn es stimmt?]
```

---

## Step 6: Approach-Datei lesen

Lese `approaches/generative-explorer.md` vollständig (falls nicht bereits geschehen).
Diese Datei definiert alle Sub-Agent-Prompts und die Orchestrierungs-Sequenz.

---

## Step 7: Recherche starten

Frage den User:

```
Setup abgeschlossen. Explorer-Projekt bereit.

  Slug:      [SLUG]
  Domänen:   [N] ([liste])
  Recency:   [Modus A/B]
  Konfidenz: [Toleranz-Einstellung]
  Agents:    Web Researcher → [N]× Domain → Hypothesis Generator → Experiment Designer → Formatter

Soll ich jetzt starten — oder möchtest du den Plan erst reviewen?
```

**Bei "starten":**
Führe die Orchestrierungs-Sequenz aus `approaches/generative-explorer.md` aus:
1. Web Researcher spawnen (Haiku, Recency-Modus beachten)
2. Nach jedem Agent: Checkpoint in `notes/[SLUG]-research-log.md` schreiben
3. Domain Researchers sequenziell spawnen — jeder mit Explorer-Sektion
4. Hypothesis Generator spawnen
5. Experiment Designer spawnen
6. Coordinator Review
7. Formatter spawnen

**Checkpoint-Protokoll (nach JEDEM Agent):**
```markdown
### Checkpoint [N] — [Agent Name] — [Datum]
Status: COMPLETE
Output: [Dateipfad]
Key Findings (2-3 Bullets):
- [finding]
Nächster Agent: [Name]
```

**Bei "reviewen":**
Zeige `prompts/queue/[SLUG]/explorer-plan.md`, nimm Änderungen an, dann starten.

---

## Step 8: Session-Abschluss

Am Ende oder bei natürlichem Haltepunkt:

1. **Coordinator-Vergleich**: Lies `scratchpad/[SLUG]-coordinator-hypotheses.md`.
   Welche Coordinator-Hypothesen wurden bestätigt, widerlegt, überraschend erweitert?
   Schreibe kurzen Vergleich in den Scratchpad.

2. **Research-Log abschließen**: Session-Status updaten

3. **research-approach.md updaten**:
   ```markdown
   ## Session 1 — [Datum]
   Status: COMPLETE
   Stärkste Hypothesen: [Top 3]
   Top-Experiment: [#1]
   Coordinator-Überraschungen: [Was war unerwartet?]
   Nächste Session: [Experimente ausführen? Weitere Domänen? Deep Dive?]
   ```

4. **Dem User mitteilen:**
   - Top-3-Hypothesen aus dem Katalog
   - Priorisiertes Experiment (#1 mit nächstem konkreten Schritt)
   - Was überraschend war vs. erwartet

---

## Während der gesamten Exploration

- Jeder Agent-Abschluss = sofort Checkpoint schreiben (Session-Limit-Schutz)
- Falls Session terminiert: neue Session liest `notes/[SLUG]-research-log.md` und
  `context/from-human/[SLUG]/research-approach.md` → resume ab letztem Checkpoint
- Konfidenz-Kennzeichnung bei ALLEN Hypothesen: Hoch / Mittel / Niedrig / Spekulativ
- `[FRONTIER]`-Tag für Quellen ohne Peer-Review aber aktiv in der Community genutzt
- `[OLDER-FOUNDATION]`-Tag (nur Modus B) für ältere Quellen mit Pflichtbegründung

---

**Beginne jetzt mit Step 0 (Bestandsprüfung) und dann Step 1 (Explorer-Interview).**
