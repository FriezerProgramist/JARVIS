import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")

# for voice in voices:
#      print("--------------------")
#      print(f"Name: {voice.name}")
#      print(f"ID: {voice.id}")
#      print(f"Language: {voice.languages}")
#      print(f"Gender: {voice.gender}")
#      print(f"Age: {voice.age}")

engine.setProperty("voice", "eng")
for voice in voices:
    if voice.name == "Microsoft Zira Desktop - English (United States)":
        engine.setProperty("voice", voice.id)

rate = engine.getProperty("rate")
engine.setProperty("rate",rate-40)
engine.say("Hello")
engine.runAndWait()