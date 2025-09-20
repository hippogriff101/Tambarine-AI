import openai
import speech_recognition as sr
from gtts import gTTS
from dotenv import load_dotenv
from playsound import playsound
import os
import sys
import shutil
import time
import atexit

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    else:
        return os.path.dirname(os.path.abspath(__file__))

BASE_DIR = get_base_dir()
os.system("title Tambarine AI Assistant Log")

TEMP_DIR = os.path.join(os.getenv("LOCALAPPDATA"), "Tambarine", "Temp")
MAX_TEMP_FILES = 10
os.makedirs(TEMP_DIR, exist_ok=True)

# Clean temp folder on exit
atexit.register(lambda: shutil.rmtree(TEMP_DIR, ignore_errors=True))

def sound(file):
    try:
        playsound(os.path.join(BASE_DIR, "Sounds", file))
    except Exception as e:
        print(f"(⚠️ Sound missing or failed: {file}) {e}")

load_dotenv(os.path.join(BASE_DIR, ".env"))
openai.api_key = os.getenv("OPENAI_API_KEY")

def speak(text, filename=None):
    # Clean up old files
    audio_files = [os.path.join(TEMP_DIR, f) for f in os.listdir(TEMP_DIR) if f.endswith(".mp3")]
    if len(audio_files) >= MAX_TEMP_FILES:
        audio_files.sort(key=os.path.getctime)
        num_to_delete = len(audio_files) - MAX_TEMP_FILES + 1
        for f in audio_files[:num_to_delete]:
            os.remove(f)
        print(f"♻️ Removed {num_to_delete} old audio files from temp folder.")

    if filename is None:
        filename = os.path.join(TEMP_DIR, f"output_{int(time.time()*1000)}.mp3")
    tts = gTTS(text, lang='en')
    tts.save(filename)
    playsound(filename)
    return filename

text = ""

def speechtotxt():
    global text
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("\nTambarine is listening... (Say 'stop' to end)\n")
                sound("listening.mp3")
                audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=20)
        except sr.WaitTimeoutError:
            print("⏳ Timeout: no speech detected, try again...")
            sound("Error.mp3")
            continue
        except Exception as e:
            print(f"Microphone error: {e}")
            sound("Error.mp3")
            continue

        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            speak(f"You said: {text}")
            time.sleep(0.5)
            speak("Do you want to send this? Say yes or no.")
        except sr.UnknownValueError:
            print("Sorry, could not understand what you said, please try again.")
            sound("Error.mp3")
            continue
        except sr.RequestError:
            print("Network error with Google Speech Recognition.")
            sound("Network_Error.mp3")
            continue

        # Confirmation loop
        while True:
            try:
                with sr.Microphone() as source:
                    confirm_audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                confirm_text = recognizer.recognize_google(confirm_audio).lower()
                print("Confirmation:", confirm_text)

                if "yes" in confirm_text:
                    return text
                elif "no" in confirm_text:
                    speak("Okay, please say it again.")
                    break
                else:
                    speak("I didn't catch that. Please try again.")
            except sr.WaitTimeoutError:
                print("⏳ Confirmation timeout, please try again.")
                sound("Error.mp3")
            except sr.UnknownValueError:
                speak("Sorry, I could not understand your confirmation.")
            except sr.RequestError:
                speak("Network error during confirmation step.")
                sound("Network_Error.mp3")

def main():
    if not openai.api_key:
        print("❌ No API key found. Please add OPENAI_API_KEY to your .env file.")
        return

    print("Welcome to v2.0.1 \n")

    print(r"""
  _______              _                _                       _____ 
 |__   __|            | |              (_)                /\   |_   _|
    | | __ _ _ __ ___ | |__   __ _ _ __ _ _ __   ___     /  \    | |  
    | |/ _` | '_ ` _ \| '_ \ / _` | '__| | '_ \ / _ \   / /\ \   | |  
    | | (_| | | | | | | |_) | (_| | |  | | | | |  __/  / ____ \ _| |_ 
    |_|\__,_|_| |_| |_|_.__/ \__,_|_|  |_|_| |_|\___| /_/    \_\_____|
                                                                      
""")

                                                                 
                                                                 
    os.system("color a")
    sound("hello.mp3")

    messages = [
        {"role": "system", "content": "You are called Tambarine, a friendly and helpful AI voice assistant coded in Python. Keep your answers short and sweet as what you reply will be turned into audio output."}
    ]

    while True:
        user_text = speechtotxt()
        if not user_text:
            continue

        if user_text.lower().strip() in ["stop", "exit", "quit"]:
            print("Goodbye, see you next time!")
            sound("Goodbye.mp3")
            break

        messages.append({"role": "user", "content": user_text})

        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )
            answer = response.choices[0].message.content.strip()
            print("\nTambarine AI says:\n" + answer + "\n")
            speak("Tambarine AI says: " + answer)
            messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            sound("Error_ai.mp3")

if __name__ == "__main__":
    main()
