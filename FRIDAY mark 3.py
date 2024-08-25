from numpy import common_type
import pyttsx3
from setuptools import Command
import speech_recognition as sr
import pyaudio
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')


def talk(text):
    engine.say('boss')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            Command = listener.recognize_google(voice)
            Command = Command.lower()
            if 'alexa' in Command:
                Command = Command.replace('alexa', '')
            print(Command)
    except:
        pass
    return Command


def run_alexa():
    Command = take_command()
    print(Command)
    if 'play on youtube' in Command:
        song = Command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in Command:
        time = datetime.datetime.now().strftime('%I,%M %p')
        print(time)
        talk(time)

    elif 'wikipedia' in Command:
        wikipedia = Command.replace('wikipedia', '')
        info = wikipedia.summary(wikipedia, 1)
        print(info)
        talk(info)

    elif 'jokes' in Command:
        talk(pyjokes.get_joke())
    else:
        talk('please tell me again')


while True:
    run_alexa()
