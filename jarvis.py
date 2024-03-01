import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import smtplib
import pyjokes
import os
import time

def speak():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry! Not Understand")

# speech to text 
def sptotxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # if 0 indexing means male and 1 means female 
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty(rate,100)
    engine.say(x)
    engine.runAndWait()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587) 
    server.ehlo()
    server.starttls()
    server.login('priyanshujain09062003@gmail.com','pbph yntg lqiu uvsu')
    server.sendmail('pj7779732@gmail.com',to,content)
    server.close()  

if __name__ == '__main__':
    sptotxt("Hello Jarvis This side can I help you!")
    while True:
        data1 = speak().lower()

        if "your name" in data1:
            name = "My name is Jarvis"
            sptotxt(name)
    
        elif "old are you" in data1:
            age = "I am 20 years old"
            sptotxt(age)

        elif "current time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")    
            sptotxt(time)
        
        elif 'open youtube' in data1:
            webbrowser.open("https://www.youtube.com/")    

        elif 'open whatsapp' in data1:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open chat gpt' in data1:
            webbrowser.open("https://chat.openai.com/")

        elif 'play song' in data1:
            add = r"C:\Users\priya\Music"
            listsong = os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add,listsong[5]))

        elif 'jokes' in data1:
            joke = pyjokes.get_joke(language="en",category="neutral")
            print(joke)
            sptotxt(joke)    
    
        elif 'send email' in data1:
                try:
                    sptotxt("What should I say to you")
                    content = speak()
                    to = "pj7779732@gmail.com"
                    sendEmail(to,content)
                    sptotxt("Email has been sent!")

                except Exception as e:
                    print(e)
                    sptotxt("sorry my friend. I am not able to send this email")    

        elif 'exit' in data1:
            sptotxt("Thank You! for your time")
            break  

else:
    print("Thanks")     