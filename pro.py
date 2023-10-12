import speech_recognition as sr
import webbrowser
import time
from time import ctime
import pyttsx3
from playsound import playsound
import glob
import os
from win10toast import ToastNotifier
import calendar
import wikipedia
import smtplib
import wolframalpha

def talk(voice):
    assistant=pyttsx3.init()
    assistant.setProperty('rate',150)
    voices=assistant.getProperty('voices')
    assistant.setProperty('voice', voices[1].id)
    assistant.say(voice)
    assistant.runAndWait()
    print(voice)

def record_voice(ask=False):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
#I want the assistant to say a sentence and then wait for our answer and consider that answer as an input
            talk(ask)
        print('start recording....')
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data= r.recognize_google(audio)
        except sr.UnknownValueError:
            talk('I\'m sorry'+s+'but I didn\'t understand')
        except sr.RequestError:
            talk('sorry, my speech is down.please checking your network')
        return voice_data
    
def answer(voice_data):
    if 'name' in voice_data:
        talk('My name is Ana')
    elif 'how' in voice_data:
        talk('greats thanks, but how about you?')
    elif'upset' in voice_data:
        talk(s+''+'Remember, nothing in this world is worth upsetting about'+ 'so smile')
    elif 'happy' in voice_data:
        talk('This is very good! I hope you have a good day')
    elif 'what' in voice_data:
        talk(ctime())
    elif 'search' in voice_data:
        search= record_voice('What do you search for?')
        url='https://google.com/search?q='+search
        webbrowser.get().open(url)
        talk('Here is what I found for '+search)
    elif 'weather' in voice_data:
        weather()
    elif 'file' in voice_data:
        txt()
    elif 'song' in voice_data:
        talk('please enter the adress of your musicف')
        karbar=input('')
        create_playlist(str(karbar)+".mp3")
    elif 'python' in voice_data:
        open_IDLE()
    elif 'calendar' in voice_data:
        opencalendar()
    elif 'find' in voice_data:
        karbbar=record_voice('Say what do you want to search in wikipedia')
        search_wikipedia(karbbar)
    elif 'set' in voice_data:
        timer()
    elif 'reminder' in voice_data:
        reminder()
    elif 'email' in voice_data:
        send_email()
    elif 'information' in voice_data:
        information()
    elif 'add' in voice_data:
        sum()
    elif 'off' in voice_data:
        talk('good bye'+s)
        exit()
    else:
        talk('I can\'t do it')
        file=open('problem.txt','a')
        file.write(voice_data)
        file.write('\n')
        file.close()
  
def txt():
    talk(s+'Please enter the name of the text file that you want to create')
    name=str(input(''))
    file=open(name+'.txt','w')
    file.write(record_voice('Say the sentence you want to save in the file'))
    file.close()
    os.system(name+'.txt')

def reminder():
    talk('please enter What would you remind of?')
    text=str(input(''))
    talk('enter your seconds:')
    timer=int(input(''))
    for i in range(timer):
        i-=timer
        time.sleep(1)
    notificator=ToastNotifier()
    notificator.show_toast('REMIDER',text,duration=3)

def create_playlist(path):
    for song in glob.glob(path):
        print("playing...."+'\n'+song)
        playsound(song)

def send_email():
    talk('please type your email adress')
    sender_email=str(input(''))
    talk('Type the recipient\'s email')
    reseve=str(input(''))
    talk('please enter your password:')
    password=str(input(''))
    talk('please type your message')
    message=str(input(''))
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender_email,password)
    print('login success')
    server.sendmail(sender_email,reseve,message)
    print('Email has been sent to', reseve)

def open_IDLE():
    talk('enter the address of your program:')
    os.system(input(''))
    
def opencalendar():
    talk('year')
    year=int(input(''))
    talk('month')
    month=int(input(''))
    n=calendar.month(year,month)
    print(n)

def search_wikipedia(karbbar):
    print(wikipedia.search(str(karbbar)))
    print(wikipedia.summary(str(karbbar),sentences=5))


def timer():
    talk('Please enter your seconds:')
    l=int(input(''))
    for i in range(l):
        talk(str(l-i))
        time.sleep(1)
    playsound('alarm.mp3')
    talk(s+'time is finish')

def weather():
    app_id="8TW2WE-A4JE9TU9QG"
    client=wolframalpha.Client(app_id)
    weather=record_voice('Which city and country do you want to know the weather?')
    weather1='weather of'
    weather2=weather+weather1
    res=client.query(weather2)
    result=next(res.results).text
    print(result)

def information():
    id="8TW2WE-A4JE9TU9QG"
    client=wolframalpha.Client(id)
    talk(s+'please type your question...')
    weather=str(input('your question:'))
    res=client.query(weather)
    result=next(res.results).text
    talk('my answer is:')
    print(result)
def sum():
    talk('please say your first number')
    n=int(input(''))
    talk('say your second number')
    s=int(input(''))
    p=n+s
    talk(p)

n=record_voice('please say your name')
x=['my name is']
for item in x:
    if item in n:
        p=list(n)
        del p[0:11]
        s=''
        for item in p:
            s+=item
    else:
        s=n

time.sleep(1)
talk('hi'+s+'how can I help you?')
while 1:
    voice_data=record_voice()
    answer(voice_data)