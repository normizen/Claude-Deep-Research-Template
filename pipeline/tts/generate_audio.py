"""
generate_audio.py — TTS Audio-Generierung aus Markdown Research-Reports.

Verwendung:
    # TTS-Modus (schnell):
    conda run -n research-audio python pipeline/tts/generate_audio.py --latest --mode tts

    # Podcast-Modus (Dialog):
    conda run -n research-audio python pipeline/tts/generate_audio.py --latest --mode podcast

    # Dry-Run (zeigt Chunks, keine Synthese):
    conda run -n research-audio python pipeline/tts/generate_audio.py --latest --dry-run

    # Spezifische Datei:
    conda run -n research-audio python pipeline/tts/generate_audio.py \\
        --input outputs/aggregated/mk-combined/REPORT.md --mode tts
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional

# ffmpeg-Pfad für pydub explizit setzen (findet es sonst nicht aus Conda-Env)
try:
    from pydub import AudioSegment
    AudioSegment.converter = "/usr/local/bin/ffmpeg"
    AudioSegment.ffprobe   = "/usr/local/bin/ffprobe"
except ImportError:
    pass  # Wird später mit klarer Fehlermeldung abgefangen

REPO_ROOT = Path(__file__).parent.parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT))


# ── Guard-Funktionen ─────────────────────────────────────────────────────────

def check_conda_env() -> None:
    env = os.environ.get("CONDA_DEFAULT_ENV", "")
    if env != "research-audio":
        print(f"[FEHLER] Falsches Conda-Environment: '{env}'")
        print("         Aktiviere mit: conda activate research-audio")
        print("         Oder starte mit: conda run -n research-audio python ...")
        sys.exit(1)


def check_backend_availability(backend) -> None:
    if not backend.is_available():
        print(f"[FEHLER] Backend '{backend.get_name()}' nicht verfügbar.")
        if hasattr(backend, "model_path"):
            print(f"         Modell nicht gefunden: {backend.model_path}")
            print(f"         Download-Befehl:")
            name = backend.model_path.name
            url = f"https://github.com/rhasspy/piper-voices/releases/download/v1.0.0/{name}"
            print(f"         mkdir -p ~/.local/share/piper-voices && curl -L -o ~/.local/share/piper-voices/{name} {url}")
        sys.exit(2)


def check_dependencies() -> None:
    missing = []
    try:
        from pydub import AudioSegment  # noqa: F401
    except ImportError:
        missing.append("pydub")
    try:
        import psutil  # noqa: F401
    except ImportError:
        missing.append("psutil")
    if missing:
        print(f"[FEHLER] Fehlende Packages: {', '.join(missing)}")
        print("         Führe 'bash pipeline/tts/setup.sh' aus.")
        sys.exit(1)


# ── Input-Auflösung ──────────────────────────────────────────────────────────

def resolve_input(args: argparse.Namespace) -> Path:
    if args.input:
        p = Path(args.input)
        if not p.exists():
            print(f"[FEHLER] Datei nicht gefunden: {p}")
            sys.exit(1)
        return p
    if args.latest:
        mk_dir = REPO_ROOT / "outputs" / "aggregated" / "mk-combined"
        candidates = [
            f for f in sorted(mk_dir.glob("*.md"), key=lambda x: x.stat().st_mtime, reverse=True)
            if f.name != ".gitkeep"
        ]
        if not candidates:
            print(f"[FEHLER] Keine .md-Dateien in {mk_dir}")
            sys.exit(1)
        return candidates[0]
    print("[FEHLER] --input DATEI oder --latest angeben.")
    sys.exit(1)


# ── Hilfsfunktionen ──────────────────────────────────────────────────────────

def save_tts_safe_text(input_path: Path, chunks: list[tuple[str, str]]) -> Path:
    """Speichert bereinigten Text als Audit-Trail."""
    out_dir = REPO_ROOT / "outputs" / "reformatted" / "tts-safe-txt"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{input_path.stem}.txt"
    full_text = "\n\n---\n\n".join(
        f"[{title}]\n{text}" for title, text in chunks
    )
    out_path.write_text(full_text, encoding="utf-8")
    return out_path


def concatenate_wav_files(wav_paths: list[Path]) -> "AudioSegment":
    from pydub import AudioSegment
    segments = [AudioSegment.from_wav(str(p)) for p in wav_paths]
    combined = segments[0]
    for seg in segments[1:]:
        combined = combined + seg
    return combined


def normalize_audio(audio: "AudioSegment", target_dbfs: float = -18.0) -> "AudioSegment":
    delta = target_dbfs - audio.dBFS
    return audio.apply_gain(delta)


def assemble_podcast(wav_paths: list[Path], silence_ms: int = 300) -> "AudioSegment":
    from pydub import AudioSegment
    silence = AudioSegment.silent(duration=silence_ms)
    segments = [AudioSegment.from_wav(str(p)) for p in wav_paths]
    # Sample-Raten angleichen (thorsten-high vs emotional können abweichen)
    target_rate = segments[0].frame_rate
    segments = [s.set_frame_rate(target_rate) for s in segments]
    combined = segments[0]
    for seg in segments[1:]:
        combined = combined + silence + seg
    return combined


def find_existing_script(input_path: Path) -> Optional[Path]:
    script_path = REPO_ROOT / "scratchpad" / "podcast-scripts" / f"{input_path.stem}-podcast-script.txt"
    return script_path if script_path.exists() else None


def parse_speaker_turns(script_text: str) -> list[tuple[str, str]]:
    turns: list[tuple[str, str]] = []
    for line in script_text.splitlines():
        line = line.strip()
        if line.startswith("HOST_A:"):
            turns.append(("HOST_A", line[len("HOST_A:"):].strip()))
        elif line.startswith("HOST_B:"):
            turns.append(("HOST_B", line[len("HOST_B:"):].strip()))
    if not turns:
        raise ValueError(
            "Keine Sprecher-Turns gefunden. "
            "Skript muss Zeilen mit 'HOST_A:' oder 'HOST_B:' enthalten."
        )
    return turns


def generate_podcast_script_via_api(raw_md: str, input_path: Path) -> Path:
    """Generiert Podcast-Skript via Claude API (Two-Pass)."""
    try:
        import anthropic
    except ImportError:
        print("[FEHLER] anthropic-Package nicht installiert.")
        print("         pip install anthropic")
        sys.exit(1)

    print("[INFO] Generiere Podcast-Skript via Claude API (Two-Pass)...")
    client = anthropic.Anthropic()

    pass1_prompt = f"""Du bist Podcast-Autor. Schreibe ein deutsches Podcast-Skript aus diesem Research-Report.

Sprecher:
HOST_A (Moderatorin): Neugierig, stellt Fragen, verbindet mit dem Hörer
HOST_B (Experte): Erklärt Findings, nutzt Beispiele, ist direkt und präzise

Plane zuerst in einem <scratchpad>-Block:
1. Die 3 wichtigsten Findings des Reports
2. Die beste Analogie für das Kernthema
3. Was ein neugieriger Laie zuerst fragen würde
4. Der "Wow-Moment" — die überraschendste Erkenntnis
5. Eine praktische Handlungsempfehlung für den Hörer

Dann schreibe das Rohskript. Regeln:
- Jede Zeile beginnt mit HOST_A: oder HOST_B:
- Kein Markdown, keine Bühnenanweisungen, keine Abschnittstitel
- Natürliche Umgangssprache, kein Akademiker-Deutsch
- Ziel: 1500-2000 Wörter für den kompletten Report

Report:
{raw_md}"""

    print("  Pass 1: Rohskript...")
    msg1 = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{"role": "user", "content": pass1_prompt}],
    )
    raw_script = msg1.content[0].text

    pass2_prompt = f"""Überarbeite dieses Podcast-Skript für bessere Hörbarkeit:

- Ersetze formelle Formulierungen durch natürliche Umgangssprache
- Breche Sätze mit mehr als 20 Wörtern in zwei auf
- Füge 2-3 echte Überraschungsmomente ein (z.B. "Warte mal — das ist eigentlich enorm")
- Maximal 4-5 Sätze pro Sprecher-Turn
- Entferne Fachbegriffe die nicht sofort erklärt werden
- Keine Wiederholungen von Informationen

Output: NUR HOST_A:/HOST_B:-Zeilen. Kein Markdown, kein <scratchpad>, kein anderes Format.

Skript:
{raw_script}"""

    print("  Pass 2: Verfeinerung...")
    msg2 = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        messages=[{"role": "user", "content": pass2_prompt}],
    )
    refined_script = msg2.content[0].text

    # Scratchpad-Block entfernen falls noch vorhanden
    refined_script = re.sub(r"<scratchpad>[\s\S]*?</scratchpad>", "", refined_script)
    refined_script = refined_script.strip()

    script_dir = REPO_ROOT / "scratchpad" / "podcast-scripts"
    script_dir.mkdir(parents=True, exist_ok=True)
    script_path = script_dir / f"{input_path.stem}-podcast-script.txt"
    script_path.write_text(refined_script, encoding="utf-8")
    print(f"  Skript gespeichert: {script_path}")
    return script_path


# ── TTS-Modus ────────────────────────────────────────────────────────────────

def run_tts_mode(args: argparse.Namespace) -> Path:
    from pipeline.tts.markdown_cleaner import MarkdownCleaner
    from pipeline.tts.tts_backends import get_backend

    input_path = resolve_input(args)
    print(f"[INFO] Eingabe: {input_path.name}")

    raw_text = input_path.read_text(encoding="utf-8")

    cleaner = MarkdownCleaner(lang="de")
    chunks = cleaner.split_into_chunks(raw_text)
    print(f"[INFO] {len(chunks)} Chunks gefunden")

    tts_safe_path = save_tts_safe_text(input_path, chunks)
    print(f"[INFO] TTS-safe Text: {tts_safe_path.relative_to(REPO_ROOT)}")

    if args.dry_run:
        print("\n--- Dry-Run: Chunks ---")
        total_chars = 0
        for i, (title, text) in enumerate(chunks):
            print(f"  [{i+1:2d}] '{title}' — {len(text)} Zeichen")
            total_chars += len(text)
        print(f"---\nGesamt: {total_chars} Zeichen, ~{total_chars//15//60} Min Audio")
        return input_path

    voices_dir = Path(args.voices_dir) if args.voices_dir else None
    backend = get_backend(args.backend, voice=args.voice, voices_dir=voices_dir)
    check_backend_availability(backend)
    print(f"[INFO] Backend: {backend.get_name()}")

    tmp_dir = Path(tempfile.mkdtemp(prefix="tts_"))
    wav_paths: list[Path] = []

    try:
        for i, (title, text) in enumerate(chunks):
            print(f"[{i+1}/{len(chunks)}] '{title}' ({len(text)} Zeichen)...")
            t0 = time.monotonic()

            wav_bytes = backend.synthesize(text)

            wav_path = tmp_dir / f"chunk_{i:04d}.wav"
            wav_path.write_bytes(wav_bytes)
            wav_paths.append(wav_path)

            elapsed = time.monotonic() - t0
            print(f"        Fertig in {elapsed:.1f}s")

            if i < len(chunks) - 1 and args.pause > 0:
                print(f"        Thermische Pause: {args.pause}s...")
                time.sleep(args.pause)

        print("[INFO] Zusammenfügen...")
        combined = concatenate_wav_files(wav_paths)

        if not args.no_normalize:
            print("[INFO] Normalisiere auf -18 dBFS...")
            combined = normalize_audio(combined, target_dbfs=-18.0)

        output_dir = Path(args.output) if args.output else REPO_ROOT / "outputs" / "audio" / "tts"
        output_dir.mkdir(parents=True, exist_ok=True)

        out_path = output_dir / f"{input_path.stem}-{args.voice}.mp3"
        combined.export(str(out_path), format="mp3", bitrate="192k")

        duration_s = len(combined) / 1000
        size_mb = out_path.stat().st_size / (1024 * 1024)
        print(f"\n[DONE] Audio gespeichert: {out_path}")
        print(f"       Dauer:    {duration_s:.0f}s ({duration_s/60:.1f} Min)")
        print(f"       Dateigröße: {size_mb:.1f} MB")
        return out_path

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


# ── Podcast-Modus ─────────────────────────────────────────────────────────────

def run_podcast_mode(args: argparse.Namespace) -> Path:
    from pipeline.tts.tts_backends import get_backend

    input_path = resolve_input(args)
    print(f"[INFO] Eingabe: {input_path.name}")

    raw_md = input_path.read_text(encoding="utf-8")

    script_path = find_existing_script(input_path)
    if script_path:
        print(f"[INFO] Vorhandenes Skript: {script_path.name}")
    else:
        script_path = generate_podcast_script_via_api(raw_md, input_path)

    turns = parse_speaker_turns(script_path.read_text(encoding="utf-8"))
    print(f"[INFO] {len(turns)} Sprecher-Turns ({sum(1 for s,_ in turns if s=='HOST_A')} HOST_A, "
          f"{sum(1 for s,_ in turns if s=='HOST_B')} HOST_B)")

    voices_dir = Path(args.voices_dir) if args.voices_dir else None

    backend_a = get_backend("piper", voice="de_DE-thorsten-high", voices_dir=voices_dir)
    backend_b = get_backend("piper", voice="de_DE-thorsten_emotional-medium", voices_dir=voices_dir)

    check_backend_availability(backend_a)
    check_backend_availability(backend_b)

    # speaker_id für HOST_B aus Config lesen
    speaker_map_b = backend_b.get_speaker_map() if hasattr(backend_b, "get_speaker_map") else {}
    speaker_id_b = speaker_map_b.get("curious", speaker_map_b.get("neutral", None))
    if speaker_id_b is not None:
        print(f"[INFO] HOST_B Emotion-ID: {speaker_id_b} (aus speaker_id_map)")

    tmp_dir = Path(tempfile.mkdtemp(prefix="podcast_"))
    wav_paths: list[Path] = []

    try:
        for i, (speaker, text) in enumerate(turns):
            backend = backend_a if speaker == "HOST_A" else backend_b
            sid = None if speaker == "HOST_A" else speaker_id_b

            print(f"[{i+1}/{len(turns)}] {speaker}: {text[:60]}{'...' if len(text)>60 else ''}")

            wav_bytes = backend.synthesize(text, speaker_id=sid)
            wav_path = tmp_dir / f"turn_{i:04d}_{speaker}.wav"
            wav_path.write_bytes(wav_bytes)
            wav_paths.append(wav_path)

            if i > 0 and i % 10 == 0 and args.pause > 0:
                print(f"  Thermische Pause: {args.pause}s...")
                time.sleep(args.pause)

        print("[INFO] Podcast zusammenfügen (300ms Stille zwischen Turns)...")
        combined = assemble_podcast(wav_paths, silence_ms=300)

        if not args.no_normalize:
            print("[INFO] Normalisiere auf -18 dBFS...")
            combined = normalize_audio(combined, target_dbfs=-18.0)

        output_dir = Path(args.output) if args.output else REPO_ROOT / "outputs" / "audio" / "podcast"
        output_dir.mkdir(parents=True, exist_ok=True)

        out_path = output_dir / f"{input_path.stem}-podcast.mp3"
        combined.export(str(out_path), format="mp3", bitrate="192k")

        duration_s = len(combined) / 1000
        size_mb = out_path.stat().st_size / (1024 * 1024)
        print(f"\n[DONE] Podcast gespeichert: {out_path}")
        print(f"       Dauer:    {duration_s:.0f}s ({duration_s/60:.1f} Min)")
        print(f"       Dateigröße: {size_mb:.1f} MB")
        return out_path

    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)


# ── CLI ──────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Generiert TTS oder Podcast-Audio aus Markdown Research-Reports.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  # Neuesten Report als TTS (Dry-Run):
  python pipeline/tts/generate_audio.py --latest --dry-run

  # TTS mit Standard-Stimme:
  python pipeline/tts/generate_audio.py --latest --mode tts

  # Podcast-Dialog:
  python pipeline/tts/generate_audio.py --latest --mode podcast

  # Spezifische Datei, anderes Backend testen:
  python pipeline/tts/generate_audio.py --input outputs/aggregated/mk-combined/REPORT.md --backend piper --voice de_DE-thorsten_emotional-medium
        """,
    )
    src = p.add_mutually_exclusive_group()
    src.add_argument("--input", type=Path, metavar="DATEI",
                     help="Pfad zur Eingabe-.md-Datei")
    src.add_argument("--latest", action="store_true",
                     help="Neueste .md in outputs/aggregated/mk-combined/ verwenden")

    p.add_argument("--mode", choices=["tts", "podcast"], default="tts",
                   help="tts = lineare Narration, podcast = zwei Sprecher (Standard: tts)")
    p.add_argument("--backend", choices=["piper", "kokoro", "mms", "api"], default="piper",
                   help="TTS-Backend (Standard: piper)")
    p.add_argument("--voice", default="de_DE-thorsten-high",
                   help="Piper-Stimme (Standard: de_DE-thorsten-high)")
    p.add_argument("--pause", type=int, default=45,
                   help="Sekunden Pause zwischen Chunks (thermisch, Standard: 45)")
    p.add_argument("--output", type=Path, metavar="VERZEICHNIS",
                   help="Ausgabeverzeichnis (Standard: outputs/audio/tts/ oder podcast/)")
    p.add_argument("--voices-dir", type=Path, metavar="VERZEICHNIS",
                   help="Piper-Stimmen-Verzeichnis (Standard: ~/.local/share/piper-voices/)")
    p.add_argument("--no-normalize", action="store_true",
                   help="Lautstärke-Normalisierung überspringen")
    p.add_argument("--dry-run", action="store_true",
                   help="Zeigt Chunks, keine Synthese")
    return p


def main() -> None:
    check_dependencies()
    check_conda_env()

    parser = build_parser()
    args = parser.parse_args()

    if not args.input and not args.latest:
        parser.print_help()
        sys.exit(1)

    if args.mode == "tts":
        run_tts_mode(args)
    elif args.mode == "podcast":
        run_podcast_mode(args)


if __name__ == "__main__":
    main()
