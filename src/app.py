
import os
import tkinter as tk
import customtkinter as ctk
from tkVideoPlayer import TkinterVideo
import vlc

from text_generation.text_generator import generate_text
from audio_generation.audio_generator import generate_audio
from video_generation.video_generator import generate_video


# Initial setup
app = tk.Tk()
app.geometry("800x600")  
app.title("AI Rapper")

# Frames
bf = tk.Frame()
bf.pack()
pf = tk.Frame()
pf.pack(padx=8, pady=8)

# Functions
def generate_text_and_update_lyrics():
    gr = generate_text(p.get())
    l.delete(0, tk.END)
    l.insert(0, gr)

def generate_audio_and_save():
    generate_audio(l.get())

def play_generated_audio():
    if os.path.exists('generated_audio.wav'):
        player = vlc.MediaPlayer(os.path.abspath('generated_audio.wav'))
        player.play()
