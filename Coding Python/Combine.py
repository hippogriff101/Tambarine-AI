from gtts import gTTS
import speech_recognition as sr
from playsound import playsound

print("Please say your name into the mic: ")

# Create a Recognizer instance
recognizer = sr.Recognizer()

# Capture audio input from the microphone
with sr.Microphone() as source:
 print("Speak something...")
 audio_data = recognizer.listen(source)

# Perform speech recognition using Google Web Speech API
try:
 text = recognizer.recognize_google(audio_data)
 print("You said:", text)
 greet = f"Hello {text}, My name is Tambarine."

 tts = gTTS(greet, lang="en")

 tts.save("hello.mp3")
 

except sr.UnknownValueError:
 print("Sorry, could not understand audio.")
except sr.RequestError as e:
 print("Error: Could not request results from Google Speech Recognition service;")