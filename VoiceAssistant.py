import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    '''it's to get something spoke'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12:
        speak("Good Morning!")
        print("Good Morning!")
    elif hour >12 and hour<=18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    else:
        speak("Good Evening!")
        print("Good Friday!")
    speak("Sir, I am Friday How can i help you?")
    print("Sir\nI am Friday How can i help you?")

def takeCommand():
    '''it's to get audio commands from user\nand first of all i can listen\ncan you'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say That again Please...")
        return "None"
    return query

if __name__=='__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'good night friday' in query:
            print("Good Night Sir! Have a nice Night")
            speak("Good Night Sir! Have a nice Night")
            break
        elif 'goodbye' in query:
            print("Good Bye Sir! Have a nice Day")
            speak("Good Bye Sir! Have a nice Day")
            break
        elif 'wikipedia' in query:
            speak("Searching on wikipedia")
            query = query.replace('wikipedia','')
            # wikipedia = webbrowser.open("wikipedia.com")
            results = wikipedia.summary(query)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open code' in query:
            # Code.exe
            codepath = "C:\\Users\\mohds\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        