# Quick Start Guide

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Windows users:** If `pyaudio` fails, try:
```bash
pip install pipwin
pipwin install pyaudio
```

## 2. Get Gemini API Key

1. Visit https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

## 3. Create .env File

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace `your_gemini_api_key_here` with your actual API key.

## 4. Run the Bot

```bash
python voice_bot.py
```

## 5. Start Talking!

- Wait for `[Listening...]` message
- Speak clearly into your microphone
- Bot will respond with voice
- Say "quit" or "exit" to stop

## Tips

- Speak clearly and wait for the listening prompt
- Make sure your microphone is working
- Check microphone permissions in system settings
- Adjust volume if you can't hear responses

## Troubleshooting

- **No microphone detected**: Check connections and permissions
- **Can't understand speech**: Speak louder/clearer, check mic quality
- **No audio output**: Check speakers and system volume
- **API errors**: Verify your Gemini API key is correct
