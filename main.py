from gtts import gTTS
import os
from datetime import datetime

text = "wake up bruh"
language = "en"

speak = gTTS(text = text, lang = language, slow = False)
speak.save("a.mp3")

print(str(datetime.now().time()))
while True:
  if str(datetime.now().time()) == '09:00:00':
    os.system("mpg123 a.mp3")
