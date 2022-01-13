import pyttsx3  # is a text-to-speech conversion module in Python.
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init(
    'sapi5')  # Speech Application Programming Interface(used for taking voices inbuilt in your windows)
voices = engine.getProperty('voices')
'''print(voices)'''  # here we get our inbuilt voices my comp have 2 voices man and woman
engine.setProperty('voice', voices[1].id)  # we set man voice if we write voices[2] then it is woman voice


def speak(audio):
    engine.say(audio)  # to speak audio string in our fun
    engine.runAndWait()  # it is necessory for speaking


def wishme():
    hour = int(datetime.datetime.now().hour)  # it gives me hour between 0-24
    if hour >= 0 and hour < 12:
        speak('good morning!')

    elif hour >= 12 and hour < 18:
        speak('good afternoon')

    else:
        speak('good evening')
    speak('I am jarvis please tell me how may help you')


def takeCommand():
    """#this fun takes microphone input from the user and returns string output"""
    r = sr.Recognizer()  # it is a class written in SpeechRecognizer module which helps in recognize the audio
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1  # seconds of non speaking audio before speaking complete
        # r.energy_threshold = 50
        # r.operation_timeout=1
        audio = r.listen(
            source)  # listen is fun written in sr.Recognizer class it Records a single phrase from ``source``

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,
                                   language='en-in')  # google web speech API. Performs speech recognition on audio data
        print('user said: ', query)  # query is variable name


    except Exception as e:
        # print(e)
        print('say that again please....')
        return ('None')
    return query


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia.')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)  # summery is fun in wikipedia module.
                                                             # it returns 2 sentences from wikipedia
            speak('according to wikipedia..')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play a song ' or 'play song' in query:
            music_path = 'D:\\Songs'
            songs=os.listdir(music_path)
            a=random.randint(1,100)
            print(songs)
            os.startfile(os.path.join(music_path,songs[a]))

        elif 'the time'in query:
            str_time=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir the time is {str_time}')

        elif 'open pycharm' in query:
            pycharm_path='C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin'
            os.startfile(pycharm_path)


