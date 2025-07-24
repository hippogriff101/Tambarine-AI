import openai
import speech_recognition as sr
from dotenv import load_dotenv
import os


load_dotenv()  # Load from .env
openai.api_key = os.getenv("OPENAI_API_KEY")

text = ""

def speechtotxt():
    global text
    while True:
        # Create a Recognizer instance
        recognizer = sr.Recognizer()

        # Capture audio input from the microphone
        with sr.Microphone() as source:
            print("What would you like to say")
            audio_data = recognizer.listen(source)

        # Perform speech recognition using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            break
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print("Error: Could not request results from Google Speech Recognition service;")
def askGPT():
    global text

    # Call GPT-4 
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": text}
        ]
    )

    # Print the AI's response
    print("\nTambarine AI says:\n")
    print(response.choices[0].message.content.strip())

def main():
    print("Welcome to Beta v1.0.1 \n")
    print("This project uses OpenAI credits. You must provide your own key in the .env file.\n")


    speechtotxt()
    while True:
        question = input("would you like to submit that to Tambarine Ai? (y or n): ").lower()
        if question == "y":
            print()
            break
        elif question == "n":
            print()
            speechtotxt()
        else:
            print("Please enter 'y' or 'n'!")
    askGPT()

if __name__ == "__main__":
    main()
