import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Print available voices
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} - {voice.id}")

# Set voice (try different indexes to find male/female)
engine.setProperty('voice', voices[1].id)

engine.say("This is a different voice.")
engine.runAndWait()
