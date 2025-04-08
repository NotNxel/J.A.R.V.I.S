import pyttsx3

import speech_recognition as sr

import datetime

import os

import random

from requests import get

import requests

import wikipedia

import webbrowser

import pywhatkit as kit

import smtplib

import sys

import pyjokes

import time

import instaloader

from instaloader import Instaloader

import PyPDF2

import pyautogui

import operator

import psutil

from bs4 import BeautifulSoup
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[-3].id)
engine.setProperty('voice', voices[0].id)

#Speaking
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=7 ,phrase_time_limit=5)



    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak('Say that again please...')
        speak("Waiting for your instructions...")
        while True:
            query = takeCommand().lower()

            if 'start listening' in query:  # Check if user wants to start the assistant
                speak("Starting now.")
                break

            elif 'quit' in query:
                speak('Thank you, sir!')
                quit()

        return "None"
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    TT=time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good Morning, its {TT}")

    elif hour>=12 and hour<16:
        speak(f"Good Afternoon, its {TT}")

    else:
        speak(f"Good Evening, its {TT}")

    speak("I am Jarvis Sir. Please tell me how may I help you")

    def news():

        main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0e9aa8817bf84aad904f253b34797bbb'

        main_page = requests.get(main_url).json()

        articles = main_page["articles"]

        head = []

        day = ['first', 'second', 'third', 'fourth', 'fifth']


        for ar in articles:
            head.append(ar["title"])

        for i in range(len(day)):
            speak(f"today's {day[i]} news is: {head[i]}")
def Password():

    speak('Password')
    password = input('password:')
    if password == 'Neel@2704':
        speak('Access Granted')
        wishMe()
    else:
        speak('Access Denied')
        quit()
Password()
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('neel.n.p.2010@gmail.com',)
    server.sendmail('neel.n.p.2010@gmail.com', to, content)
    server.close()
def news():

    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=0e9aa8817bf84aad904f253b34797bbb'

    main_page = requests.get(main_url).json()

    articles = main_page["articles"]

    head = []

    day = ['first', 'second', 'third', 'fourth', 'fifth']
    for ar in articles:
        head.append(ar["title"])

    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def weather(city):
    city = city.replace(" ", "+")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers)
    speak("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    speak(location)
    speak(time)
    speak(info)
    speak(weather + "°C")

if __name__ == "__main__":
#    Password()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            webbrowser.open('spotify.com')

        elif 'open spotify' in query:
            webbrowser.open('spotify.com')

        elif "google and search" in query or "search on google" in query or "search something on google" in query:

            speak("sir what should i search on google")

            cm = takeCommand().lower()

            webbrowser.open(f"{cm}")

        elif'shut up'in query:
            speak('sorry sir')

        elif 'the time' in query:
            TT=time.strftime("%I:%M %p")
            speak(f"Sir, the time is {TT}")
        elif "wikipedia" in query:

            speak("searching wikipedia...")

            query = query.replace("wikipedia", "")

            results = wikipedia.summary(query, sentences=2)

            speak("according to wikipedia")

            speak(results)
        elif'send an email to Dad' in query:
            try:

                speak("what should i send")

                content = takeCommand().lower()

                to = 'nikhil.pappu@gmail.com'

                sendEmail(to, content)

                speak("email has been sent to dad")



            except Exception as e:

                print(e)

                speak("sorry sir, i am not able to send email to dad")

        elif "open hotstar" in query:
            url = "hotstar.com"
            hotstsar_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(hotstsar_path).open(url)
        elif "open zee5" in query:
            url = "zee5.com"
            zee_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(zee_path).open(url)
        elif "open instagram" in query:
            url = "instagram.com"
            instagram_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(instagram_path).open(url)
        elif "open facebook" in query:
            url = "facebook.com"
            facebook_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(facebook_path).open(url)

        elif "close notepad" in query:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        elif "close google" in query:
            speak("ok sir, closing google")
            os.system("taskkill /f /im chrome.exe")
        elif'ip address'in query:
            ip = get('https://ap.ipify.org').text
            print(ip)

        elif "play believer on youtube" in query:

            kit.playonyt("believer")



        elif "play believer lyrics on youtube" in query:

            kit.playonyt("believer lyrics")



        elif "play thunder on youtube" in query:

            kit.playonyt("thunder")



        elif "play same" in query:

            kit.playonyt("furelise ")



        elif "play drag me down on youtube" in query:

            kit.playonyt("drag me down")



        elif "play drag me down lyrics on youtube" in query:

            kit.playonyt("drag me down lyrics")
        elif "open notepad" in query:
            notepad_path = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(notepad_path)



        elif "open pycharm" in query:

            pycharm_path = "C:\\Pycharm app\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"

            os.startfile(pycharm_path)



        elif "open command prompt" in query:
            os.system("start cmd")

        elif "thanks" in query:
            speak("that's my pleasure sir!")
        elif "where am I" in query or "where we are" in query or "where are we" in query:
            speak("wait sir, let me check")

            try:

                ipAdd = requests.get('https://api.ipify.org').text

                print(ipAdd)

                url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'

                geo_requests = requests.get(url)

                geo_data = geo_requests.json()

                city = geo_data['city']

                country = geo_data['country']

                speak(f"sir i am not sure but i think we are in {city} city of {country} country")



            except Exception as e:

                speak("sorry sir, due to network issue i am not able to find where are.")

        elif "do some calculations" in query or "can you calculate" in query:

            r = sr.Recognizer()

            with sr.Microphone() as source:

                speak("Say what should i calculate for you sir, example 5 plus 4")

                print("listening...")

                r.adjust_for_ambient_noise(source)

                audio = r.listen(source)

            my_string = r.recognize_google(audio)

            print(my_string)


            def get_operator_fn(op):

                return {

                    '+': operator.add,  # plus

                    '-': operator.sub,  # minus

                    'x': operator.mul,  # multiplied by

                    'divided by': operator._truediv_,  # divided by

                }[op]


            def eval_binary_expr(op1, oper, op2):

                op1, op2 = int(op1), int(op2)

                return get_operator_fn(oper)(op1, op2)


            speak("your result is")

            speak(eval_binary_expr(*(my_string.split())))

        elif'switch the window'in query:
            pyautogui.keyDown('alt')
            pyautogui.keyDown('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')
            pyautogui.keyUp('tab')
        elif'program restart'in query:
            pyautogui.keyDown('shift')
            pyautogui.press('f10')
            pyautogui.keyUp('shift')
        elif'quit' in query:
            speak('Thank You Sir')
            quit()
        elif'battery' in query:
            import psutil
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f'sir our system has {percentage} percent battery')
            if percentage>75:
                speak('We Have enough power to continue our work')
            elif percentage>40 and percentage<75:
                speak('we should connect our system to a charging point to charge our battery')
            elif percentage>15 and percentage<30:
                speak('we dont have enough power to work, please connect to charging')
            elif percentage<15:
                speak('we have very low power ,please connect to charging the system will shutdown very soon')
        elif 'weather report'in query:
            speak("is That A Jojo Reference")
            city = input("Enter the Name of City ->  ")
            city = city + " weather"
            weather(city)
            speak("Have a Nice Day:)")
        elif'news'in query:
            news()
        elif "take screenshot" in query or "take a screenshot" in query:

            speak("sir please tell me the name of this screenshot file")

            name = takeCommand().lower()

            speak("please sir hold the screen for few seconds, i am taking screenshot")

            time.sleep(1)

            img = pyautogui.screenshot()

            img.save(f"{name}.png")

            speak("i am done sir, profile picture is saved in our main folder. Now i am ready for your next command")

            image = takeCommand().lower()

            if "show" in image:
                img.show()


        elif "shutdown the system" in query or "shut down the system" in query:

            os.system("shutdown /l")



        elif "restart the system" in query:

            os.system("restart /r /t 5")

        elif 'sleep the system' in query:
            speak('Thank you Sir')
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            quit()
