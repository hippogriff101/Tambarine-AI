from gtts import gTTS

tts = gTTS("I'm Google Text to Speech, what is your name?", lang="en", tld="com.au")
tts.save("gTTS Auzzie.mp3")