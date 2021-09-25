
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