# /generate-audio — Audio aus Research-Report generieren

Du bist der Audio-Generierungs-Assistent für das Deep Research Repository.

## Schritt 1: Report finden

Liste alle .md-Dateien in `outputs/aggregated/mk-combined/` (Bash: `ls outputs/aggregated/mk-combined/*.md 2>/dev/null`).
- Keine Datei gefunden → "Kein Report vorhanden. Führe zuerst /initiate-research aus."
- Genau eine Datei → direkt verwenden, kurz nennen
- Mehrere Dateien → Liste ausgeben, User wählen lassen

## Schritt 2: Modus wählen

Frage:
"Welches Audio-Format?
  (1) TTS — lineare Narration, ~15-40 Min Generierung, schnell zum Hören
  (2) Podcast — Zwei-Sprecher-Dialog, ~30-60 Min Generierung, unterhaltsamer"

## Schritt 3: Conda-Env prüfen

Prüfe ob `research-audio` existiert: `conda info --envs`

- Env fehlt → "Bitte zuerst einrichten: `bash pipeline/tts/setup.sh`"
- Env vorhanden → weiter (conda run übernimmt die Aktivierung)

## Schritt 4: Skript ausführen

Verwende `conda run -n research-audio` damit das Env nicht manuell aktiviert werden muss.

Für TTS:
```
conda run -n research-audio python pipeline/tts/generate_audio.py \
    --input [AUFGELÖSTER_PFAD] \
    --mode tts \
    --backend piper \
    --pause 45
```

Für Podcast:
```
conda run -n research-audio python pipeline/tts/generate_audio.py \
    --input [AUFGELÖSTER_PFAD] \
    --mode podcast \
    --backend piper \
    --pause 45
```

Für Dry-Run (Vorschau ohne Synthese):
```
conda run -n research-audio python pipeline/tts/generate_audio.py \
    --input [AUFGELÖSTER_PFAD] \
    --dry-run
```

## Schritt 5: Ergebnis melden

Parse die `[DONE]`-Zeile aus dem Skript-Output:
- Dateipfad
- Dauer in Minuten
- Dateigröße in MB

Melde das Ergebnis und wie die Datei angehört werden kann: `afplay [PFAD]`

## Fehler-Behandlung

- Exit Code 1: Falsches Conda-Env → "Aktiviere mit: conda activate research-audio"
- Exit Code 2: Modell fehlt → Zeige den curl-Befehl aus dem Skript-Output
- Exit Code 3: Zu wenig RAM → "Schließe andere Anwendungen und versuche es erneut"

## Hinweise

- Thermal Throttling: Das MacBook Pro 2014 pausiert 45s zwischen Chunks — das ist normal
- Podcast-Modus erstellt automatisch ein Skript in scratchpad/podcast-scripts/ das wiederverwendet wird
- Andere Stimme testen: `--voice de_DE-thorsten_emotional-medium`
- Anderes Backend testen: `--backend kokoro` (zeigt hilfreiche Fehlermeldung mit Implementierungshinweis)
