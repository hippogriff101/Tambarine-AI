# Tambarine AI

A voice-based assistant powered by OpenAI's GPT-4 (```openai```) and ```SpeechRecognition``` built in python.

---

## Features

- Speech-to-text input using microphone (Google Speech Recognition)

- GPT-4 conversation with memory

- Continuous conversation loop

- Voice commands

- Handles errors like bad connection or misunderstood speech

---

## Requirements

- Microphone

- **```requirements.txt```**
 ```txt
 openai==1.97.0
 SpeechRecognition==3.14.3
 ```
  Install the dependencies using:

```bash
pip install -r requirements.txt
```


---

## Installation Instructions


**Clone the repository**
```
git clone https://github.com/hippogriff101/Tambarine-AI.git
cd tambarine-ai
```

**Install dependencies**
```
pip install -r requirements.txt
```

---

## Open AI Key Setup

When the script starts, it will ask:
```
Please paste in your OpenAI key.
```
You can get your key from https://platform.openai.com/account/api-keys

_I hope to make this project free by using a free model or key_
_If you need a free key head to [this repo](https://github.com/dan1471/FREE-openai-api-keys) by [@dan1471](https://github.com/dan1471) 

---

## How to run / use

```
python main.py
```

What you need to do:

- Speak clearly into your microphone
- The assistant will transcribe what you say and reply using GPT-4
- Say "stop", "exit", or "quit" to end the session

---

## To Do

- Add text to speech with ``` GTTS ``` or ``` pyttsx3```
- Make a GUI version
- Option to use different ai models

## License

[_MIT License_](https://github.com/hippogriff101/Tambarine-AI/blob/main/LICENSE)

_Copyright (c) 2025 Freddie_
