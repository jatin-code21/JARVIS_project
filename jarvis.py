# from _typeshed import Self
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os  # It is used to open files in the computer
import smtplib  # Use to send email
import pyjokes
# import colour  # another file for game in same directory
import requests  # Used for weather forecasting
from googletrans import Translator
from wikipedia import exceptions  # module for starting file
import pywhatkit as kit
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUI import Ui_JarvisUI
import sys


# sapi5 used to take voices which is inbuilt in windows
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# Male voice and if voices[1] then female
engine.setProperty('voice', voices[0].id)


def speak(audio):  # for it to speak the function is created
    engine.say(audio)  # saying the audio that is passed
    engine.runAndWait()


def wishMe():  # will wish me in time
    hour = int(datetime.datetime.now().hour)  # will take current time is pc
    if hour >= 0 and hour <= 12:
        speak("Good Morning")

    elif hour > 12 and hour <= 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)  # 587 is port used
    server.ehlo()
    server.starttls()
    server.login('randomone112009@gmail.com', 'AaBb@147')
    server.sendmail('randomone112009@gmail.com', to, content)
    server.close()


def jokes():
    my_jokes = pyjokes.get_jokes(language='en', category='neutral')
    print(my_jokes)
    speak(my_jokes)


def weather():
    speak("Enter the name of city of which you want weather")
    city = input("City Name: ")
    Api_key = '6f788fac99978f726c25bb3b633a6fca'
    final_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(
        city, Api_key)

    result = requests.get(final_url)
    data = result.json()
    # city_weather = data['weather']['description']
    # speak(city_weather)
    temperature = data['main']['temp']
    print(f"The temperature is {temperature}")
    speak(f"The temperature is {temperature}")
    humidity = data['main']['humidity']
    print(f"Also humidity is {humidity}")
    speak(f"Also humidity is {humidity}")


class MainThread(QThread):
    def __init__(self):  # Inhereting so declare __init__
        super(MainThread, self).__init__()

    def run(self):  # main function (first this is called)
        self.TaskExecution()

    def translator(self):
        translater = Translator()
        speak("Say the words you want to tanslate")
        input_lang = self.takeCommand().lower()
        out = translater.translate(input_lang, dest="es")
        # print(out)
        speak(out.text)

    def takeCommand(self):
        # It takes voice input from user and return string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listining....")
            r.pause_threshold = 1  # can change different parameters also
            # seconds of non-speaking audio before a phrase is considered complete
            audio = r.listen(source)

        try:  # will run if there is no error
            print("Recognizing....")
            self.query = r.recognize_google(audio, language="en-in")
            # its using google engine to recognize audio there are different also present like bing,etc
            print(f"User said: {self.query}\n")

        except Exception as e:  # will run if program encounters any error
            print(e)
            # If you don't want to see error in console comment above line
            print("Say that again please...")
            return "None"  # Returning none string and not python one
        return self.query

    def TaskExecution(self):

       
        wishMe()
        while True:
            # to match the self.query we have lower it
            self.query = self.takeCommand().lower()
            # Logic for executing tasks based on self.query
            if "wikipedia" in self.query:
                speak("Searching Wikipedia")
                self.self.query = self.self.query.replace("wikipedia", "")
                result = wikipedia.summary(self.query, sentences=2)
                # returns 2 sentences from wikipedia
                speak("According to wikipedia")
                print(result)
                speak(result)

            elif "open youtube" in self.query:
                webbrowser.get(
                    "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s").open("youtube.com")

            elif "open google" in self.query:
                browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                webbrowser.get(browser_path).open("google.com")

            elif "open netflix" in self.query:
                browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                webbrowser.get(browser_path).open(
                    "https://www.netflix.com/in/")

            elif "play music" in self.query:
                music_dir = "D:\songs"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "the time" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif "open code" in self.query:
                code_path = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(code_path)

            elif "email me" in self.query:
                try:
                    speak("What should I say")
                    content = self.takeCommand()
                    to = "ozajatin9309@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent")
                except exceptions as e:
                    print(e)
                    speak("Sorry Jatin, I am not able to send this email")

            elif "colour game" in self.query:
                speak("Opening game")
                os.system('colour.py')

            elif "jokes" in self.query:
                jokes()

            elif "weather" in self.query:
                weather()

            elif "translator" in self.query:
                self.translator()

            elif "search google" in self.query:
                speak("what should i search on google")
                browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                cm = self.takeCommand().lower()
                webbrowser.get(browser_path).open(
                    "https://www.google.com/search?q=" + cm)

            elif "search youtube" in self.query:
                speak("what should i search on youtube")
                browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                cm = self.takeCommand().lower()
                webbrowser.get(browser_path).open(
                    "https://www.youtube.com/results?search_self.query=" + cm)

            elif "search amazon" in self.query:
                speak("what should i search on amazon")
                browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                cm = self.takeCommand().lower()
                webbrowser.get(browser_path).open(
                    f"https://www.amazon.in/s?k={cm}&ref=nb_sb_noss_2")

            elif "open amazon" in self.query:
                browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
                webbrowser.get(browser_path).open("https://www.amazon.in/")

            elif "play songs on youtube" in self.query:
                speak("Say the song name you want to play")
                song_name = self.takeCommand().lower()
                kit.playonyt(song_name)

            elif "exit" or "quit" in self.query:
                exit()

startExecution = MainThread()

class Main(QMainWindow): #QMainWindow has been inherited
    def __init__(self):
        super().__init__()
        self.ui = Ui_JarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close) #.close already defined

    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/Lenovo/Downloads/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/Lenovo/Downloads/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("gif/giphy.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main() # object creation
jarvis.show()
exit(app.exec_())
