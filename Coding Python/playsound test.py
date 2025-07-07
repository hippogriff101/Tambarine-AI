from playsound import playsound
from gtts import gTTS
import os

def speak(text):
    filename = "hello.mp3"
    tts = gTTS(text)
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

speak("Hello!, This is working now.")