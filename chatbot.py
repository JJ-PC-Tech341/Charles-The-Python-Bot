import smtplib
import datetime
import webbrowser
import os
import pywhatkit
import wikipedia
import pyjokes
import pyautogui as pg

def chatbot():
    operation = input('''
    Hi there I Am Charles your personal Chatbot
    Do You Want to Talk with me type Y for Yes and N for No
    ''')

    if operation == 'Y':
        wishme()

    elif operation == 'y':
        wishme()

    elif operation == 'N':
        print("Bye-Bye Thank You For Visiting")
        exit()

    elif operation == 'n':
        print("Bye-Bye Thank You For Visiting")
        exit()

    else:
        print("Can't Understand what you just said")
        chatbot()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")   

    else:
        print("Good Evening!")

    command = input('''
    Let's start a conversation
    ask me what you want to ??
    ''')

    if command == 'hi':
        print("Hello")
        wishme()

    elif command == 'open code':
        codePath = "C:\\Users\\Jash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        wishme()

    elif command == 'send mail':
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('pramendrajetly12@gmail.com', 'titu2104')
        server.sendmail('pramendrajetly12@gmail.com', 'jjpctech83@gmail.com',
        'Jash is a great Hacker')
        print('''
        Sending Mail
        To Your Recipent
        ''')
        server.close()
        wishme()
        
    elif command == 'open google':
        print("Opening Google !")
        webbrowser.open ("www.google.co.in")
        wishme()
        
    elif 'wikipedia' in command:
        print('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        print("According to Wikipedia")
        print(results)
        wishme()

    elif 'play' in command:
        song = command.replace('play', '')
        print('playing ' + song)
        pywhatkit.playonyt(song)
        wishme()

    elif 'the time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        print(f"Sir, the time is {strTime}")
        wishme()

    elif 'jash' in command:
        print('''He Is The Lord Of All Coders
        Hail Jash!''')
        wishme()

    elif 'whatsapp' in command:
        print("Opening Whatsapp !")
        webbrowser.open("web.whatsapp.com")
        wishme()

    elif 'shutdown' in command:
        print("Shutting Down Your PC")
        pg.hotkey('alt' + 'f4')
        pg.hotkey('/n')
        pg.hotkey('alt' + 'f4')
        pg.hotkey('/n')
        exit()
        
    elif command == 'open youtube':
        print("Opening Youtube !")
        webbrowser.open("www.youtube.com")
        wishme()

    elif command == 'run':
        print("Opening Run !")
        pg.hotkey('winleft')
        pg.typewrite("run \n", 0.1)
        wishme()

    elif command == 'open zoom':
        print("Opening Zoom")
        pg.hotkey('winleft')
        pg.typewrite("zoom \n", 0.1)
        wishme()

    elif command == 'delete unwanted files':
        print("Deleting Unwanted Files")
        pg.hotkey('winleft' + 'R')
        pg.typewrite("temp ")
        pg.hotkey('Ctrl' + 'A')
        pg.press('delete ')
        pg.hotkey('winleft' + 'R')
        pg.typewrite("run ", 0.1)
        pg.typewrite("%temp% ")
        pg.hotkey('Ctrl + A')
        pg.press('delete ')
        pg.hotkey('winleft')
        pg.typewrite("run ", 0.1)
        pg.typewrite("prefetch ")
        pg.hotkey('Ctrl + A')
        pg.press('delete')
        pg.hotkey('winleft')
        pg.typewrite("run ", 0.1)
        pg.typewrite("recent ")
        pg.hotkey('Ctrl + A')
        pg.press('delete')
        pg.hotkey('winleft')
        pg.typewrite("run ", 0.1)
        pg.typewrite("tree")
        pg.press('alt + f4')
        wishme()

    elif command == 'open this pc':
        print("Opening This PC !")
        pg.hotkey('winleft')
        pg.typewrite("file explorer \n", 0.1)
        wishme()

    elif command == 'open jeet construction':
        print("Opening JEET CONSTRUCTION & INTERIOR WORK")
        codePath = "I:\\Jeet P. Jetly\\Jeet Construction"
        os.startfile(codePath)
        wishme()

    elif command == 'about you':
        print('''
        l am your oersonal assistant charles sir
        l am developed by Jash P. Jetly
        Using Java Core and JavaScript
        l can be considered to be a simple
        A.I Assistant
        ''')
        wishme()

    elif command == 'about':
        print('''
        l am your oersonal assistant charles sir
        l am developed by Jash P. Jetly
        Using Java Core and JavaScript
        l can be considered to be a simple
        A.I Assistant
        ''')
        wishme()

    elif command == 'tell me a joke':
        print(pyjokes.get_joke())
        joke = input('''
        should l tell one more 
        Joke Sir
        type Y for Yes and N for No
        ''')

        if joke == 'Y':
            print(pyjokes.get_joke())
            
        elif joke == 'y':
            print(pyjokes.get_joke())

        elif joke == 'N':
            wishme()

        elif jokes == 'n':
            wishme()
        
    elif command == 'open J.J PC Tech':
        what = input('''
        What should I open Website Or Youtube Channel
        Type W for Website and Y for Youtube Channel
         ''')

        if what == 'w':
            print("Opening Website !")
            webbrowser.open("https://jjpctech83.wixsite.com/home")
            wishme()

        if what == 'W':
            print("Opening Website !")
            webbrowser.open("https://jjpctech83.wixsite.com/home")
            wishme()

        if what == 'Y':
            print("Opening Youtube Channel !")
            webbrowser.open("https://www.youtube.com/channel/UCgM1g1Rk3UObehRTddllTvw/featured")
            wishme()

        if what == 'y':
            print("Opening Youtube Channel !")
            webbrowser.open("https://www.youtube.com/channel/UCgM1g1Rk3UObehRTddllTvw/featured")
            wishme()

    elif command == "quit":
        print("Bye-Bye Thank You For Visiting")
        exit()
        wishme()

    else:
        print("Can't Understand What You Just Said")
        wishme()

chatbot()
wishme()
