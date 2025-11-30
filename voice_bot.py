#!/usr/bin/env python3
"""
Simple voice bot using Gemini API
Terminal-based voice conversation bot - no LiveKit needed
"""

import os
import sys
import time

from dotenv import load_dotenv
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Load environment variables
load_dotenv()

# Initialize Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("ERROR: GEMINI_API_KEY not found in environment variables")
    print("Please set GEMINI_API_KEY in your .env file or environment")
    sys.exit(1)

genai.configure(api_key=GEMINI_API_KEY)

# Initialize speech recognition and TTS
recognizer = sr.Recognizer()
microphone = sr.Microphone()
tts_engine = pyttsx3.init()

# Configure TTS (optional - adjust voice, speed, etc.)
tts_engine.setProperty('rate', 150)  # Speech speed
voices = tts_engine.getProperty('voices')
if voices:
    tts_engine.setProperty('voice', voices[0].id)  # Use first available voice


def speak(text):
    """Convert text to speech"""
    print(f"[Bot]: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()


def listen():
    """Listen to microphone and convert speech to text"""
    with microphone as source:
        print("\n[Listening...]")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            # Listen for audio with timeout
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("[Processing...]")
            
            # Use Google Speech Recognition
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            print("[Timeout] No speech detected")
            return None
        except sr.UnknownValueError:
            print("[Error] Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"[Error] Speech recognition service error: {e}")
            return None
        except Exception as e:
            print(f"[Error] {e}")
            return None


def get_gemini_response(user_input, chat_session):
    """Get response from Gemini API"""
    try:
        response = chat_session.send_message(user_input)
        return response.text.strip()
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"


def main():
    """Main function to run the voice bot"""
    print("=" * 60)
    print("Voice Bot - Gemini API")
    print("=" * 60)
    print("\nBot is ready!")
    print("Speak into your microphone...")
    print("Say 'quit' or 'exit' to stop")
    print("=" * 60 + "\n")
    
    # Initialize Gemini chat
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    
    # Welcome message
    welcome_msg = "Hello! I'm your voice assistant. How can I help you today?"
    speak(welcome_msg)
    
    # Main conversation loop
    while True:
        try:
            # Listen for user input
            user_text = listen()
            
            if user_text is None:
                continue
            
            print(f"[User]: {user_text}")
            
            # Check for exit commands
            if user_text.lower() in ['quit', 'exit', 'stop', 'goodbye']:
                goodbye_msg = "Goodbye! Have a great day!"
                speak(goodbye_msg)
                break
            
            # Get response from Gemini
            bot_response = get_gemini_response(user_text, chat)
            
            # Speak the response
            speak(bot_response)
            
        except KeyboardInterrupt:
            print("\n\nShutting down...")
            speak("Goodbye!")
            break
        except Exception as e:
            print(f"\n[Error]: {e}")
            error_msg = "Sorry, something went wrong. Please try again."
            speak(error_msg)


if __name__ == "__main__":
    # Test microphone availability
    try:
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Microphone initialized successfully!\n")
    except Exception as e:
        print(f"Error initializing microphone: {e}")
        print("Please check your microphone connection and permissions.")
        sys.exit(1)
    
    main()
