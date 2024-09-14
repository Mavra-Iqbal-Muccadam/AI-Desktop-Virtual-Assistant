import pyttsx3 #For converting user text into speech
import datetime # For current date and time
import speech_recognition as sr #Ffor recognizing user voice
import wikipedia # For search engine from wikipedia
import webbrowser  #For opening any website on web
import os #For fetching directory contents (to open files)
import pytz
# import pyaudio 
import pywhatkit #For diff features in whatsapp and Youtube
from bs4 import BeautifulSoup
from googlesearch import search #For search through google
from word2number import w2n #For converting word as text to number
import math  #For math operations
from playsound import playsound #For playing audio file
import random as rd #For random stuff
import sys #For system exiting
import time #For time sleep
import pyjokes #For getting jokes from google
from tkinter import * #For visuals
from tkinter import Tk
from PIL import  Image,ImageTk #python imaging library (For jpg images)

# for Alpromav Speaking
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#voices[0] for male and voices[1] for female
voice_rate=engine.getProperty('rate')
engine.setProperty("rate",voice_rate-10)
# print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#for greeting
def greetings():
    hour= int(datetime.datetime.now().hour)
    if 6<=hour<12:
        speak("Rise and Shine. Hope you have a nice day today")
    elif 12<=hour<18:
        speak("Good afternoon")
    elif 18<=hour<24:
        speak("Good evening")
    else:
        speak("Best of luck for tommorrow ")


def missasma():
    speak("Miss Asma teaches Programming Language Subject to Software Engineering students, She is the reason i am made. To the world you may be a teacher. But to us you are like the biggest star shining out there.You are the only reason, We enjoy studying Python deligently. Thanks for being our teacher")

# for taking command for user
#takes voice input from user and converts into string
def command_input():
    a= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        a.pause_threshold = 1
        a.energy_threshold = 300
        with sr.Microphone() as source:
            # print("Say something!")
            audio = a.listen(source=source, timeout=3,phrase_time_limit=3)
    try:
        print("Recognizing...")
        user_query=a.recognize_google(audio,language="eng-us")
        print(f"you mean:{user_query}".lower())

    except Exception as e:
        speak("Unable to recognize your voice")
        return "none"
    return user_query

def worldclock():
    speak("i can tell you the time of following countries")
    country_names = ["Africa","America","Bangladesh","Dubai","Afghanistan","China","Canada ","Pakistan","Saudia Arabia","United Kingdom"]
    output.insert(INSERT, country_names)
    output.update()
    print(country_names)
    speak("Now tell me your choice")

def jokes():
    my_jokes = pyjokes.get_joke(language="en", category="all")
    output.delete("1.0",END)
    output.insert(INSERT,my_jokes)
    output.update()
    print(my_jokes)
    speak(my_jokes)

def best_websites(x):
    speak("these are the best result for your required search")
    for website in search(x, num=5, stop=10, pause=2):
        output.delete("1.0", END)
        output.insert(INSERT, website)
        output.update()
        print(website)

def calcdisplay():
    operation = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Angles through trignometry']
    output.delete("1.0", END)
    output.insert(INSERT,operation)
    output.update()
    print(operation)

def addition(x,y):
    try:
        c = w2n.word_to_num(x)
        print(c)
        output.delete("1.0", END)
        output.insert(INSERT, c)
        output.update()
        d = w2n.word_to_num(y)
        print(d)
        output.delete("1.0", END)
        output.insert(INSERT,d)
        output.update()
        answer = c + d
        output.delete("1.0", END)
        output.insert(INSERT, answer)
        output.update()
        speak(f"your answer is {answer}")
        print(answer)
    except Exception as e:
        speak("unable to recognize,try again")
    
def subtraction(x,y):
    try:
        c = w2n.word_to_num(x)
        print(c)
        output.delete("1.0", END)
        output.insert(INSERT, c)
        output.update()
        d = w2n.word_to_num(y)
        print(d)
        output.delete("1.0", END)
        output.insert(INSERT, d)
        output.update()
        answer = c - d
        output.delete("1.0", END)
        output.insert(INSERT, answer)
        output.update()
        speak(f"your answer is {answer}")
        print(answer)
    except EXCEPTION as e:
        speak("unable to recognize,try again")

def multiplication(x,y):
    try:
        c = w2n.word_to_num(x)
        print(c)
        output.delete("1.0", END)
        output.insert(INSERT, c)
        output.update()
        d = w2n.word_to_num(y)
        print(d)
        output.delete("1.0", END)
        output.insert(INSERT, d)
        output.update()
        answer = c*d
        output.delete("1.0", END)
        output.insert(INSERT, answer)
        output.update()
        speak(f"your answer is {answer}")
        print(answer)
    except EXCEPTION as e:
        speak("unable to recognize,try again")
    
def division(x,y):
    try:
        c = w2n.word_to_num(x)
        print(c)
        output.delete("1.0", END)
        output.insert(INSERT, c)
        output.update()
        d = w2n.word_to_num(y)
        print(d)
        output.delete("1.0", END)
        output.insert(INSERT, d)
        output.update()
        answer = c/d
        output.delete("1.0", END)
        output.insert(INSERT, answer)
        output.update()
        speak(f"your answer is {answer}")
        print(answer)
    except EXCEPTION as e:
        speak("unable to recognize,try again")

def sinQ(x):
    try:
        c = w2n.word_to_num(x)
        answer4 = '%.3f' % (math.sin(c))
        output.delete("1.0", END)
        output.insert(INSERT, answer4)
        output.update()
        speak(f"sin{c} is {answer4} ")
    except Exception as e:
        speak("unable to recognize,try again")

def cosQ(x):
    try:
        c = w2n.word_to_num(x)
        answer5 = '%.3f' % (math.cos(c))
        output.delete("1.0", END)
        output.insert(INSERT, answer5)
        output.update()
        speak(f"cos{c} is {answer5} radian ")
    except Exception as e:
        speak("unable to recognize,try again")

def tanQ(x):
    try:
        c = w2n.word_to_num(x)
        answer5 = '%.3f' % (math.tan(c))
        output.delete("1.0", END)
        output.insert(INSERT, answer5)
        output.update()
        speak(f"tan{c} is {answer5} radian ")
    except Exception as e:
        speak("unable to recognize,try again")

def livesaving():
    output.delete("1.0", END)
    output.insert(INSERT,"You are allowed to feel messed up and inside out It doesn't mean you are defective, it means you are human")
    output.update()
    speak("You are allowed to feel messed up and inside out It doesn't mean you are defective, it means you are human")
    output.insert(INSERT,"\nIf today all you did was hold yourself, i'm proud of you")
    output.update()
    speak("If today all you did was hold yourself, i'm proud of you")
    output.insert(INSERT,"\n Once you choose hope, anything is possible")
    output.update()
    speak(" Once you choose hope, anything is possible")




# Main Program
def main_program():
    greetings()
    speak("Welcome")
    speak("Alpro mav is at your service. How may I help you?")
    while True:
        user_query=command_input().lower()
        # if user_query==0:
            # continue
        ''' All the commands said by user will be stored here in 'query' and will be converted to lower case for easily
        recognition of command'''
        
#creating logics for our various task

        if 'tell me about yourself' in user_query or 'Who are You?' in user_query:
            speak("Hi!Nice to meet you. I am Alpro mav and I am made by Mavra and Aleeza. I am here to help you.To say any command, click speak button")
            
        elif "what's your name" in user_query or "what is your name" in user_query:
            speak("My friends call me Alpro mav")
            
        elif 'joke' in user_query or 'tell me a joke' in user_query:
            jokes()

        elif 'wikipedia' in user_query:
            try:
                speak("What do you want from wikipedia?")
                inst=command_input().lower()
                user_query=user_query.replace("wikipedia"," ")
                speak("Getting to wikipedia..")
                results= wikipedia.summary(inst,sentences= 1)
                speak("According to Wikipedia")
                output.insert(INSERT,results)
                output.update()
                speak(results)
            except Exception as e:
                speak("Wikipedia doesnot have infromation related to "+inst)
                   
        elif 'open youtube'in user_query or 'utube' in user_query:
                speak("opening youtube")
                webbrowser.open("https://www.youtube.com/")
                time.sleep(5)
                
        elif 'google' in user_query or 'googli' in user_query:
            speak("opening google")
            webbrowser.open("https://www.google.com/")
            time.sleep(5)
            
        elif 'open stackoverflow' in user_query or 'overflow' in user_query:
            speak("opening stackoverflow")
            webbrowser.open("https://stackoverflow.com/")
            time.sleep(5)
            
        elif 'Open github' in user_query or 'git hub' in user_query:
            speak("opening github")
            webbrowser.open("https://github.com/")
            time.sleep(5)

        elif 'open instagram' in user_query or 'insta gram' in user_query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")
            time.sleep(5)
            
        elif 'open classroom' in user_query or 'gc' in user_query:
            speak("opening classroom")
            webbrowser.open("https://classroom.google.com/u/0/h")
            time.sleep(5)
        
        elif 'open netflix' in user_query:
            speak("opening netflix")
            webbrowser.open("https://www.netflix.com/pk/")                
            time.sleep(5)
            
        elif 'open gmail' in user_query or 'mail'in user_query or 'male' in user_query:
            speak("opening gmail")
            webbrowser.open("https://mail.google.com/mail/u/0/")                
            time.sleep(5)
                    
        elif 'Open code' in user_query or 'vs code' in user_query:
            speak("opening Vs code")
            ProgramPath1="C:\\Users\\mavra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(ProgramPath1)                
            time.sleep(5)
            
        elif 'Open notepad' in user_query or 'notepad' in user_query or 'note' in user_query:
            speak("opening notepad")
            os.system("Notepad")                
            time.sleep(5)

        elif 'open weather' in user_query or 'weather now' in user_query:
            speak("opening weather on google")
            webbrowser.open('''https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-
            ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..
            35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..''')
            time.sleep(5)
           
#current time
        elif 'time' in user_query:
            # time=datetime.datetime.now().strftime("%H-%M minutes %S seconds")
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time now is" +time)  
#current date

        elif 'date' in user_query:
            date=datetime.datetime.now().strftime("%d/%m/%y")
            speak(f"The date today is" +date) 

#time zone in different countries
        elif 'world clock' in user_query or 'countries' in user_query:
            worldclock()
            
        elif 'dubai' in user_query or 'dubaai' in user_query:
            dubai_tz = pytz.timezone('Asia/Dubai')
            current_time_dubai = datetime.datetime.now(dubai_tz)
            print(f'The current time in Dubai is {current_time_dubai.strftime("%H:%M:%S")}')
            speak(f'The current time in Dubai is {current_time_dubai.strftime("%H:%M:%S")}')    

        elif 'america' in user_query or 'amarica' in user_query:
            america_tz = pytz.timezone('America/New_York')
            current_time_america = datetime.datetime.now(america_tz)
            print(f'The current time in America is {current_time_america.strftime("%H:%M:%S")}')
            speak(f'The current time in America is {current_time_america.strftime("%H:%M:%S")}')

        elif 'africa' in user_query or 'afreca' in user_query:
            africa_tz = pytz.timezone('Africa/Cairo')
            current_time_africa = datetime.datetime.now(africa_tz)
            print(f'The current time in Africa is {current_time_africa.strftime("%H:%M:%S")}')
            speak(f'The current time in Africa is {current_time_africa.strftime("%H:%M:%S")}')

        elif 'bangladesh' in user_query or 'baangladesh' in user_query:
            bangladesh_tz = pytz.timezone('Asia/Dhaka')
            current_time_bangladesh = datetime.datetime.now(bangladesh_tz)
            print(f'The current time in Bangladesh is {current_time_bangladesh.strftime("%H:%M:%S")}')
            speak(f'The current time in Bangladesh is {current_time_bangladesh.strftime("%H:%M:%S")}')

        elif 'afghanistan' in user_query or 'afghan' in user_query:
            afghanistan_tz = pytz.timezone('Asia/Kabul')
            current_timeafghanistan = datetime.datetime.now(afghanistan_tz)
            print(f'The current time in afghanistan is {current_timeafghanistan.strftime("%H:%M:%S")}')
            speak(f'The current time in afghanistan is {current_timeafghanistan.strftime("%H:%M:%S")}')

        elif 'china' in user_query or 'chaina' in user_query:
            china_tz = pytz.timezone('Asia/Shanghai')
            current_time_china = datetime.datetime.now(china_tz)
            print(f'The current time in china is {current_time_china.strftime("%H:%M:%S")}')
            speak(f'The current time in china is {current_time_china.strftime("%H:%M:%S")}')

        elif 'australia' in user_query or 'austrelia' in user_query:
            australia_tz = pytz.timezone('Australia/Sydney')
            current_time_australia = datetime.datetime.now(australia_tz)
            print(f'The current time in australia is {current_time_australia.strftime("%H:%M:%S")}')
            speak(f'The current time in australia is {current_time_australia.strftime("%H:%M:%S")}')

        elif 'pakistan' in user_query or 'karachi' in user_query:
            pakistan_tz = pytz.timezone('Asia/Karachi')
            current_time_pakistan = datetime.datetime.now(pakistan_tz)
            print(f'The current time in pakistan is {current_time_pakistan.strftime("%H:%M:%S")}')
            speak(f'The current time in pakistan is {current_time_pakistan.strftime("%H:%M:%S")}')   
    
#whatsapp sending messages
        elif 'message' in user_query or 'Whatsapp' in user_query:
            speak("Who do you want to message")
            a = int(datetime.datetime.now().hour)
            b = int(datetime.datetime.now().minute) + 2
            reciever = command_input().lower()
            speak("Kindly tell me your message")
            chat = command_input().lower()
            send_to = 0
            if "Friend" in reciever or "Mavra" in reciever or "Partner" in reciever or "Class fellow" in reciever:
               send_to = "+923326287222"
               pywhatkit.sendwhatmsg(send_to, chat, a, b)
            else:
               speak("limited to one number only")

#languages
        elif 'eid mubarak in 5' in user_query or '5 languages' in user_query:
            with open("alllanguage.txt") as f:
                for i in f.readlines():
                    speak(i)
                      
#google search engine links
        elif 'best websites' in user_query or 'best links' in user_query or 'best webs' in user_query:
            speak("what do you want me to search")
            user_query2 = command_input().lower()
            best_websites(user_query2)
          
#google search on google
        elif 'search' in user_query or 'search on google' in user_query :
            speak("What do you want me to search")
            user_query2= command_input().lower()
            speak("opening searches for"+user_query2)
            pywhatkit.search(user_query2)
            time.sleep(5)

#voice calculator
        elif 'calculate' in user_query or 'voice calculator' in user_query:
            speak("i can only perform following calculation")
            calcdisplay()
       
        elif "add" in user_query or "addition" in user_query:
           speak("tell me your first number")
           user_query3 = command_input().lower()
           speak("tell me your 2nd number")
           user_query4 = command_input().lower()
           addition(user_query3,user_query4) 
          
        elif "subtract" in user_query or "subtraction" in user_query or "minus" in user_query:
            speak("tell me your first number")
            user_query3 = command_input().lower()
            speak("tell me your 2nd number")
            user_query4 = command_input().lower()
            subtraction(user_query3,user_query4)  
          
        elif "multiply" in user_query or "product" in user_query or "multiplication" in user_query:
            speak("tell me your first number")
            user_query3 = command_input().lower()
            speak("tell me your 2nd number")
            user_query4 = command_input().lower()
            multiplication(user_query3,user_query4)

        elif "division" in user_query or "divide" in user_query:
            speak("tell me your first number")
            user_query3 = command_input().lower()
            speak("tell me your 2nd number")
            user_query4 = command_input().lower()
            division(user_query3,user_query4)   

        elif "sin" in user_query or "sin theta" in user_query:
            speak("tell me your angle")
            user_query3 = command_input().lower()
            sinQ(user_query3)       

        elif "cos theta" in user_query or "cosine" in user_query:
            speak("tell me your angle")
            user_query3 = command_input().lower()
            cosQ(user_query3)

        elif "ten" in user_query or "tangent" in user_query:
            speak("tell me your angle")
            user_query3 = command_input().lower()
            tanQ(user_query3)

#for solving quadratic equation
        elif "quadratic equation" in user_query or "maths" in user_query:
            try:
               speak("Tell me the value of a")
               user_query3= command_input().lower()
               a= w2n.word_to_num(user_query3)
               speak("Tell me the value of b")
               user_query4= command_input().lower()
               b= w2n.word_to_num(user_query4)
               speak("Tell me the value of c")
               user_query5= command_input().lower()
               speak("Tell me the value of c")
               c = w2n.word_to_num(user_query5)
               underoot= math.sqrt((b*b)-4*a*c)
               det1 = (-(b*b)+underoot)/(2*a)
               det2 = (-(b*b)-underoot)/(2*a)
               speak(f"the roots are {det1},{det2}")
            except Exception as e:
               speak("Math error")
            
#live saving 
        elif 'suicide' in user_query or 'kill' in user_query or 'depression' in user_query:
            a = int(datetime.now().hour)
            b = int(datetime.now().minute) + 2
            livesaving()
            pywhatkit.sendwhatmsg("+923213226078", "your child may do something dangerous. Go and check on him or her",a, b)
            
#on yt play song
        elif 'play songs on youtube' in user_query:
            # on yt play song
            # song=query.replace('play',"")
            speak("Which song you want to play")
            song=command_input().lower()
            speak("Playing" + song + "On youtube")
            pywhatkit.playonyt(song)
            time.sleep(5)
            
#music form vlc
        elif 'music' in user_query or 'song' in user_query:
            music_dir= "C:\\Users\\cz 3\\Desktop\\My Docs\\mysongs"
            songs= os.listdir(music_dir)
            print(songs)
            l1=[0,1,2,3]
            number= rd.choice(l1)
            os.startfile(os.path.join(music_dir,songs[number]))
            time.sleep(18)
                    


#existing from assistant
        elif 'exit' or 'quit' or 'close' in user_query:
            speak("See you later. Bye")
            sys.exit()

# Interface
main_interface=Tk()
main_interface.title("ALproMav Desktop Assistant")
main_interface.geometry("1920x1080")
main_interface.maxsize(1920,1080)
main_interface.minsize(1920,1080)
# BG Image
bg= Image.open("backgroundpicturefinal.jpg")
bg1=ImageTk.PhotoImage(bg)
bg_label= Label(main_interface,image=bg1)
# Main Heading
bg_label.place(x=0,y=0)
label_1=Label(main_interface,text="ALproMAV",fg="#06D9FF",bg="#000117",font="Algerian 60",relief=RAISED,border=0,width=10).place(x=40,y=160)
# Side heading
label_2=Label(main_interface,text="Engine of Future",bg="#000117",fg="white",font="Constantia 26 italic",relief=RIDGE,width=14,border=0).place(x=320,y=320)
# For name label
label_3=Label(main_interface,text='''Made By : 
Mavra Iqbal(SE-22019) 
Aleeza Hussain(SE-22018)''',bg="#000110",fg="#06D9FF",font="Constantia 12",width=30,border=0).place(x=1400,y=850)
#Button as Image
mic =Image.open("waves.jpg")
final_image=ImageTk.PhotoImage(mic)
button1=Button(main_interface,text="Microphone",font="Constantia 17",fg="white",borderwidth=0,relief=RAISED,image=final_image,command=lambda: [main_program(),command_input()]).place(x=320,y=420)
button2=Button(main_interface,text="Open with smile",bg="#000110",fg="white",relief=RAISED,font="Constantia 15 ",borderwidth=0,width=15,command= lambda : missasma()).place(x=460,y=650)
#for displaying results
output= Text(main_interface,wrap="word",width=30,height=10,bg="#000110",fg="#06D9FF")
output.place(x=50,y=730)

main_interface.mainloop()
