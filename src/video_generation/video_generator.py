import os

def copy_audio_to_directory():
    os.system("cp generated_audio.wav ./MakeItTalk/examples")

def generate_video():
    copy_audio_to_directory()
    os.system("cd MakeItTalk && python generate.py")

def play_generated_video():
    if os.path.exists('generated_audio.wav'):
        player = vlc.MediaPlayer(os.path.abspath('generated_audio.wav'))
        player.play()