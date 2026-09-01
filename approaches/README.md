# Research Approaches

Dieses Verzeichnis enthält wiederverwendbare Ansatz-Templates, die festlegen wie Claude eine Recherche durchführt. Der passende Ansatz wird während `/initiate-research` automatisch empfohlen und kann jederzeit manuell überschrieben werden.

## Verfügbare Ansätze

| Datei | Ansatz | Am besten für |
|---|---|---|
| `single-agent-deep-dive.md` | Single-Agent Deep Dive | 1–2 Domänen, fokussiert, kein Adversarial nötig |
| `multi-agent-adversarial.md` | Multi-Agent Adversarial | High-Stakes, Gegenprüfung gewünscht |
| `cross-domain-synthesis.md` | Cross-Domain Synthesis | 3+ Domänen, Verbindungen zwischen Feldern gesucht |
| `generative-explorer.md` | Generative Explorer | Neue Möglichkeiten entdecken, Hypothesen entwickeln, Experimente designen |
| `strategic-innovation.md` | Strategic Innovation | Axiomatisches Erstprinzipiendenken + Dogmen-Dekonstruktion — genuine neue Ideen aus Grundsätzen, nicht Frontier-Dokumentation |
| `custom-approach-template.md` | — | Skeleton für eigene Ansätze |

## Assessment-Kriterien

Claude bewertet nach dem Interview 5 Dimensionen und wählt den Ansatz per folgender Logik:

```
WENN Ziel ist axiomatisches Grundsatzdenken / Dogmen brechen / genuine neue Mechaniken:
    → strategic-innovation

SONST WENN Ziel ist neue Möglichkeiten entdecken / Hypothesen entwickeln / Explorer-Modus:
    → generative-explorer

SONST WENN Domänen >= 3 UND Cross-Domain-Synthese systematisch gewünscht:
    → cross-domain-synthesis

SONST WENN Stakes hoch ODER Adversarial-Prüfung gewünscht:
    → multi-agent-adversarial

SONST WENN Zeitdruck dringend:
    → single-agent-deep-dive

SONST:
    → single-agent-deep-dive  (sicherer Default)
```

**Dimensionen im Detail:**

| Dimension | Signal im Interview | Schwellwert |
|---|---|---|
| Innovation-Modus | Formulierung, Ziele | "axiom", "grundsatz", "was ist wirklich wahr", "dogma", "genuinely new", "erste prinzipien", "was ist wirklich eingepreist" |
| Explorer-Modus | Ziele, Formulierung | "neue Möglichkeiten", "was können wir bauen", "kreativ", "über den Tellerrand" |
| Domänen-Anzahl | Thema, Scope-Antwort | ≥ 3 distinct Wissensfelder |
| Stakes | Objektive, Verwendungszweck | Output ist Entscheidungsgrundlage mit hohen Konsequenzen |
| Cross-Domain | Ziele, Output-Format | Verbindungen *zwischen* Feldern sind das Ziel, nicht nur parallele Recherche |
| Zeitdruck | Timeline | Tage statt Wochen/offen |

## Modell-Zuweisungen

Alle Ansätze verwenden folgende Modell-Strategie:

| Rolle | Modell | Begründung |
|---|---|---|
| Research Coordinator | `claude-sonnet-4-6` | Orchestrierung braucht Urteilsvermögen |
| Domain Researcher | `claude-sonnet-4-6` | Analyse-Tiefe entscheidend |
| Adversarial Critic | `claude-sonnet-4-6` | Muss nicht-offensichtliche Lücken finden |
| Cross-Domain Synthesizer | `claude-sonnet-4-6` | Wertvollste kreative Aufgabe |
| Source Gatherer / Web Research | `claude-haiku-4-5-20251001` | Mechanische, gut definierte Aufgabe |
| Formatter / File Manager | `claude-haiku-4-5-20251001` | Rein strukturell |

## Session-Persistenz

Nach Approach-Auswahl schreibt Claude `context/from-human/research-approach.md` mit:
- Gewähltem Ansatz und Datum
- Welche Kriterien getriggert haben
- Modell-Zuweisungen
- Referenz auf diese Approach-Datei

Diese Datei wird in Folge-Sessions automatisch gelesen, damit der Ansatz konsistent bleibt.

## Eigenen Ansatz erstellen

1. `approaches/custom-approach-template.md` kopieren
2. Alle Abschnitte ausfüllen (keiner ist optional)
3. Datei in `approaches/` speichern
4. Claude anweisen: "Nutze den Ansatz in `approaches/[dateiname].md`"

Alternativ: Claude kann auf Basis einer Beschreibung automatisch eine neue Approach-Datei generieren.

## Hinweis zur Selbst-Enthaltung

Jede Approach-Datei ist so geschrieben, dass sie auch ohne `CLAUDE.md` im Kontext funktioniert. Wenn Claude nur die Approach-Datei liest, hat er alle nötigen Informationen zur Ausführung.

## Cluster-System (Strategic Innovation)

Der `strategic-innovation.md` Ansatz nutzt ein persistentes Cluster-Memory-System unter `projects/`. Clusters speichern Axiome, Dogmen und Ideen-Ergebnisse über Sessions hinweg, sodass jede Folge-Session auf akkumuliertem Wissen aufbaut statt von Null zu starten.

→ Vollständige Dokumentation: `projects/README.md`
