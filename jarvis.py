import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui
import psutil
import time
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
        #playsound("/E:/jarvis/wish.wav")
    else:
        speak("Good Evening sir")
        # playsound("E:/jarvis/wish.wav")

def take_input():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        input.pause_threshold = 1
       # input.energy_threshold = 200
        audio = input.listen(source)
    try:
        print("Recognizing...")
        input_data = input.recognize_google(audio, language="en-in")
    except Exception as e:
        print(e)
        speak("Sorry sir,Say that again please...")
        input_data = take_input()
    return input_data

def take_voice():
    input = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening in background...")
        input.pause_threshold = 1
        input.energy_threshold = 200
        audio = input.listen(source)
    try:
        print("Recognizing in background...")
        input_data = input.recognize_google(audio, language="en-in")
    except Exception as e:
        print(e)
        input_data = take_voice()
    return input_data


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening  ")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        qurey = r.recognize_google(audio, language="en-in")
        print(f"user said :{qurey}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("!sir, Please reapeat the statment")
        qurey = takeCommand()
    return qurey


if __name__ == "__main__":
    speak("All systems are up")
    wishMe()
    while True:
        qurey = takeCommand().lower()
        if 'wikipedia' in qurey:
            speak("Searching...")
            qurey = qurey.replace("wikipedia", "")
            result = wikipedia.summary(qurey, sentences=5)
            speak("According to wikipedia")
            speak(result)
            print(result)

        elif 'who are you' in qurey:
            speak("My name is Jarvis")

        elif 'open youtube' in qurey:
            webbrowser.open("youtube.com")

        elif 'open whatsapp' in qurey:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open classroom' in qurey:
            webbrowser.open("https://classroom.google.com/u/0/h")

        elif 'search' in qurey:
            qurey = qurey.replace("search", "")
            result = webbrowser.open(qurey)

        elif 'play music' in qurey:
            webbrowser.open("https://www.youtube.com/watch?v=rtDw-_1Gh0Q")

        elif 'open collage' in qurey:
            dir = "D:\\collage"
            os.startfile(dir)

        elif 'the time' in qurey:
            strtime = datetime.datetime.now().strftime("%H:%M")
            speak(f"its being !!!!! {strtime}")

        elif 'open vs code' in qurey:
            path = "C:\\Users\\Shoaib\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'open android studio' in qurey:
            path = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(path)

        elif 'open google' in qurey:
            path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(path)

        elif 'open  terminal' in qurey:
            os.system(" start cmd /c ")
            

        elif 'open notepad' in qurey:
            path = "%windir%\system32\notepad.exe"
            os.startfile(path)

        elif 'open paint' in qurey:
            path = "%windir%\system32\mspaint.exe"
            os.startfile(path)

        elif 'take screenshot' in qurey:
            path = "C:\\Users\\Shoaib\\Pictures"
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save("C:\\Users\\Shoaib\\Pictures\\screenshot1.png")
            speak("Screenshort taken ")

        elif 'take note' in qurey:
            dir = open("root.txt", "w")
            speak("Sir , Would you like to name it")
            time = datetime.datetime.now()

            c = take_input().lower()
            if c == 'yes':
                speak("By which name , i shoud save it")
                file_name = take_input().lower()

            else:
                file_name = time.strftime("%d_%m_%y_%H_%M")
            dir.write(file_name)
            dir.write("\n")
            speak("okay sir ! started noting")
            file = open(file_name, 'w+')
            text = takeCommand()
            file.writelines(text)
            file.close()
            dir.close()
            

        elif 'read note' in qurey:
            f= open("root.txt","r")
            if f.read() == None:
                speak("Sir, thier are no notes")
            else:
                data=f.readlines()
                speak(data)
            f.close()

        elif 'take a break'  in qurey:
            speak("Sure sir")
            c= True
            while c == True:
                time.sleep(5)
                data=take_voice()                
                if 'start' or 'up' or 'jarvis' in data :
                    speak("tell me  sir")
                    c = False
                else:
                    c= True
        
        elif 'close process' in qurey:
            qurey = qurey.replace("close process", "")
            for pid in (process.pid for process in psutil.process_iter() if process.name() == f"{qurey}.exe"):
                os.kill(pid)

        elif 'shutdown' in qurey:
            speak("good night sir !!!!! shuting down all ! systems ")
            os.system("shutdown /s")

        elif 'reboot' in qurey:
            speak("System is rebooting")
            os.system("shutdown /r")

        elif 'log out' in qurey:
            speak("Taking a nap!!!")
            os.system("shutdown -l")

        elif 'exit' in qurey:
            speak("Closing all systems !!!!!!! good night sir")
            exit()
        else:
            speak("Sir , try another keyword")


