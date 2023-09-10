from tkinter import * 
import speech_recognition as sr
import pyttsx3 
from datetime import datetime
import time as t
import subprocess 
import webbrowser

root = Tk()
root.geometry("500x500")
root.configure(background="Light Blue")

label=Label(root,text="Welcome to your personal desktop asistant", bg="light blue", font=("Bahnschrift Light",15,"bold"))
label.place(relx=0.5,rely=0.1,anchor= CENTER)

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():
    speak("How can I help you...?")
    speech_recognisor = sr.Recognizer()
    voice_data=""
    while voice_data == "":  
     with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        #voice_data=""
        try: 
            voice_data=speech_recognisor.recognize_google(audio,language="en-in")
            t.sleep(5)
        except sr.UnknownValueError:
            print("Please repeat I did not get that")
            #speak("Please repeat I did not get that")
    print(voice_data)
    respond(voice_data)
    
def respond(voice_data):
    voice_data=voice_data.lower()
    print(voice_data)
    if "call" in voice_data:
        speak("My name is Jarvis")
        print("My name is Jarvis")
    if "one" in voice_data:
        speak("Current time is ")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
    if "text editor" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["notepad.exe"])
    elif "videos" in voice_data:
        speak('Opening youtube')
        print("Opening Youtube")
        webbrowser.get().open("https://youtube.com/")
    elif "search" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://google.com/")
    else:
        speak("I don't understand")
        print("I don't understand")

    
    
btn = Button(root,text = "Start",bg = "red3", fg="white", padx=10,pady=1,font=("Arial",11,"bold"),relief = FLAT, command=r_audio)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()