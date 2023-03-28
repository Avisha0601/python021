from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
import subprocess

root = Tk()
root.geometry("500x500")
root.configure(background="Light Blue")

label=Label(root,text="Welcome To Your Personal DeskTop Assisstant",bg="Light Blue",font="Arial")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speech_recognisor= sr.Recognizer()
    speak("How can i help you..?")
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data= speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('Please repeat i do not get that')
            speak('Please repeat i do not get that')
            r_audio()
        respond(voice_data)
        
        
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak('My name is Jarvis')
        print('My name is Jarvis')
    
    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
    if "search" in voice_data:
        speak("Opening Google")
        print("Openng Google")
        webbrowser.get().open("https://google.com/")
        
    if "videos" in voice_data:
        speak("Opening Youtube")
        print("Opening Youtube")
        webbrowser.get().open("https://youtube.com/")
        
    if "text editor" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["notepad.exe"])
        
    if "wikipedia" in voice_data:
        speak("Opening Wikipedia")
        print("Opening Wikipedia")
        webbrowser.get().open("https://www.wikipedia.org/")
        
    if "minecraft" in voice_data:
         speak("Opening Minecraft")
         print("Opening Minecraft")
         webbrowser.get().open("https://www.minecraft.net/en-us")
         
    if "valorant" in voice_data:
         speak("Opening Valorant")
         print("Opening Valorant")
         webbrowser.get().open("https://auth.riotgames.com/")
         
    if "call of duty" in voice_data:
         speak("Opening COD")
         print("Opening COD")
         webbrowser.get().open("https://www.callofduty.com/")
         
    if "schoolpad" in voice_data:
        speak("Opening Schoolpad")
        print("Opening Schoolpad")
        webbrowser.get().open("https://vhs.schoolpad.in/dashboardFeed/feed")
        
    if "drawing game" in voice_data:
        speak("Opening Scribble")
        print("Opening Scribble")
        webbrowser.get().open("https://skribbl.io/")
        
    if "canva" in voice_data:
        speak("Opening Canva")
        print("Opening Canva")
        webbrowser.get().open("https://www.canva.com/")
        
    if "pinterest" in voice_data:
        speak("Opening Pinterest")
        print("Opening Pinterest")
        webbrowser.get().open("https://in.pinterest.com/")
        
    if "book" in voice_data:
        speak("Opening Booktoopia")
        print("Opening Booktopia")
        webbrowser.get().open("https://www.booktopia.com.au/")

    if "teams" in voice_data:
        speak("Opening Microsoft Teams")
        print("Opening MS Teams")
        webbrowser.get().open("https://teams.microsoft.com")
        
    if "movies" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["netfilx.exe"])
        
    if "songs" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["spotify.exe"])
        
    if "calculate" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["calculator.exe"])
        
    if "Microsoft Word" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["word.exe"])
        
    if "table" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["excel.exe"])
        
    if "presentation" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["PowerPoint.exe"])
        
    if "coding" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["spyder.exe"])
   
    if "settings" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["settings.exe"])
        
    if "camera" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["camera.exe"])
        
    if "calendar" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["calendar.exe"])
        
    if "paint" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["paint.exe"])
        
btn= Button(root, text="Start", command=r_audio,bg="red3", fg="white", padx=10, pady=1, font=(Arial,11, "bold"), relief=FLAT)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()