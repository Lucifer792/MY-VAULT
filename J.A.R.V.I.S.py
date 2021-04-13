import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak("Good Evening sir!")  

    speak("hello, I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'joke' in query:
            joke=pyjokes.get_joke()
            speak(joke)
            print(joke)

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by aaditya gupta.")

    

        elif 'news' in query:
             
            
            webbrowser.open("https://www.hindustantimes.com/")
                 
            speak('here are some top news from the hindustan times')
            print('''=============== HINDUSTAN TIMES ============'''+ '\n')
                 


        elif 'hey man are you there' in query:

            speak("Jarvis 1 point 4 point 1 in your service sir")#current version of the ai
        elif 'wake up' in query:

            speak("for you sir always")

        elif 'addition' in query:
            speak("please enter how many values you wanna enter")
            a=int(input())
            sum=0
            for i in range(a):
                b=float(input("Enter the value"))
                sum=sum+b
            print("the answer is", sum)
            speak(sum)

        elif 'subtract' in query:
            speak("enter the values to start calculation")
            print("'a'-'b'")
            gfx=float(input("enter value 'a'"))
            fxg=float(input("enter value 'b'"))
            sai=gfx-fxg
            print("the answer is", sai)
            speak(sai)

        elif 'multiply' in query:
            speak("please enter how many values you wanna enter")
            py=int(input())
            hai=1
            for i in range(py):
                yp=float(input("Enter the value"))
                hai=hai*yp
            print("the answer is", hai)
            speak(hai)

        elif 'divide' in query:
            speak("enter the values to start calculation")
            print("'a'/'b'")
            h=float(input("enter value 'a'"))
            m=float(input("enter value 'b'"))
            if m==0:
                speak("the answer to this is infinity or not defined")
            else:
                z=h/m
                print("the answer is", z)
                speak(z)

        elif 'shutdown my computer' in query:
            os.system("shutdown /s /t S")

        elif 'search google' in query:
            speak("what should i search on google")
            command = takeCommand().lower()
            webbrowser.open(f"{command}")

        elif "set alarm" in query:
            speak("at what time should i remind you?")
            command = takeCommand().lower()
            hour = int(datetime.datetime.now().hour)
            if command == hour:
                speak("please wake up sir your alarm has rang")
            
        elif "hello" in query:
            speak("hello! how are you?")

        elif "high" in query:
            speak("hello! how are you?")

        elif "that was fun" in query:
            speak("i am glad you liked that joke")

        
        
            
            
            
                
        

        
