from gtts import gTTS

tts = gTTS("Hello, World! What a nice day.")
tts.save("hello.mp3")