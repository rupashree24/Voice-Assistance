import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyautogui
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
from translate import Translator
import pyjokes
import threading

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')

# Initialize the translator
translator = Translator(from_lang="English", to_lang="Hindi")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def screenshot():
    pic = pyautogui.screenshot()
    pic.save('screenshot.jpeg')

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 6:
        speak("Hey Owl")
    elif hour >= 6 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Hello sir")
    speak("I'm osky")
    speak("Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    print("Listening....")
    with sr.Microphone() as source:
        r.pause_threshold = 1
        try:
            audio = r.listen(source)
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            print("Sorry, there was an error with the request.")
            return "None"

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('rupashrees.cy23@rvce.edu.in', 'dhanashree758@gmail.com')
        server.sendmail('rupashrees18@gmail.com', to, content)
        server.close()
    except Exception as e:
        print(e)

def joke():
    speak(pyjokes.get_joke(language='en', category='all'))

def run_assistant():
    wishMe()
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia','https://en.wikipedia.org/wiki/History_of_India')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            speak(results)
            print(results)
        elif 'open college website' in query:
            webbrowser.open("https://www.rnsit.ac.in")
        elif 'start youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open dashboard' in query:
            webbrowser.open("http://mydy.dypatil.edu/rait/my/")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'email to omkar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "rupashrees18@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")
        elif 'shutdown' in query:
            print("shutting down...")
            speak("shutting down")
            break
        elif 'translate' in query:
            query = query.replace('translate', '')
            translation = translator.translate(query)
            speak(translation)
            print(translation)
        elif 'joke' in query:
            joke()
        elif 'screenshot' in query:
            screenshot()
        elif 'search youtube' in query:
            speak("What do you like to see ")
            search = takeCommand().lower()
            speak('I got this videos for you')
            webbrowser.open('https://www.youtube.com/results?search_query=' + search)
        elif 'search google' in query:
            speak("What should I search?")
            search = takeCommand().lower()
            speak('I hope this information might be useful')
            webbrowser.open('https://www.google.com/search?q=' + search)

def on_run_button_click():
    assistant_thread = threading.Thread(target=run_assistant)
    assistant_thread.daemon = True
    assistant_thread.start()

if _name_ == "_main_":
    root_1 = tk.ThemedTk()
    root_1.set_theme('radiance')
    root_1.title("Voice assistant")
    root_1.geometry("400x350")

    lbl1 = ttk.Label(master=root_1, text="Welcome to voice assistant app\n\n", wraplength=600)
    lbl1.pack()
    
    but1 = ttk.Button(root_1, text="Run the assistant🤖🔊", command=on_run_button_click)
    but1.config(width=22)
    but1.pack(padx=10, pady=10)
    
    quit4 = ttk.Button(root_1, text="EXIT", command=root_1.destroy)
    quit4.config(width=22)
    quit4.pack(padx=10, pady=20)
    
    root_1.mainloop()