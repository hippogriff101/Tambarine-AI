import speech_recognition as sr
from openai import OpenAI

#PLEASE USE YOUR OWN KEY - if i froget to remove my key please don't banckrupt me
client = OpenAI()

def Speech():
    # Create a Recognizer instance
    recognizer = sr.Recognizer()

    # Capture audio input from the microphone
    with sr.Microphone() as source:
    print("What is your question?: ")
    audio_data = recognizer.listen(source)

    # Perform speech recognition using Google Web Speech API
    try:
    text = recognizer.recognize_google(audio_data)
    print("You said:", text)
    except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
    except sr.RequestError as e:
    print("Error: Could not request results from Google Speech Recognition service;")

def askGPT():
    if not text:
        return

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": text}
        ]
    )

    print("🤖 Tambarine AI says:", response.choices[0].message.content)