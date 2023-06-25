import os
import speech_recognition as sr

# ------------------
import pyttsx3
engine = pyttsx3.init()
# engine.say("Текст")
# engine.runAndWait()



def talk(words):
    print(words)
    # os.system("say " + words)
    engine.say(words)
    engine.runAndWait()


# talk("Привіт, чим можу допомогти?")
talk("Hello, how can I help you")


def command():
    r = sr.Recognizer()

command()