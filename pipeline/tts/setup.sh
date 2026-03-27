#!/usr/bin/env bash
# setup.sh — TTS Audio Pipeline Setup
# Erstellt Conda-Env, installiert System-Dependencies, lädt Piper-Modelle herunter.
# Verwendung: bash pipeline/tts/setup.sh
# Voraussetzung: Homebrew installiert

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
VOICES_DIR="$HOME/.local/share/piper-voices"
ENV_NAME="research-audio"

echo "=== TTS Audio Pipeline Setup ==="
echo "Repo: $REPO_ROOT"
echo "Voices: $VOICES_DIR"
echo ""

# ── Schritt 1: Homebrew prüfen ──────────────────────────────────────────────
echo "[1/5] Homebrew prüfen..."
if ! command -v brew &>/dev/null; then
    echo "FEHLER: Homebrew nicht gefunden."
    echo "       Bitte installieren: https://brew.sh"
    exit 1
fi
echo "      OK ($(brew --version | head -1))"

# ── Schritt 2: System-Dependencies via Homebrew ─────────────────────────────
echo "[2/5] espeak-ng + ffmpeg installieren..."
HOMEBREW_NO_AUTO_UPDATE=1 brew install espeak-ng ffmpeg
echo "      OK"

# ── Schritt 3: Conda-Env erstellen oder aktualisieren ───────────────────────
echo "[3/5] Conda-Env '$ENV_NAME' einrichten..."
if ! command -v conda &>/dev/null; then
    echo "FEHLER: conda nicht gefunden. Bitte Anaconda/Miniconda installieren."
    exit 1
fi

if conda env list | grep -q "^$ENV_NAME "; then
    echo "      Env existiert bereits — aktualisiere..."
    conda env update --name "$ENV_NAME" --file "$SCRIPT_DIR/environment.yml" --prune
else
    echo "      Erstelle neues Env..."
    conda env create -f "$SCRIPT_DIR/environment.yml"
fi
echo "      OK"

# ── Schritt 4: libstdcxx-ng — Pflicht für piper-tts auf Intel-Mac ───────────
echo "[4/5] libstdcxx-ng installieren (verhindert GLIBCXX-Fehler)..."
conda run -n "$ENV_NAME" conda install -c conda-forge libstdcxx-ng -y 2>/dev/null || true
echo "      OK"

# ── Schritt 5: Piper-Modelle herunterladen ───────────────────────────────────
echo "[5/5] Piper-Stimmen herunterladen nach $VOICES_DIR..."
mkdir -p "$VOICES_DIR"

HF_BASE="https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0"

download_if_missing() {
    local dest="$1"
    local url="$2"
    if [ -f "$dest" ] && [ "$(wc -c < "$dest")" -gt 1000 ]; then
        echo "      $(basename "$dest") — bereits vorhanden, überspringe"
    else
        echo "      Lade $(basename "$dest") herunter..."
        curl -L --progress-bar -o "$dest" "$url"
    fi
}

download_if_missing "$VOICES_DIR/de_DE-thorsten-high.onnx" \
    "$HF_BASE/de/de_DE/thorsten/high/de_DE-thorsten-high.onnx"
download_if_missing "$VOICES_DIR/de_DE-thorsten-high.onnx.json" \
    "$HF_BASE/de/de_DE/thorsten/high/de_DE-thorsten-high.onnx.json"
download_if_missing "$VOICES_DIR/de_DE-thorsten_emotional-medium.onnx" \
    "$HF_BASE/de/de_DE/thorsten_emotional/medium/de_DE-thorsten_emotional-medium.onnx"
download_if_missing "$VOICES_DIR/de_DE-thorsten_emotional-medium.onnx.json" \
    "$HF_BASE/de/de_DE/thorsten_emotional/medium/de_DE-thorsten_emotional-medium.onnx.json"

echo ""
echo "=== Setup abgeschlossen ==="
echo ""
echo "Nächste Schritte:"
echo "  conda activate $ENV_NAME"
echo ""
echo "Piper-Schnelltest:"
echo "  echo 'Hallo, das ist ein Test.' | piper \\"
echo "    --model $VOICES_DIR/de_DE-thorsten-high.onnx \\"
echo "    --output_file /tmp/piper_test.wav && afplay /tmp/piper_test.wav"
echo ""
echo "Audio generieren:"
echo "  conda run -n $ENV_NAME python pipeline/tts/generate_audio.py --latest --mode tts --dry-run"
