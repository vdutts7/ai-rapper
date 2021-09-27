import os
import torch
import torchaudio
from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_voice


def generate_audio(lyrics):
    vs, cl = load_voice('eminem', extra_voice_dirs=['audio_samples'])
    tts = TextToSpeech()
    audio_tensor = tts.tts_with_preset(lyrics, voice_samples=vs, conditioning_latents=cl, preset='ultra_fast')
    torchaudio.save('generated_audio.wav', audio_tensor.squeeze(0).cpu(), 24000)
