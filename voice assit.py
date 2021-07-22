import speech_recognition as sr  
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files
import smtplib 
import webbrowser
import requests
import pyowm as po
import datetime
import pyjokes as pj
from selenium import webdriver# to control browser operations
import time






def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!"+"hello chirag sir" )

    elif hour>=12 and hour<18:
        speak("Good Afternoon!"+"hello chirag sir" )   

    else:
        speak("Good Evening!"+"hello chirag sir" )


def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('your email', 'password')
    server.sendmail('your email', to, content)
    server.close()
  
num = 1
def speak(output): 
    global num 
  
    # num to rename every audio file  
    # with different name to remove ambiguity 
    num += 1
    print("Jarvis : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en', slow = False) 
    # saving the audio file given by google text to speech 
    file = str(num)+".mp3"  
    toSpeak.save(file) 
      
    # playsound package is used to play the same file. 
    playsound.playsound(file, True)  
    os.remove(file) 
    
def listening():
    reg=sr.Recognizer()
    audio=" " #intializing audio with an empty node
    with sr.Microphone() as source:
        print("listening...")
        audio=reg.listen(source,phrase_time_limit=3)
    print("Recognising")#time limit is 5 sec as pause
    
    try:
        text=reg.recognize_google(audio,language="en-in")
        print("you:",text)
        return(text)
            
    except:
        speak("sorry sir i couldn't get this")
        return
if __name__ == "__main__":
    wishMe()  
    while(1):
        speak("what can i do for you")
        text=listening().lower()
        if text == 0:
            speak("sorry i couldn't get this")
            continue;
        if "exit" in (text) or "bye" in (text) or "stop" in (text) or "moveout" in (text):
            speak("Ok sir bye bye and have a good time")
            break;
        if "open google" in text:
            speak("do you want me to search something in google")
            text=listening().lower()
            if "no" in text:
                speak("opening google chrome")
                os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome")
            if "yes" in text or "yup" in text or "yeah" in text:
                speak("what u want me to search")
                text=listening().lower()
                driver=webdriver.Firefox()
                driver.get("https://www.google.com/results?search_query=" + ''.join(text))   

        if "open youtube" in text:
            speak("do you want me to search something in youtube")
            text=listening().lower()
            if "no" in text :    
                speak("ok sir")
                url="https://www.youtube.com/"
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                speak("opening youtube in chrome")
                webbrowser.get(chrome_path).open(url)
            if "yes" in text or "yup" in text or "yeah" in text:
                speak("what u want me to search")
                text=listening().lower()
                driver=webdriver.Firefox()
                driver.get("https://www.youtube.com/results?search_query=" + ''.join(text))    

        if "wait" in text:
            speak("ok sir , on standby for 10 seconds")
            time.sleep(10)
            while(1):
                speak("time is over sir ,want me to wait for next 10 seconds")
                text=listening().lower()    
                if "yes" in text or "yup" in text or "yeah" in text:
                    speak("ok sir, on standby for 10 seconds")
                    time.sleep(10)
                if "no" in text:
                    speak("ok sir")
                    break;
        
        if "open blackboard" in text:
            speak("ok sir opening blackboard")
            url="https://learn.upes.ac.in/"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
        
        if "introduce" in text or "who are you" in text or "who created you" in text :
            speak("I am virtual assiatant and build by Chirag sir,do you want to know more about me contact him")
        
        if 'joke' in text :
            a=pj.get_joke()
            speak(a)
        if 'the time' in text:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")    
        
        if "email" in text or "mail" in text:
            speak("please input sender address for min address")
            to=input("enter email:")
            speak("what is the content")
            content=listening().lower
            sendmail(to,content)
            speak("check the email")
