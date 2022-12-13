import winsound
from gtts import gTTS
import os

import speech_recognition as sr

"""
myText = 'hi how are you'
language = 'en'

output = gTTS(text=myText, lang = language, slow=False)
output.save("output.mp3")
os.system("start output.mp3")

fliename = ''
winsound.PlaySound(fliename,  winsound.SND_FILENAME)

"""

voice = ""
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:

        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text == "stop":
                break
            voice = voice + str(text)
        except:
            print('say something...')
hr = gTTS(text=voice, lang='en', slow=False)
hr.save("1.wav")