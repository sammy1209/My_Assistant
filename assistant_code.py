import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import smtplib
import random
import wikipedia
import wolframalpha
import sys
from playsound import playsound

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Mam, I am your digital assistant LARVIS the Lady Jarvis!')
speak('How may I help you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
            
        elif 'open instagram' in query:
            speak('okay')
            speak('opening instagram')
            webbrowser.open('www.instagram.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy', "Today is inspiring,I've learnt about a lot of different things."]
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Mam! I am unable to send your message at this moment!')
                    
        elif 'can you sing' in query or 'do you sing' in query:
            speak('I am your personal assistant, tu tu tu tu, tu tu tu tu, I am here to help you tu tu tu tu')
            speak("I can search for you, even find you places, mail for you and cover many bases")            
         
         
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Mam, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Mam')

        elif 'bye' in query:
            speak('Bye Mam, have a good day.')
            sys.exit()
            
                                    
        elif 'play music' in query:
            
            
            speak("Here are the songs you wanna listen offline: ")
            speak("1. colors")
            speak("2. I'm not her")
            speak("3. nobody")
            speak("4. photograph")
            speak("5. the night we met")
            speak("6. you are the reason")
            query=x
            x=int(input("Enter your choice:"))
            
            speak('Okay, here is your music! Enjoy!')
            
            if(x==1):
                playsound('C:\\Users\\sameeksha\\Music\\Hollywood\\colors.mp3')
            elif(x==2):
                playsound("C:\\Users\\sameeksha\\Music\\Hollywood\\I'm not her.mp3")
            elif(x==3):
                playsound("C:\\Users\\sameeksha\\Music\\Hollywood\\nobody.mp3")
            elif(x==4):
                playsound("C:\\Users\\sameeksha\\Music\\Hollywood\\photograph.mp3")  
            elif(x==5):
                playsound("C:\\Users\\sameeksha\\Music\\Hollywood\\the night we met.mp3") 
            elif(x==6):
                playsound("C:\\Users\\sameeksha\\Music\\Hollywood\\you are the reason.mp3")  
            else:
                print("please select valid option")
    
    
              

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
