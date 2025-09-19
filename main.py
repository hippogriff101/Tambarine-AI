import openai
import speech_recognition as sr
from gtts import gTTS
from dotenv import load_dotenv
from playsound import playsound
import os


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("⚠️ No API key found! Abuse of key may have occurred.")



def speak(text, filename="temp/output.mp3"):
    os.makedirs("temp", exist_ok=True)  # make sure temp/ exists
    tts = gTTS(text, lang='en')
    tts.save(filename)
    playsound(filename)

text = ""

def speechtotxt():
    global text
    while True:
        # Create a Recognizer instance
        recognizer = sr.Recognizer()

        # Capture audio input from the microphone
        with sr.Microphone() as source:
            print("\nTambarine is listening... (Say 'stop' to end)\n")
            playsound("listening.mp3")
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=20)

        # Perform speech recognition using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            playsound("wait4response.mp3")
            speak(text, "temp/user_input.mp3") 
            break
        except sr.UnknownValueError:
            print("Sorry, could not understand what you said, please try again.")
            playsound("Error.mp3")
        except sr.RequestError as e:
            print("Network error with Google Speech Recognition.")
            playsound("Network_Error.mp3")

def main():
    print("Welcome to Beta v1.0.2 \n")
    print("This project uses OpenAI credits. You must provide your own key for now.")
    print("This version allows for continous chats and voice commands")
    print("To exit, just say 'stop', 'quit', or 'exit' at any time.\n")
    playsound("hello.mp3")

    # Conversation history
    messages = [
        {"role": "system", "content": "You are called Tambarine, a friendly and helpful AI voice assistant coded in python."}
    ]


    while True:
        speechtotxt()


        if text.lower().strip() in ["stop", "exit", "quit"]:
            print("Goodbye, see you next time!")
            playsound("Goodbye.mp3")
            break

        messages.append({"role": "user", "content": text})

        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=messages
            )

            answer = response.choices[0].message.content.strip()
            print("\nTambarine AI says:\n" + answer + "\n")
            speak("Tambarine AI says: " + answer, "temp/assistant_response.mp3")

            messages.append({"role": "assistant", "content": answer})

        except Exception as e:
            print(f"Error during OpenAI API call: {e}") 
            playsound("Error_ai.mp3")

        



if __name__ == "__main__":
    main()
