"""
markdown_cleaner.py — Bereinigt Markdown-Research-Reports für TTS-Synthese.

Konvertiert Markdown-Syntax, Tabellen, URLs und Sonderzeichen in
gesprochenes Deutsch. Teilt den Text in Chunks an ## Headings auf
für thermisch sichere Verarbeitung.
"""

import re
from typing import Optional


class MarkdownCleaner:
    """
    Bereinigt Markdown für TTS-Synthese auf Deutsch.

    Verwendung:
        cleaner = MarkdownCleaner()
        chunks = cleaner.split_into_chunks(markdown_text)
        # → [("Einleitung", "clean text..."), ("Abschnitt: Methoden", "..."), ...]
    """

    ABBREVIATIONS_DE = {
        r"\bz\.B\.\b": "zum Beispiel",
        r"\bd\.h\.\b": "das heißt",
        r"\bu\.a\.\b": "unter anderem",
        r"\betc\.\b":  "und so weiter",
        r"\bvgl\.\b":  "vergleiche",
        r"\bbzw\.\b":  "beziehungsweise",
        r"\bca\.\b":   "circa",
        r"\binkl\.\b": "inklusive",
        r"\bexkl\.\b": "exklusive",
        r"\bggf\.\b":  "gegebenenfalls",
        r"\bi\.d\.R\.\b": "in der Regel",
        r"\bm\.E\.\b": "meines Erachtens",
        r"\bo\.ä\.\b": "oder ähnliches",
        r"\bu\.U\.\b": "unter Umständen",
        r"\bv\.a\.\b": "vor allem",
        r"\bw\.o\.\b": "wie oben",
    }

    def __init__(self, lang: str = "de"):
        self.lang = lang

    def clean(self, text: str) -> str:
        """Vollständige Bereinigungspipeline. Gibt sauberen Plaintext zurück."""
        text = self._convert_tables(text)
        text = self._clean_special_chars(text)
        text = self._clean_urls_and_code(text)
        text = self._strip_markdown(text)
        text = self._normalize_numbers(text)
        text = self._expand_abbreviations(text)
        text = self._final_cleanup(text)
        return text

    def split_into_chunks(self, text: str) -> list[tuple[str, str]]:
        """
        Teilt den Text an ## Headings auf.
        Gibt Liste von (chunk_titel, bereinigter_text) zurück.
        Text vor dem ersten ## wird als "Einleitung" behandelt.
        """
        parts = re.split(r"^(## .+)$", text, flags=re.MULTILINE)

        chunks: list[tuple[str, str]] = []

        # Erster Teil: Text vor dem ersten ## Heading
        intro_text = parts[0].strip()
        if intro_text:
            clean_intro = self.clean(intro_text)
            if clean_intro.strip():
                chunks.append(("Einleitung", clean_intro))

        # Restliche Teile: abwechselnd Heading + Inhalt
        for i in range(1, len(parts) - 1, 2):
            heading_raw = parts[i]          # z.B. "## Cross-Domain Verbindungen"
            content_raw = parts[i + 1] if i + 1 < len(parts) else ""

            title = heading_raw.lstrip("#").strip()
            clean_content = self.clean(content_raw)

            if clean_content.strip():
                # Titel als gesprochene Einleitung voranstellen
                full_text = f"Abschnitt: {title}. {clean_content}"
                chunks.append((title, full_text))

        return chunks if chunks else [("Dokument", self.clean(text))]

    # ── Private Methoden ────────────────────────────────────────────────────

    def _convert_tables(self, text: str) -> str:
        """
        Konvertiert Markdown-Tabellen in gesprochene Beschreibungen.
        Muss VOR _strip_markdown laufen (braucht Pipe-Zeichen).
        """
        lines = text.split("\n")
        result: list[str] = []
        i = 0

        while i < len(lines):
            line = lines[i]

            # Erkenne Tabellenanfang: Zeile mit mindestens zwei | Zeichen
            if re.match(r"^\s*\|.+\|", line):
                table_lines: list[str] = []
                while i < len(lines) and re.match(r"^\s*\|", lines[i]):
                    table_lines.append(lines[i])
                    i += 1

                spoken = self._table_to_speech(table_lines)
                result.append(spoken)
            else:
                result.append(line)
                i += 1

        return "\n".join(result)

    def _table_to_speech(self, table_lines: list[str]) -> str:
        """Wandelt Tabellen-Zeilen in gesprochenen Text um."""
        rows: list[list[str]] = []
        for line in table_lines:
            # Überspringe Separator-Zeilen (---|---|--)
            if re.match(r"^\s*\|[\s\-:\|]+\|\s*$", line):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if any(cells):
                rows.append(cells)

        if not rows:
            return ""

        headers = rows[0]
        n_cols = len(headers)
        spoken_parts: list[str] = [
            f"Eine Tabelle mit {n_cols} Spalten: {', '.join(headers)}."
        ]

        for row in rows[1:]:
            pairs = [f"{headers[j] if j < len(headers) else 'Spalte'}: {row[j]}"
                     for j in range(len(row)) if j < len(headers)]
            spoken_parts.append(". ".join(pairs) + ".")

        return " ".join(spoken_parts)

    def _clean_special_chars(self, text: str) -> str:
        """Bereinigt HTML-Entities, Sonderzeichen und überschüssige Leerzeilen."""
        # HTML-Entities
        replacements = {
            "&amp;": "und", "&lt;": "kleiner als", "&gt;": "größer als",
            "&nbsp;": " ", "&mdash;": " — ", "&ndash;": " – ",
            "&#x27;": "'", "&quot;": '"',
        }
        for entity, repl in replacements.items():
            text = text.replace(entity, repl)

        # Em-Dash / En-Dash normalisieren
        text = re.sub(r"\s*—\s*", " — ", text)
        text = re.sub(r"\s*–\s*", " – ", text)

        # Mehrfache Leerzeilen auf maximal zwei reduzieren
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text

    def _clean_urls_and_code(self, text: str) -> str:
        """Entfernt URLs, Code-Blöcke und Inline-Code."""
        # Fenced code blocks (``` ... ```)
        text = re.sub(r"```[\s\S]*?```", "", text)

        # Inline code (`...`)
        text = re.sub(r"`[^`]+`", "", text)

        # Markdown-Links: [text](url) → text
        text = re.sub(r"\[([^\]]+)\]\(https?://[^\)]+\)", r"\1", text)

        # Nackte URLs
        text = re.sub(r"https?://\S+", "", text)

        # Bild-Tags: ![alt](url)
        text = re.sub(r"!\[[^\]]*\]\([^\)]+\)", "", text)

        return text

    def _strip_markdown(self, text: str) -> str:
        """Entfernt restliche Markdown-Syntax."""
        # Headings (###, ##, #) — nur den Text behalten
        text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)

        # Bold + Italic (**text**, *text*, __text__, _text_)
        text = re.sub(r"\*{1,3}([^\*]+)\*{1,3}", r"\1", text)
        text = re.sub(r"_{1,3}([^_]+)_{1,3}", r"\1", text)

        # Strikethrough (~~text~~)
        text = re.sub(r"~~([^~]+)~~", r"\1", text)

        # Aufzählungszeichen (-, *, +) am Zeilenanfang
        text = re.sub(r"^[\s]*[-\*\+]\s+", "", text, flags=re.MULTILINE)

        # Nummerierte Listen (1. 2. etc.)
        text = re.sub(r"^[\s]*\d+\.\s+", "", text, flags=re.MULTILINE)

        # Blockquotes (>)
        text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)

        # Horizontale Linien (--- oder ***)
        text = re.sub(r"^[-\*]{3,}\s*$", "", text, flags=re.MULTILINE)

        # Verbleibende einzelne Pipe-Zeichen
        text = re.sub(r"\|", " ", text)

        # Eckige und runde Klammern ohne Link-Kontext
        text = re.sub(r"\[([^\]]+)\]", r"\1", text)

        return text

    def _normalize_numbers(self, text: str) -> str:
        """
        Normalisiert Zahlen für deutsche TTS-Synthese.
        Deutsche Konvention: . = Tausender-Trennzeichen, , = Dezimalzeichen.
        """
        # Tausender-Trennzeichen entfernen: 1.000 → 1000, 10.000 → 10000
        # Achtung: Nur wenn dem Punkt eine Ziffer folgt (kein Satzende)
        text = re.sub(r"(\d)\.(\d{3})\b", r"\1\2", text)

        # Prozent: 42% → 42 Prozent
        text = re.sub(r"(\d+)\s*%", r"\1 Prozent", text)

        # Euro: 42€ oder €42 → 42 Euro
        text = re.sub(r"(\d+)\s*€", r"\1 Euro", text)
        text = re.sub(r"€\s*(\d+)", r"\1 Euro", text)

        # Dollar: $42 → 42 Dollar
        text = re.sub(r"\$\s*(\d+)", r"\1 Dollar", text)

        # Dezimalzahlen: 3,14 bleibt als ist (Piper versteht deutsches Dezimalkomma)

        return text

    def _expand_abbreviations(self, text: str) -> str:
        """Expandiert gängige deutsche Abkürzungen."""
        for pattern, replacement in self.ABBREVIATIONS_DE.items():
            text = re.sub(pattern, replacement, text)
        return text

    def _final_cleanup(self, text: str) -> str:
        """Finaler Durchlauf: überschüssige Leerzeichen und Satzzeichen."""
        # Mehrfache Leerzeichen → eines
        text = re.sub(r" {2,}", " ", text)

        # Leerzeichen vor Satzzeichen entfernen
        text = re.sub(r" ([,\.;:!?])", r"\1", text)

        # Mehrfache Satzzeichen bereinigen
        text = re.sub(r"\.{2,}", ".", text)

        # Leerzeilen am Anfang/Ende trimmen
        text = text.strip()

        # Einzelne Zeilenumbrüche durch Leerzeichen ersetzen (TTS liest besser)
        text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)

        # Doppelte Leerzeilen auf eine reduzieren
        text = re.sub(r"\n{2,}", "\n\n", text)

        return text
