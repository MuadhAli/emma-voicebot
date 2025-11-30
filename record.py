import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import time

SAMPLE_RATE = 44100
CHANNELS = 1
OUTPUT_FILE = "long_recording.wav"

print("🎤 Recording... Press Ctrl+C to stop.")

frames = []

def callback(indata, frames_count, time_info, status):
    if status:
        print("Status:", status)
    frames.append(indata.copy())

try:
    with sd.InputStream(samplerate=SAMPLE_RATE,
                        channels=CHANNELS,
                        callback=callback):
        while True:
            time.sleep(0.1)   # prevents 100% CPU usage
except KeyboardInterrupt:
    print("\n🛑 Stopped recording.")

# Convert list → NumPy array
audio_data = np.concatenate(frames, axis=0)

# Save as WAV
write(OUTPUT_FILE, SAMPLE_RATE, audio_data)

print(f"✅ Audio saved as: {OUTPUT_FILE}")
