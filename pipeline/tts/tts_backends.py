"""
tts_backends.py — Backend-Abstraktion für TTS-Modelle.

Ermöglicht einfaches Austauschen von TTS-Modellen ohne Änderungen
im Hauptskript. Piper ist vollständig implementiert, andere als Stubs.

Neues Backend hinzufügen:
    1. Klasse die TTSBackend erbt erstellen
    2. In _BACKEND_REGISTRY eintragen
    3. Fertig — keine andere Datei anfassen
"""

import io
import json
import os
import wave
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional


class TTSBackend(ABC):
    """Basisklasse für alle TTS-Backends. Schnittstelle: Text rein → WAV-Bytes raus."""

    @abstractmethod
    def synthesize(self, text: str, speaker_id: Optional[int] = None) -> bytes:
        """Synthetisiert Text zu WAV-Bytes. Gibt rohes WAV-Binary zurück."""
        ...

    @abstractmethod
    def is_available(self) -> bool:
        """Prüft ob Modell-Dateien und Dependencies vorhanden sind."""
        ...

    @abstractmethod
    def get_name(self) -> str:
        """Gibt lesbaren Namen zurück (z.B. 'piper/de_DE-thorsten-high')."""
        ...

    def check_ram(self, required_mb: int) -> bool:
        """Prüft ob genug RAM verfügbar ist. Gibt False zurück wenn zu wenig."""
        try:
            import psutil
            avail_mb = psutil.virtual_memory().available / (1024 * 1024)
            return avail_mb >= required_mb
        except ImportError:
            return True  # psutil nicht verfügbar → nicht blockieren


class PiperBackend(TTSBackend):
    """
    Piper TTS Backend — vollständig implementiert.

    Primär-Backend für deutsche TTS-Synthese. Basiert auf VITS-Architektur,
    ONNX-nativ, läuft auf CPU ohne GPU.

    Verfügbare Stimmen (Download via setup.sh):
        de_DE-thorsten-high          — neutral, männlich, hohe Qualität
        de_DE-thorsten_emotional-medium — neutral + 8 Emotionen (speaker_id)
    """

    DEFAULT_VOICES_DIR = Path.home() / ".local" / "share" / "piper-voices"
    RAM_REQUIRED_MB = 512

    def __init__(
        self,
        voice: str = "de_DE-thorsten-high",
        voices_dir: Optional[Path] = None,
    ):
        self.voice = voice
        self.voices_dir = Path(voices_dir) if voices_dir else self.DEFAULT_VOICES_DIR
        self.model_path = self.voices_dir / f"{voice}.onnx"
        self.config_path = self.voices_dir / f"{voice}.onnx.json"
        self._voice_obj = None        # lazy-loaded beim ersten synthesize()
        self._speaker_map: dict = {}  # aus .onnx.json gelesen wenn vorhanden

    def _load_model(self) -> None:
        """Lädt Piper-Modell mit ONNX-Optimierungen für Intel CPU."""
        if not self.check_ram(self.RAM_REQUIRED_MB):
            raise MemoryError(
                f"Zu wenig RAM für Piper-Modell. "
                f"Benötigt: {self.RAM_REQUIRED_MB} MB. "
                f"Schließe andere Anwendungen und versuche es erneut."
            )

        # OMP-Threads vor dem Import setzen (wirkt auch wenn sess_options nicht exponiert)
        os.environ.setdefault("OMP_NUM_THREADS", "4")

        try:
            import onnxruntime as ort
            from piper.voice import PiperVoice

            # ONNX Session-Optionen für Intel Haswell (thermisch optimiert)
            sess_opts = ort.SessionOptions()
            sess_opts.intra_op_num_threads = 4   # physische Kerne
            sess_opts.inter_op_num_threads = 1
            sess_opts.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL

            # Versuche allow_spinning zu setzen (reduziert Idle-CPU-Last)
            try:
                sess_opts.intra_op.allow_spinning = False
            except AttributeError:
                pass  # Nicht alle ort-Versionen exponieren das

            # Prüfe ob PiperVoice.load() sess_options unterstützt
            import inspect
            load_sig = inspect.signature(PiperVoice.load)
            load_kwargs = {"use_cuda": False}
            if "config_path" in load_sig.parameters:
                load_kwargs["config_path"] = str(self.config_path)
            if "sess_options" in load_sig.parameters:
                load_kwargs["sess_options"] = sess_opts

            self._voice_obj = PiperVoice.load(str(self.model_path), **load_kwargs)

        except ImportError as e:
            raise ImportError(
                f"piper-tts oder onnxruntime nicht installiert: {e}\n"
                f"Führe 'bash pipeline/tts/setup.sh' aus."
            ) from e

        # Speaker-Map aus Config laden (für emotionale Stimme)
        if self.config_path.exists():
            try:
                config = json.loads(self.config_path.read_text())
                self._speaker_map = config.get("speaker_id_map", {})
            except (json.JSONDecodeError, OSError):
                pass

    def synthesize(self, text: str, speaker_id: Optional[int] = None) -> bytes:
        if self._voice_obj is None:
            self._load_model()

        from piper.config import SynthesisConfig
        syn_config = SynthesisConfig(speaker_id=speaker_id) if speaker_id is not None else None

        buf = io.BytesIO()
        with wave.open(buf, "wb") as wav_file:
            self._voice_obj.synthesize_wav(text, wav_file, syn_config=syn_config)
        return buf.getvalue()

    def is_available(self) -> bool:
        return self.model_path.exists() and self.config_path.exists()

    def get_name(self) -> str:
        return f"piper/{self.voice}"

    def get_speaker_map(self) -> dict:
        """Gibt die Emotions-Map zurück (z.B. {'neutral': 0, 'happy': 1, ...})."""
        if not self._speaker_map and self.config_path.exists():
            try:
                config = json.loads(self.config_path.read_text())
                self._speaker_map = config.get("speaker_id_map", {})
            except (json.JSONDecodeError, OSError):
                pass
        return self._speaker_map

    def get_speaker_id_for_emotion(self, emotion: str) -> Optional[int]:
        """Gibt die speaker_id für eine Emotion zurück. None wenn nicht gefunden."""
        return self.get_speaker_map().get(emotion)


class KokoroBackend(TTSBackend):
    """
    Stub für Kokoro-82M TTS.

    Kokoro v1.0 hat KEINE deutsche Sprachunterstützung.
    Für Implementierung wenn Deutsch hinzugefügt wird:
        pip install kokoro-onnx
        from kokoro_onnx import Kokoro
    """

    def synthesize(self, text: str, speaker_id: Optional[int] = None) -> bytes:
        raise NotImplementedError(
            "KokoroBackend ist nicht implementiert.\n"
            "Grund: Kokoro v1.0 hat keine Deutsch-Unterstützung.\n"
            "Verwende stattdessen: --backend piper\n"
            "Für Implementierung wenn Deutsch verfügbar: pip install kokoro-onnx"
        )

    def is_available(self) -> bool:
        return False

    def get_name(self) -> str:
        return "kokoro (stub — kein Deutsch)"


class MmsBackend(TTSBackend):
    """
    Stub für facebook/mms-tts-deu.

    Hinweis: CC-BY-NC 4.0 Lizenz — nicht für kommerzielle Nutzung.
    Für Implementierung:
        pip install transformers
        from transformers import VitsModel, AutoTokenizer
    """

    def synthesize(self, text: str, speaker_id: Optional[int] = None) -> bytes:
        raise NotImplementedError(
            "MmsBackend ist nicht implementiert.\n"
            "Lizenz: CC-BY-NC 4.0 (nicht kommerziell).\n"
            "Für Implementierung: pip install transformers\n"
            "Dann: from transformers import VitsModel, AutoTokenizer"
        )

    def is_available(self) -> bool:
        return False

    def get_name(self) -> str:
        return "mms-tts-deu (stub)"


class APIBackend(TTSBackend):
    """
    Stub für Cloud-TTS APIs (ElevenLabs, OpenAI TTS).

    Voraussetzung: ELEVENLABS_API_KEY oder OPENAI_API_KEY als Env-Variable.
    Vorteil: Höchste Qualität, SSML-Support, kein CPU-Overhead.
    Nachteil: Kosten, Internet-Abhängigkeit, Datenschutz.
    """

    def synthesize(self, text: str, speaker_id: Optional[int] = None) -> bytes:
        raise NotImplementedError(
            "APIBackend ist nicht implementiert.\n"
            "Setze ELEVENLABS_API_KEY oder OPENAI_API_KEY als Env-Variable.\n"
            "ElevenLabs: pip install elevenlabs\n"
            "OpenAI TTS: pip install openai"
        )

    def is_available(self) -> bool:
        return bool(
            os.environ.get("ELEVENLABS_API_KEY")
            or os.environ.get("OPENAI_API_KEY")
        )

    def get_name(self) -> str:
        if os.environ.get("ELEVENLABS_API_KEY"):
            return "api/elevenlabs (stub — implementierung fehlt)"
        if os.environ.get("OPENAI_API_KEY"):
            return "api/openai (stub — implementierung fehlt)"
        return "api (stub — kein API-Key gesetzt)"


# ── Factory ──────────────────────────────────────────────────────────────────

_BACKEND_REGISTRY: dict[str, type[TTSBackend]] = {
    "piper":  PiperBackend,
    "kokoro": KokoroBackend,
    "mms":    MmsBackend,
    "api":    APIBackend,
}


def get_backend(name: str, **kwargs) -> TTSBackend:
    """
    Erstellt eine Backend-Instanz nach Name.

    Args:
        name: Backend-Name ('piper', 'kokoro', 'mms', 'api')
        **kwargs: Werden an den Backend-Konstruktor weitergegeben.
                  Für PiperBackend: voice, voices_dir

    Beispiel:
        b = get_backend("piper", voice="de_DE-thorsten_emotional-medium")
        wav = b.synthesize("Hallo Welt", speaker_id=1)
    """
    if name not in _BACKEND_REGISTRY:
        available = list(_BACKEND_REGISTRY.keys())
        raise ValueError(
            f"Unbekanntes Backend '{name}'. "
            f"Verfügbar: {available}"
        )
    return _BACKEND_REGISTRY[name](**kwargs)


def list_backends() -> list[str]:
    """Gibt alle registrierten Backend-Namen zurück."""
    return list(_BACKEND_REGISTRY.keys())
