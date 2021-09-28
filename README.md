
<div align="center">

<img src="https://res.cloudinary.com/dnz16usmk/image/upload/v1708917426/hf-transformers-logo.png" alt="logo" width="100" height="80"  />
<img src="https://res.cloudinary.com/dnz16usmk/image/upload/v1708917602/tortoise-tts-logo.png" alt="logo" width="140" height="80"  />
<img src="https://res.cloudinary.com/dnz16usmk/image/upload/v1708917770/eminem-face-logo.png" alt="logo" width="80" height="80"  />

  <h1 align="center">
        AI Rapper
    </h1>
    <p align="center"> 
        <i><b>Talking Head videos of your favorite rapper rapping about anything. Using open-source NLP and TTS libraries.</b></i>
        <br /> 
    </p>

[![Github][github]][github-url]

<img src="https://res.cloudinary.com/dnz16usmk/image/upload/v1708871291/ai-rapper-cover-vd7.png" />


 </div>

<br/>

## Table of Contents

  <ol>
    <a href="#about">📝 About</a><br/>
    <a href="#how-to-build">💻 How to build</a><br/>
    <a href="#tools-used">🔧 Tools used</a>
        <ul>
        </ul>
    <a href="#contact">👤 Contact</a>
  </ol>

<br/>

## 📝About

### Overview

- Input a prompt, reference audio, reference photo
- Output auto-generated rap lyrics in style of rapper, synthesized audio using cloned voice, and Talking Head video. 

### Features

- **Intelligent text (lyrics)**: input a prompt and harness state-of-the-art LLMs to craft creative and engaging rap verses.

- **Synthetic audio (voice)**: a text-to-speech (TTS) system to clone a voice based on audio sample and feed it generated lyrics.

- **Talking Head (video)**: input a reference image and cobine with generated audio to create a realistic, engaging talking head.


## 💻 How to build

### Prerequisites 

- **Clone MakeItTalk (for video generation)** `https://github.com/adobe-research/MakeItTalk/` into root directory of `ai-rapper`
- Add a strictly **256 x 256** image of rapper in `MakeItTalk/examples`. Face should be clear and un-obstructed. Ex: `MakeItTalk/examples/eminem.png`
- Add an audio **.wav** file ( ~ 10-30 sec) of rapper in a separate directory of `audio_samples` i.e.`audio_samples/eminem_00.wav`

### Install dependencies and run

```
pip install -r requirements.txt
```

```
python src/app.py
```

### Output

Look for generated video in `MakeItTalk/examples`:

```
/tmp/tmpx_swo6p1eminem_00.wav
/tmp/tmp7zx0u65zem.png
Audio-----> tmpx_swo6p1eminem_00.wav
Parameters===== tmpx_swo6p1eminem_00.wav 48000 [-29 -36 -43 ... 120 125 124]
Loaded the voice encoder model on cuda in 0.04 seconds.
Processing audio file tmpx_swo6p1eminem_00.wav
Loaded the voice encoder model on cuda in 0.03 seconds.
source shape: torch.Size([1, 576, 80]) torch.Size([1, 256]) torch.Size([1, 256]) torch.Size([1, 576, 257])
converted shape: torch.Size([1, 576, 80]) torch.Size([1, 1152])
Run on device: cuda
======== LOAD PRETRAINED FACE ID MODEL examples/ckpt/ckpt_speaker_branch.pth =========
....
....
....
====================================
z = torch.tensor(torch.zeros(aus.shape[0], 128), requires_grad=False, dtype=torch.float).to(device)
OpenCV: FFMPEG: fallback to use tag 0x7634706d/'mp4v'
examples/tmpx_swo6p1eminem_00.wav
ffmpeg version 4.4.2-0ubuntu0.22.04.1 Copyright (c) 2000-2021 the FFmpeg developers
....
....
....
OpenCV: FFMPEG: tag 0x67706a6d/'mjpg' is not supported with codec id 7 and format 'mp4 / MP4 (MPEG-4 Part 14)'
OpenCV: FFMPEG: fallback to use tag 0x7634706d/'mp4v'
Time - ffmpeg add audio: 15.704241514205933
finish image2image gen
examples/test_pred_fls_tmpx_swo6p1eminem_00_audio_embed.mp4
```
<video width="320" height="240" controls>
  <source src="https://res.cloudinary.com/dnz16usmk/video/upload/v1708870234/test_pred_fls_tmpx_swo6p1eminem3_audio_embed_kawjx8.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## 🔧Tools Used


<img
src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=yellow"
alt="Python"
/>
<img
src="https://img.shields.io/badge/🤗 HuggingFace Transformers libary-000000?style=for-the-badge&logoColor=white&color=white"
alt="Hugging Face Transformers library"
/>
<img
src="https://img.shields.io/badge/pyTorch_audio-EE4C2C?style=for-the-badge&logo=pyTorch&logoColor=white&color=EE4C2C"
alt="pyTorch audio"
/>
<img
src="https://img.shields.io/badge/CUDA Toolkit-40B5A4?style=for-the-badge&logo=nvidia&logoColor=ffffff&color=76b900"
alt="CUDA Toolkit"
/>
<img
  src="https://img.shields.io/badge/🐢 Tortoise TTS-40B5A4?style=for-the-badge&color=green"
  alt="Tortoise TTS"
/>
<img
  src="https://img.shields.io/badge/FFPMPEG-DD0031?style=for-the-badge&logo=ffmpeg&color=gray"
  alt="FFMPEG"
/>
<img
  src="https://img.shields.io/badge/OpenCV-FF6F00?style=for-the-badge&logo=opencv&logoColor=0166ff&color=black"
  alt="OpenCV"
/>


### NLP

**HuggingFace Transformers libary**
- Harnesses fine-tuned and pre-trained language models for rap lyric generation
- `AutoModelForCausalLM` generates text by predicting the next word based on previous ones, not on the ones that follow. Useful for speciifc creative tasks such as generating rap lyrics, which rely on stylistic model outputs that have been trained on vast amounts of diverse text data (thus enabling it to generate coherent and contextually relevant text based on a given user prompt)
- `AutoTokenizer` efficiently tokenizes input prompts, enabling seamless integration with LLMs. `DistilGPT2` (a distilled, more efficient version of GPT-2) efficiently handles this. See usage in `src/text_generation/text_generator.py`

### TTS

**Tortoise TTS**
- Used for synthesizing audio from text
- Supports custom voice models to mimic specific rappers' voices 

**CUDA Toolkit**
- Trained  Eminem's voice (as in the example) on a custom TTS model.
- NVIDIA's CUDA Toolkit used to accelerate GPU training.

**PyTorch Audio**
- `torchaudio` library handles audio data, saving synthesized rap audio in `*.wav` format


### Talking Head generation

**MakeItTalk** 
- Open-source Github repo used for video synthesis, harnessing OpenCV and FFMPEG
- Demo: `MakeItTalk/official_demo_make_it_talk.ipynb` 

**OpenCV**
- used to segment facial features in input image and lip-sync to audio

**FFMPEG**
- Used to handle smooth, compatible audio + video synthesis



## 👤Contact

<!-- Replace placeholders with your actual contact information -->
[![Email][email]][email-url]
[![Twitter][twitter]][twitter-url]

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[email]: https://img.shields.io/badge/me@vd7.io-FFCA28?style=for-the-badge&logo=Gmail&logoColor=00bbff&color=black
[email-url]: #
[github]: https://img.shields.io/badge/Github-2496ED?style=for-the-badge&logo=github&logoColor=white&color=black
[github-url]: https://github.com/vdutts7/ai-rapper
[twitter]: https://img.shields.io/badge/Twitter-FFCA28?style=for-the-badge&logo=Twitter&logoColor=00bbff&color=black
[twitter-url]: https://twitter.com/vdutts7/

