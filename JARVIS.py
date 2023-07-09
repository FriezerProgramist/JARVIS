import os
import sys
import webbrowser
import openai
import speech_recognition as sr


from dotenv import load_dotenv as ld
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api_key = os.getenv("api_key")

def ai_response(my_task):
    copletion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": my_task}]
    )
    return copletion


import pyttsx3
engine = pyttsx3.init()
# engine.say("Текст")
# engine.runAndWait()



def talk(words):
    print(words)
    # os.system("say " + words)
    engine.say(words)
    engine.runAndWait()


talk("Привіт, чим можу допомогти?")

r = sr.Recognizer()
def command():
    global r

    with sr.Microphone() as source:
        print("Кажи")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        #task = r.recognize_google(audio, language="en-US").lower()
        task = r.recognize_google(audio, language="uk-UA").lower()
        #task = r.recognize_google(audio, language="ru-RU").lower()
        print("You: " + task)
    except sr.UnknownValueError:
        talk("Я тебе не розумію")
        task = command()

    return task


def make_something(ar_task):
    if ("відкрий" and "сайт") in ar_task:
        talk("ok")
        url = "https://ituniver.com"
        webbrowser.open(url)

    elif "стоп" in ar_task:
        talk("Goodbye")
        sys.exit()

    elif "ім'я" in ar_task:
        talk("My name is JARVIS")

    else:
        #print(handle_input(input("You: ")).choices[0].message.content)
        try:
            ai_res = ai_response(ar_task).choices[0].message.content
            talk(ai_res)
        except openai.error.ServiceUnavailableError:
            talk("Виникла помилка, спробую ще раз")
            try:
                ai_res = ai_response(ar_task).choices[0].message.content
                talk(ai_res)
            except openai.error.ServiceUnavailableError:
                talk("Не можу обробити відповідь, запитай ще раз")
            except openai.error.RateLimitError:
                talk("Спробуй через 20 секунд")
                r.pause_threshold = 20
        except:
            talk("Упс, щось пішло не так. Спробуйте ще раз")

while True:
    make_something(command())