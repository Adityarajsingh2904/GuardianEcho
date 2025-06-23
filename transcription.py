#!/usr/bin/env python3
"""Transcribe speech from audio files using OpenAI's Whisper model."""

import argparse
from pathlib import Path

from transformers import pipeline


def transcribe(audio_path: str, model: str = "openai/whisper-small") -> str:
    """Return transcribed text from the provided audio file."""
    asr = pipeline("automatic-speech-recognition", model=model)
    result = asr(audio_path)
    return result.get("text", "")


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe a WAV file with Whisper")
    parser.add_argument(
        "file",
        nargs="?",
        default="recorded.wav",
        help="Path to the WAV file to transcribe (default: recorded.wav)",
    )
    parser.add_argument(
        "--model",
        default="openai/whisper-small",
        help="HuggingFace model to use",
    )
    args = parser.parse_args()

    path = Path(args.file)
    if not path.is_file():
        parser.error(f"Audio file not found: {path}")

    text = transcribe(str(path), args.model)
    print(text)


if __name__ == "__main__":
    main()
