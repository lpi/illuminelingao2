#!/usr/bin/env python
# coding: utf-8


from pathlib import Path
import wave
import numpy as np
from pocket_tts import TTSModel
import re

voice_name = 'azelma'
BASE_DIR = Path("../").resolve()
english_dir = BASE_DIR / "english_chapters"
audio_base_dir = english_dir.parent / "speeched_english_chapters"
chapter_re = re.compile(r"\d\d-[a-z]+([-_][a-z]+)*")
file_re = re.compile(r"\d{3}-[^.]+\.md")

# Load the model and voice state
tts_model = TTSModel.load_model()
voice_state = tts_model.get_state_for_audio_prompt(voice_name)

for path in english_dir.iterdir():
    if path.is_dir() and chapter_re.fullmatch(path.name):
        for md in path.rglob("*.md"):
            if md.is_file() and file_re.fullmatch(md.name):
                text = md.read_text(encoding='utf-8')

                # Calculate new path
                relative_path = path.relative_to(english_dir)

                # Combine: New Base + Relative Subfolders + Filename.wav
                output_path = audio_base_dir / relative_path / f"{md.stem}.wav"

                # Ensure the directory exists
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Generate
                print(f"Generating audio for {md.name} with voice: {voice_name}...")
                audio = tts_model.generate_audio(voice_state, text)

                # Normalize and convert to 16-bit PCM
                audio_data = audio.numpy()
                max_val = np.max(np.abs(audio_data))
                if max_val > 0:
                    audio_data = audio_data / max_val
                audio_data = (audio_data * 32767).astype(np.int16)

                print(f"Saving to {output_path}...")
                with wave.open(str(output_path), 'wb') as wav_file:
                    wav_file.setnchannels(1)  # Mono
                    wav_file.setsampwidth(2)  # 16-bit (2 bytes)
                    wav_file.setframerate(tts_model.sample_rate)
                    wav_file.writeframes(audio_data.tobytes())