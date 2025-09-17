import openai
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


text = ""

def speechtotxt():
    global text
    while True:
        # Create a Recognizer instance
        recognizer = sr.Recognizer()

        # Capture audio input from the microphone
        with sr.Microphone() as source:
            print("\nTambarine is listening... (Say 'stop' to end)\n")
            audio_data = recognizer.listen(source)

        # Perform speech recognition using Google Web Speech API
        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            break
        except sr.UnknownValueError:
            print("Sorry, could not understand what you said, please try again.")
        except sr.RequestError as e:
            print("Network error with Google Speech Recognition.")

def main():
    print("Welcome to Beta v1.0.2 \n")
    print("This project uses OpenAI credits. You must provide your own key for now.")
    print("This version allows for continous chats and voice commands")
    print("To exit, just say 'stop', 'quit', or 'exit' at any time.\n")

    # Conversation history
    messages = [
        {"role": "system", "content": "You are called Tambarine, a friendly and helpful AI voice assistant coded in python."}
    ]


    while True:
        speechtotxt()


        if text.lower().strip() in ["stop", "exit", "quit"]:
            print("Goodbye, see you next time!")
            break

        messages.append({"role": "user", "content": text})

        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=messages
            )

            answer = response.choices[0].message.content.strip()
            print("\nTambarine AI says:\n" + answer + "\n")

            messages.append({"role": "assistant", "content": answer})

        except Exception as e:
            print(f"Error during OpenAI API call: {e}")  

        



if __name__ == "__main__":
    main()
