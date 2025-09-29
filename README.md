# Real-Time Language Translator Bot

A real-time speech translator that listens from a microphone, converts speech to text, translates it into a target language, and optionally speaks out the translated audio for quick, natural communication across languages.[1]

## Features

- Real-time speech-to-text using the system microphone.[1]
- Fast translation between multiple languages using popular translation libraries/APIs.[1]
- Optional text-to-speech output for the translated result.[1]
- Simple, modular Python codebase ready for extension and UI integration.[1]

## Demo

- Run locally with a single command (see Quick Start), then speak into the microphone to hear or see the translated output.[1]
- Add a simple CLI flag to choose source/target languages.[1]

## Architecture

- Input: Microphone stream captured and buffered.[1]
- ASR: Speech recognition converts audio to source-language text.[1]
- MT: Machine translation converts text into target language.[1]
- TTS (optional): Translated text is synthesized to audio and played back.[1]

## Requirements

- Python 3.8+ recommended.[1]
- A working microphone.[1]
- Suggested Python packages:
  - speechrecognition (ASR)[1]
  - pyaudio or sounddevice (audio input)[1]
  - googletrans or deep_translator (translation)[1]
  - gTTS or pyttsx3 (TTS)[1]
  - playsound or pygame (audio playback)[1]

Create a requirements.txt with typical pins:
```
speechrecognition==3.10.0
pyaudio==0.2.14
googletrans==4.0.0rc1
gTTS==2.5.1
playsound==1.3.0
deep-translator==1.11.4
sounddevice==0.4.7
numpy==1.26.4
```


Note: On some systems, installing PyAudio requires system-level headers (e.g., portaudio). Check platform-specific instructions.[1]

## Installation

1) Clone the repository
```
git clone https://github.com/Jaiamar/Real-Time-language-translator-bot.git
cd Real-Time-language-translator-bot
```


2) Create and activate a virtual environment
```
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```


3) Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```


4) (If needed) Install system audio dependencies
- Windows: Install Microsoft C++ Build Tools if PyAudio fails to build.[1]
- macOS: `brew install portaudio` then `pip install pyaudio`.[1]
- Linux: `sudo apt-get install portaudio19-dev` then `pip install pyaudio`.[1]

## Quick Start

Run the main script with default languages (example assumes source=en, target=hi):
```
python main.py --src en --tgt hi --tts on
```


Common flags:
- `--src`: Source language code (e.g., en, ta, hi, ml).[1]
- `--tgt`: Target language code (e.g., en, ta, hi, ml).[1]
- `--tts {on,off}`: Enable text-to-speech output.[1]
- `--engine {googletrans,deep_translator}`: Choose translation backend.[1]
- `--mic-index N`: Select a specific microphone device index.[1]

Example:
```
python main.py --src ta --tgt en --tts on
```


## Usage Guide

- Speak clearly near the microphone after startup.[1]
- The console prints recognized text and translated text.[1]
- If TTS is on, the translated audio will play automatically.[1]
- Use Ctrl+C to stop the program.[1]

## Configuration

Create a `.env` for optional keys or configuration:
```
TRANSLATION_ENGINE=googletrans
DEFAULT_SRC=en
DEFAULT_TGT=hi
TTS=on
```


For engines requiring API keys (if added later), set:
```
API_KEY=your_key_here
```


## Language Codes

Typical codes follow ISO-639-1 (examples):
- en: English[1]
- hi: Hindi[1]
- ta: Tamil[1]
- ml: Malayalam[1]
- te: Telugu[1]
- kn: Kannada[1]

## Project Structure

Example layout:
```
Real-Time-language-translator-bot/
├─ main.py
├─ translator/
│  ├─ __init__.py
│  ├─ asr.py           # speech-to-text
│  ├─ mt.py            # translation
│  ├─ tts.py           # text-to-speech
│  └─ audio_io.py      # mic capture & playback
├─ requirements.txt
├─ .env.example
└─ README.md
```


- `asr.py`: Wraps SpeechRecognition for microphone input and transcription.[1]
- `mt.py`: Wrapper for chosen translation engine with retry and error handling.[1]
- `tts.py`: TTS synthesis and audio playback utilities.[1]
- `audio_io.py`: Microphone selection, stream handling, and buffering.[1]

## Error Handling and Tips

- If recognition fails: ensure the correct microphone index and adequate input volume.[1]
- If translation fails: check internet connection and try a different engine.[1]
- If TTS is silent: verify audio output device and that gTTS can reach the service.[1]
- Use `--mic-index` to pick the right input device; list devices via a small helper snippet or sounddevice query.[1]

## Roadmap

- Add offline ASR (Vosk/whisper.cpp) and offline TTS (Coqui-AI).[1]
- Add simple GUI (Tkinter/Streamlit) with language dropdowns.[1]
- Caching translations for repeated phrases.[1]
- Transcription saving and subtitle (SRT) export.[1]

## Contributing

Contributions are welcome:
- Fork the repo and create a feature branch.[1]
- Follow PEP 8 and include docstrings/tests where reasonable.[1]
- Open a pull request describing the change and testing steps.[1]

