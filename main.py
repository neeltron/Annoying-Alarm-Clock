from gtts import gTTS
import os

text = "wake up bruh"
language = "en"

speak = gTTS(text = text, lang = language, slow = False)
speak.save("a.mp3")
os.system("mpg123 a.mp3")
