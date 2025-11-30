# Simple Voice Bot - Gemini API

A simple terminal-based voice conversation bot that uses Google's Gemini API for intelligent responses. No LiveKit or complex setup required!

## Features

- 🎤 Real-time voice input from microphone
- 🤖 Powered by Google Gemini API
- 🔊 Text-to-speech responses
- 💬 Natural conversation with context awareness
- 🖥️ Simple terminal interface
- ✅ No external servers needed (except for API calls)

## Prerequisites

1. **Python 3.8+** installed
2. **Gemini API Key** - Get one from [Google AI Studio](https://makersuite.google.com/app/apikey)
3. **Microphone** connected and working
4. **Speakers/Headphones** for audio output

## Installation

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   **Note for Windows:** If `pyaudio` installation fails, you may need to install it manually:
   ```bash
   pip install pipwin
   pipwin install pyaudio
   ```
   
   Or download the wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it.

2. **Set up environment variables:**
   
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

   Get your API key from: https://makersuite.google.com/app/apikey

## Usage

1. **Run the bot:**
   ```bash
   python voice_bot.py
   ```

2. **Start talking:**
   - The bot will listen when you see `[Listening...]`
   - Speak clearly into your microphone
   - The bot will process and respond
   - Say "quit", "exit", or "stop" to end the conversation

## How It Works

1. **Voice Input**: Microphone captures your speech
2. **Speech-to-Text**: Google Speech Recognition converts speech to text
3. **AI Processing**: Text is sent to Gemini API for intelligent responses
4. **Text-to-Speech**: Bot response is converted to speech using pyttsx3
5. **Audio Output**: Response is played through your speakers

## Configuration

You can modify the bot's behavior in `voice_bot.py`:

- **Speech speed**: Change `tts_engine.setProperty('rate', 150)` (default: 150)
- **Voice selection**: Modify voice selection in the TTS setup
- **Timeout settings**: Adjust `timeout` and `phrase_time_limit` in `listen()`
- **Model**: Change `gemini-pro` to other Gemini models

## Troubleshooting

- **"Microphone not found"**: Check your microphone connection and system permissions
- **"GEMINI_API_KEY not found"**: Make sure your `.env` file exists and contains the API key
- **"Could not understand audio"**: Speak more clearly or check microphone quality
- **"pyaudio installation fails"**: Use `pipwin` or install the wheel file manually (see Installation)
- **No audio output**: Check your speakers/headphones and system volume
- **Import errors**: Make sure all dependencies are installed: `pip install -r requirements.txt`

## Requirements

- Python 3.8+
- Microphone (for input)
- Speakers/Headphones (for output)
- Internet connection (for Gemini API and Speech Recognition)

## Notes

- The bot uses Google Speech Recognition which requires internet connection
- Gemini API calls require internet connection
- Text-to-speech (pyttsx3) works offline
- The bot maintains conversation context throughout the session

## License

MIT
