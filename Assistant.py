import datetime
import speech_recognition as sr
import pyttsx3
import pyaudio
import wikipedia
import webbrowser
import time
import os





engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


######################### The  above function is used to convert text into audio   ##########################

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning Sir")
    elif hour >=12 and hour < 16:
        speak("Good Afternoon Sir")
    elif hour >=16  and hour <= 19:
        speak("Good Evening Sir")
    else:
        speak("Good night")
    speak(" I am Bantai can I help you")

######################### The  above function is used to wish the user ##########################


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=0.5
        audio=r.listen(source)

    try:
        print("Recongnizing....")
        query = r.recognize_google(audio,language='en-in')
        print("User said: {}\n".format(query))

    except Exception as e:
        print("Say that again....Please")
        return "None"
    return query

######################### The  above function is used to convert audio into text   ##########################

if __name__=="__main__":

    wishMe()
    k = 0

    while True:
     query = takeCommand().lower()

     ########################### Below are the Commands we want the assitant to perform ########################

     if 'who' in query:
        query=query.replace("who is","")
        results=wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)

     elif 'open youtube' in query:
         webbrowser.open("https://www.youtube.com/")


     elif 'linkedin' in query:
         webbrowser.open("www.linkedin.com/in/pawan07")


     elif 'mail' in query:
         webbrowser.open("https://mail.google.com/mail/u/0/#inbox")



     elif "play music" in query:

         songs = os.listdir("E:\\songs")
         os.startfile(os.path.join("E:\songs",songs[k]))

     elif "next song" in query:
         k=k+1
         songs = os.listdir("E:\\songs")
         os.startfile(os.path.join("E:\songs", songs[k]))


