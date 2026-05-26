import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')

if len(voices) > 0:
    engine.setProperty('voice', voices[0].id)

# ======================================

def speak(text):

    engine.say(text)

    engine.runAndWait()

# ======================================

def listen():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        return command.lower()

    except:

        return "Sorry sir, I could not understand."