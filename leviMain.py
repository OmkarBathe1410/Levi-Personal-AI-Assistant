import sys
import typing
from PyQt5.QtWidgets import QDialog, QWidget, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QThread

from finalAiGui import Ui_finalAiGui

from LeviChatBot import *
import pyttsx3
import speech_recognition as sr
import webbrowser
import keyboard
import pyjokes
import os
import pyautogui
import datetime
import time as t
from time import sleep
import pywhatkit
import wikipedia
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

warnings.simplefilter("ignore")
url = f'https://cdn.botpress.cloud/webchat/v1/index.html?options=%7B%22config%22%3A%7B%22composerPlaceholder%22%3A%22Talk%20with%20Levi%22%2C%22botConversationDescription%22%3A%22A%20personal%20AI%20Assistant%20built%20with%20the%20help%20of%20Python.%22%2C%22botId%22%3A%2210be8df2-4230-4249-8fa0-6cbc495da8d8%22%2C%22hostUrl%22%3A%22https%3A%2F%2Fcdn.botpress.cloud%2Fwebchat%2Fv1%22%2C%22messagingUrl%22%3A%22https%3A%2F%2Fmessaging.botpress.cloud%22%2C%22clientId%22%3A%2210be8df2-4230-4249-8fa0-6cbc495da8d8%22%2C%22webhookId%22%3A%22241ac713-4132-4ccf-8057-f4be4f847162%22%2C%22lazySocket%22%3Atrue%2C%22themeName%22%3A%22prism%22%2C%22botName%22%3A%22Levi%20-%20Personal%20AI%20Assistant%22%2C%22frontendVersion%22%3A%22v1%22%2C%22enableConversationDeletion%22%3Atrue%2C%22theme%22%3A%22prism%22%2C%22themeColor%22%3A%22%232563eb%22%2C%22chatId%22%3A%22bp-web-widget%22%2C%22encryptionKey%22%3A%22ajTlzD7DMRpHYcbq5pkhC4IBvtDvlkli%22%7D%7D'

chrome_options = Options()
# Enable headless mode (runs Chrome without GUI)
chrome_options.add_argument('--headless=new')
chrome_options.add_argument('--log-level=3')  # Set Chrome log level
driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(5)


def click_on_chat_button():
    '''
    To click on the chat button that appears when the above site is opened
    '''
    driver.find_element(By.XPATH, '/html/body/div/div/button').click()
    sleep(4)
    while True:
        try:
            loader = driver.find_element(
                By.CLASS_NAME, 'bpw-msg-list-loading')
            is_visible = loader.is_displayed()
            ui.terminalPrint('Initializing Levi...')

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            ui.terminalPrint('Levi is initializing...')
            break
        sleep(1)


def sendQuery(text):
    '''
    Find and interact with the textarea element
    '''
    textarea = driver.find_element(By.ID, 'input-message')
    textarea.send_keys(text)
    sleep(2)

    send_btn = driver.find_element(By.ID, 'btn-send').click()
    sleep(2)


def isBubbleLoaderVisible():
    ui.terminalPrint('Levi is typing...')
    while True:
        try:
            bubble_loader = driver.find_element(
                By.CLASS_NAME, 'bpw-typing-group')
            is_visible = bubble_loader.is_displayed()

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            ui.terminalPrint('Levi is sending message...')
            break
        sleep(1)


chatnumber = 2


def retriveData():
    '''
    For retrieving the reply given by our chatbot
    '''
    ui.terminalPrint('Retriving Chat...')
    global chatnumber
    sleep(1)
    try:
        p = driver.find_element(
            By.XPATH, f'/html/body/div/div/div/div[2]/div[1]/div/div/div[{chatnumber}]/div/div[2]/div/div/div/div/div')
        chatnumber = chatnumber + 2
        return (p.text)
    except:
        return ''


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 170)


def Speak(audio):
    '''
    @param audio = text
    Makes our assistant to speak the provided text.
    '''
    ui.updateMoviesDynamically('speaking')
    engine.say(audio)
    ui.terminalPrint(f"Levi: {audio}")
    print("  ")
    engine.runAndWait()


def TakeCommand():
    ui.updateMoviesDynamically('listening')
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        ui.terminalPrint("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, 0, 8)

        try:
            ui.updateMoviesDynamically('loading')
            ui.terminalPrint("Recognizing...")
            query = str(recognizer.recognize_google(audio, language='en-in')).lower()
            ui.terminalPrint(f"You Said: {query}")
            return query
        except sr.UnknownValueError:
            ui.terminalPrint('Sorry could not understand the audio..')
            return ''

def PlayMusic():
    '''
    Performs task related to music.
    '''
    Speak("Once I start listening, please tell me the name of song..")
    
    musicName = TakeCommand()
    pywhatkit.playonyt(musicName)
    t.sleep(3)
    Speak("Your song has been started, Enjoy!")
    return


def WikipediaSearch(query):
    """
    @param query = User's query.
    Does the wikipedia search and returns the results.
    """
    Speak("Once I start listening, please tell me what do you want to search on wikipedia..?")
    
    query = TakeCommand()
    Speak("Searching Wikipedia...")
    wiki = wikipedia.summary(query, 10)
    Speak(f"According to wikipedia: {wiki}")
    return


def Screenshot():
    """
    Takes a screenshot and saves it with the name that we provide
    """
    Speak("Ok boss.. What should i name the file?")
    path = TakeCommand()
    path1name = path + ".png"
    path1 = "C:\\Users\\Omkar\\Pictures\\Screenshots\\" + path1name
    ss = pyautogui.screenshot()
    ss.save(path1)
    os.startfile(path1)
    t.sleep(2)
    Speak("Here is your screenshot boss..")
    return


def YoutubeAuto(query):
    """
    @param query = User's query
    Does all the automation related to Youtube.com
    """
    from keyboard import press_and_release
    from time import sleep
    from pyautogui import press, write, click
    query = str(query)
    if 'pause' in query:
        press('k')
    elif 'resume' in query:
        press('k')
    elif 'full screen' in query:
        press('f')
    elif 'film screen' in query or 'film mode' in query:
        press('t')
    elif 'skip' in query or 'foward' in query:
        press('l')
    elif 'back' in query or 'backward' in query:
        press('j')
    elif 'seek' in query:
        if 'forward' in query:
            press('l')
        elif 'backward' in query:
            press('j')
    elif 'increase' in query and ('speed' in query or 'playback rate' in query):
        press_and_release('shift + ,')
    elif 'decrease' in query and ('speed' in query or 'playback rate' in query):
        press_and_release('shift + .')
    elif 'mute' in query:
        press('m')
    elif 'unmute' in query:
        press('m')
    elif 'play' in query and 'previous' in query:
        press_and_release('shift + p')
    elif 'play' in query and 'next' in query:
        press_and_release('shift + n')
    elif 'play' in query or 'search' in query:
        Speak('Okay boss!')
        Speak('Once I start listening please tell me, what you want to search?')
        search_query = TakeCommand().lower()
        Speak('Processing your request...')
        press('/')
        sleep(0.7)
        press(['shift', 'home', 'backspace'])
        sleep(0.7)
        write(search_query)
        sleep(0.7)
        press('enter')
        sleep(3)
        click(x=813, y=238)
        Speak('Done boss!')
    else:
        Speak("I am sorry boss! I can't process your demand.. I have limited functionalities, and I am in an experimental phase.")

    return


def ChromeAuto(query):
    """
    @param query = User's query
    Does all the automation related to Google.
    """
    from time import sleep
    from webbrowser import open
    from keyboard import press, press_and_release, write
    from word2number import w2n
    if 'new tab' in query:
        Speak('Processing your request...')
        press_and_release('ctrl + t')
    elif 'close tab' in query:
        Speak('Processing your request...')
        press_and_release('ctrl + w')
    elif 'new window' in query:
        if 'go' in query or 'jump' in query:
            Speak('Processing your request...')
            press_and_release('ctrl + t')
        else:
            Speak('Processing your request...')
            press_and_release('ctrl + n')
    elif 'history' in query:
        Speak('Processing your request...')
        press_and_release('ctrl + h')
    elif 'bookmark' in query:
        if 'make' in query or 'save' in query:
            Speak('Processing your request...')
            press_and_release('ctrl + d')
            sleep(1)
            press('enter')
        elif 'open' in query:
            Speak('Processing your request...')
            press_and_release('ctrl + shift + o')
    elif 'incognito' in query:
        Speak('Processing your request...')
        press_and_release('ctrl + shift + n')
    elif 'switch tab' in query:
        Speak('To which tab boss?')
        Speak('Once I start listening, please mention the tab number only, for example: 1, 2, 3 and so on..')
        
        tab_num = int(TakeCommand())
        Speak('Processing your request...')
        press_and_release(f'ctrl + {tab_num}')
    elif 'open' in query:
        query = query.replace('open', '')
        query = query.replace('levi', '')
        website_name = str(query)
        if 'whatsapp' in query:
            Speak('Processing your request...')
            open('web.whatsapp.com/', 2)
        elif 'youtube' in query:
            Speak('Processing your request...')
            open('www.youtube.com/', 2)
        elif 'instagram' in query:
            Speak('Processing your request...')
            open('www.instagram.com/', 2)
        elif 'facebook' in query:
            Speak('Processing your request...')
            open('www.facebook.com/', 2)
        else:
            Speak('Processing your request...')
            press_and_release('ctrl + t')
            press_and_release('shift + /')
            sleep(1)
            write(website_name)
            sleep(1)
            press('enter')
            sleep(1)
            for i in range(0, 21):
                press('tab')
            press('enter')
    elif 'zoom' in query:
        if 'in' in query:
            Speak('Processing your request...')
            press_and_release('ctrl + plus')
        elif 'out' in query:
            Speak('Processing your request...')
            press_and_release('ctrl + minus')
    elif 'print' in query:
        Speak('Processing your request...')
        press_and_release('ctrl + p')
    elif 'save' in query:
        Speak('Processing your request...')
        press_and_release('ctrl + s')
    elif 'reload' in query:
        Speak('Processing your request...')
        press_and_release('ctrl + r')
    elif 'scroll' in query:
        if 'up' in query:
            Speak('Processing your request...')
            press_and_release('up arrow')
        elif 'down' in query:
            Speak('Processing your request...')
            press_and_release('down arrow')
    else:
        Speak('Sorry boss! I have limited functionalities..')
    return


def Dict():
    """
    Does tasks such as finding meaning, synonym and antonym for the given word.
    """
    from PyDictionary import PyDictionary as Diction
    Speak("Activated dictionary..")
    Speak("Boss, what do you want to know? Please choose any one of the following:")
    ui.terminalPrint("1. For finding 'MEANING OF WORD' say 'Meaning of the word'")
    ui.terminalPrint("2. For finding 'SYNONYM OF WORD' say 'Synonym of the word'")
    ui.terminalPrint("3. For finding 'ANTONYM OF WORD' say 'Antonym of the word'")
    Speak('Once I start listening, Please say your choice boss..')
    choice = TakeCommand().lower()
    Speak("Okay boss!")
    if 'meaning' in choice:
        Speak("Once I start listening, please tell me the WORD, for which you want the MEANING of it..")
        
        word = TakeCommand()
        Speak('Processing your request...')
        result = Diction.meaning(word)
        Speak(f"The meaning for {word} is {result}")
    elif 'synonym' in choice:
        Speak("Once I start listening, please tell me the WORD, for which you want the SYNONYM of it..")
        
        word = TakeCommand()
        Speak('Processing your request...')
        result = Diction.synonym(word)
        Speak(f"The synonym for {word} is {result}")
    elif 'antonym' in choice:
        Speak("Once I start listening, please tell me the WORD, for which you want the ANTONYM of it..")
        
        word = TakeCommand()
        Speak('Processing your request...')
        result = Diction.antonym(word)
        Speak(f"The antonym for {word} is {result}")
    else:
        Speak("Invalid Input Boss! Please try again later..")
        return

    Speak("Job done boss! Now exiting from the dictionary..")
    Speak("Exited from the dictionary..")
    return


def SetAlarm():
    '''
    Sets an alarm, as per our need.
    '''
    Speak("Okay boss!")
    correct_time = False
    while not correct_time:
        Speak("NOTE: TELL ME THE TIME IN FOLLOWING FORMAT:")
        Speak("3 and 30 AM")
        Speak("12 and 30 PM")
        Speak("Now once I start listening, please tell me the time for which the alarm should be set..")
        
        time_query = TakeCommand().lower()
        time_query = time_query.replace(" and ", ":")
        Speak(
            f"Boss, you told me the time as {time_query}, Is it correct ? Please type Yes or No below:")
        correct_query = input("Type your choice: ").lower()
        if 'yes' in correct_query:
            fd = open("F:\\Ava - Personal AI Assistant\\AlarmData.txt", "a")
            fd.write(time_query)
            fd.close()
            Speak("Okay boss, your alarm has been set!")
            Speak("A new window will open, do not close that window, just minimize it.")
            correct_time = True
        elif 'no' in correct_query:
            Speak("Sorry boss! Let's try again...")
            continue
        else:
            Speak("Invalid Input! Try again later...")
            return
    os.startfile("F:\\Ava - Personal AI Assistant\\Alarm.py")
    return


def TakeHindi():
    '''
    Takes the input voice in Hindi
    '''
    command = sr.Recognizer()
    with sr.Microphone() as source:
        ui.updateMoviesDynamically('listening')
        ui.terminalPrint("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            ui.updateMoviesDynamically('loading')
            ui.terminalPrint("Recognizing....")
            query = command.recognize_google(audio, language='hi')
            ui.terminalPrint(f"You: {query}")

        except:
            return "None"

        return query.lower()


def TakeMarathi():
    '''
    Takes the input voice in Marathi
    '''
    command = sr.Recognizer()
    with sr.Microphone() as source:
        ui.updateMoviesDynamically('listening')
        ui.terminalPrint("Listening....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            ui.updateMoviesDynamically('loading')
            ui.terminalPrint("Recognizing....")
            query = command.recognize_google(audio, language='mr')
            ui.terminalPrint(f"You: {query}")

        except:
            return "None"

        return query.lower()


def Tran():
    '''
    Translates the user's queries into English, Marathi or Hindi language.
    '''
    from googletrans import Translator
    Speak("Okay boss, Please provide me the following details:")
    Speak("Please choose the source language:")
    ui.terminalPrint("1. For Hindi enter 'H' or 'h'")
    ui.terminalPrint("2. For Marathi enter 'M' or 'm'")
    ui.terminalPrint("3. For English enter 'E' or 'e'")
    src_lang = input("Enter your choice from above: ")
    src_lang = src_lang.lower()

    if 'h' in src_lang:
        Speak("Please choose the destination language:")
        ui.terminalPrint("1. For Marathi enter 'M' or 'm'")
        ui.terminalPrint("2. For English enter 'E' or 'e'")
        des_lang = input("Enter your choice from above: ")
        des_lang = des_lang.lower()

        if 'm' in des_lang:
            Speak("Speak something, which you want to translate..")
            line = TakeHindi()
            Speak('Processing your request...')
            translate = Translator()
            result = translate.translate(line, 'mr', 'hi')
            Text = result.text
            Speak("The Translation for this is" + Text)
            return
        elif 'e' in des_lang:
            Speak("Speak something, which you want to translate..")
            line = TakeHindi()
            Speak('Processing your request...')
            translate = Translator()
            result = translate.translate(line, 'en-in', 'hi')
            Text = result.text
            Speak("The Translation for this is" + Text)
            return
        else:
            Speak("You entered something wrong!")
            return
    elif 'm' in src_lang:
        Speak("Please choose the destination language:")
        ui.terminalPrint("1. For Hindi enter 'H' or 'h'")
        ui.terminalPrint("2. For English enter 'E' or 'e'")
        des_lang = input("Enter your choice from above: ")
        des_lang = des_lang.lower()

        if 'h' in des_lang:
            Speak("Speak something, which you want to translate..")
            line = TakeMarathi()
            Speak('Processing your request...')
            translate = Translator()
            result = translate.translate(line, 'hi', 'mr')
            Text = result.text
            Speak("The Translation for this is" + Text)
            return
        elif 'e' in des_lang:
            Speak("Speak something, which you want to translate..")
            line = TakeMarathi()
            Speak('Processing your request...')
            translate = Translator()
            result = translate.translate(line, 'en-in', 'mr')
            Text = result.text
            Speak("The Translation for this is" + Text)
            return
        else:
            Speak("You entered something wrong!")
            return
    elif 'e' in src_lang:
        Speak("Please choose the destination language:")
        ui.terminalPrint("1. For Hindi enter 'H' or 'h'")
        ui.terminalPrint("2. For Marathi enter 'M' or 'm'")
        des_lang = input("Enter your choice from above: ")
        des_lang = des_lang.lower()

        if 'h' in des_lang:
            Speak("Speak something, which you want to translate..")
            line = TakeCommand()
            Speak('Processing your request...')
            translate = Translator()
            result = translate.translate(line, 'hi', 'en-in')
            Text = result.text
            Speak("The Translation for this is" + Text)
            return
        elif 'm' in des_lang:
            Speak("Speak something, which you want to translate..")
            line = TakeCommand()
            Speak('Processing your request...')
            translate = Translator()
            result = translate.translate(line, 'mr', 'en-in')
            Text = result.text
            Speak("The Translation for this is" + Text)
            return
        else:
            Speak("You entered something wrong!")
            return
    else:
        Speak("You've entered something wrong! Try again later...")
        return


def RememberMsg(query):
    '''
    @param query = User's query.
    Let the assistant remember whatever the user has told it to remember.
    '''
    rememberMsg = query.replace("remember that", "")
    rememberMsg = rememberMsg.replace("levi", "")
    Speak("You told me to remind you that: "+rememberMsg)
    remember = open('RememberedData.txt', 'a+')
    remember.write("\n"+rememberMsg)
    remember.close()
    Speak('Done boss..')
    return


def HowToFunc(query):
    '''
    @param query = User's query
    Does search for the query like how to ...... ?
    '''
    from pywikihow import search_wikihow
    Speak("Getting data from the internet..")
    max_result = 1
    how_to_func = search_wikihow(query, max_result)
    assert len(how_to_func) == 1
    how_to_func[0].ui.terminalPrint()
    Speak(how_to_func[0].summary)
    Speak('Done boss...')
    return


def GoogleImage():
    '''
    Scraps the images for given search query.
    '''
    from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper
    Speak("Boss, I am also downloading some images related to your search.. Please wait..")
    fd1 = open("F:\\Ava - Personal AI Assistant\\Image_Scrapper.txt", "rt")
    query = str(fd1.read())
    fd1.close()

    fd2 = open("F:\\Ava - Personal AI Assistant\\Image_Scrapper.txt", "r+")
    fd2.truncate(0)
    fd2.close()

    web_driver = "F:\\Ava - Personal AI Assistant\\Webdriver\\chromedriver.exe"
    photos = "F:\\Ava - Personal AI Assistant\\Scrapped_Images"

    search_keys = [f"{query} free images"]
    number = 5
    head = False
    max = (1920, 1080)
    min = (0, 0)

    for search_key in search_keys:
        image_search = GoogleImageScraper(
            web_driver, photos, search_keys, number, head, min, max)
        image_url = image_search.find_image_urls()
        image_search.save_images(image_url)

    os.startfile(photos)
    return


def GoogleSearch():
    '''
    Does the google search according to the input query.
    '''
    Speak("Once I start listening, please tell me WHAT DO YOU WANT TO SEARCH?")
    
    query = TakeCommand()
    Speak('Processing your request...')
    if 'how to' in query:
        HowToFunc(query)
    else:
        write_data = str(query)
        fd = open("F:\\Ava - Personal AI Assistant\\Image_Scrapper.txt", "a")
        fd.write(write_data)
        fd.close()
        Speak("Okay boss! This is what i found for your search boss..")
        try:
            pywhatkit.search(query)
            GoogleImage()
            Speak('Done boss..!')
            return
        except:
            Speak("Sorry boss, no speakable data available")
            return


def Temp():
    '''
    Fetches the temperature for specific place.
    '''
    import requests
    from bs4 import BeautifulSoup
    Speak("Boss, please tell me the name of the place..")
    place = TakeCommand()
    Speak('Processing your request...')
    search = "Temperature in " + place
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    Speak(f"The Temperature outside is : {temperature}")
    return


def SpeedTest(query):
    '''
    Does the internet speed test.
    '''
    import speedtest
    Speak("Checking Speed...")
    test = speedtest.Speedtest()
    ui.terminalPrint("Loading server list...")
    test.get_servers()
    ui.terminalPrint("Choosing best server...")
    best = test.get_best_server()
    ui.terminalPrint(f"Found: {best['host']} located in {best['country']}")
    Speak("Performing download test...")
    download_result = test.download()
    Speak("Performing upload test...")
    upload_result = test.upload()
    if 'uploading' in query:
        Speak(f"Upload speed: {upload_result / 1024 / 1024:.2f} Mbps")
    elif 'downloading' in query:
        Speak(f"Download speed: {download_result / 1024 / 1024:.2f} Mbps")
    else:
        Speak(
            f"The Downloading speed is {download_result / 1024 / 1024:.2f}Mbps and Uploading speed is {upload_result / 1024 / 1024:.2f}Mbps")
    return


def WhatsappMsg():
    '''
    Sends a whatsapp message.
    '''
    Speak('Please tell me the name of the receiver as per you have saved it..')
    Speak('IMPORTANT: Please do not make any mistake while pronouncing the names..')
    name = TakeCommand().lower()
    ui.terminalPrint(f'You said:{name}')
    Speak('Great now, please type the message that you want to send:')
    Speak('IMPORTANT: Do not press enter, until and unless you have finished typing your entire message!')
    message = input('Type the message here: ')
    Speak('Processing your request...')
    pyautogui.press('win')
    sleep(1)
    pyautogui.write("Whatsapp")
    keyboard.press('enter')
    sleep(10)
    for i in range(0, 3):
        pyautogui.click(x=133, y=121)
        i = i+1
    keyboard.press('backspace')
    sleep(1)
    pyautogui.write(name)
    sleep(1)
    pyautogui.click(x=152, y=188)
    sleep(1)
    Speak('Sending the message..')
    pyautogui.write(message)
    keyboard.press('enter')
    Speak('Boss, message was sent successfully!')
    return


def OpenWhatsAppChat():
    '''
    Opens a whatsapp chat.
    '''
    Speak('Please type the first name of the person as per you have saved it:')
    firstname = input('Enter the first name here: ')
    Speak('Please type the last name of the person as per you have saved it:')
    Speak('IMPORTANT: If you do not have saved his or her last name then leave it blank and press enter..')
    lastname = input('Enter the last name here: ')
    name = "".join((firstname+lastname).split())
    Speak('Processing your request...')
    pyautogui.press('win')
    sleep(1)
    pyautogui.write("Whatsapp")
    keyboard.press('enter')
    sleep(10)
    for i in range(0, 3):
        pyautogui.click(x=133, y=121)
        i = i+1
    Speak('Opening the chat now...')
    keyboard.press('backspace')
    sleep(1)
    pyautogui.write(name)
    sleep(1)
    pyautogui.click(x=152, y=188)
    Speak('Done boss...')
    return


def WhatsappCall():
    '''
    Does a normal whatsapp call.
    '''
    Speak('Please type the first name of the receiver as per you have saved it:')
    firstname = input('Enter the first name here: ')
    Speak('Please type the last name of the receiver as per you have saved it:')
    Speak('IMPORTANT: If you do not have saved his or her last name then leave it blank and press enter..')
    lastname = input('Enter the last name here: ')
    name = "".join((firstname+lastname).split())
    Speak('Processing your request...')
    pyautogui.press('win')
    sleep(1)
    pyautogui.write("Whatsapp")
    keyboard.press('enter')
    sleep(10)
    for i in range(0, 3):
        pyautogui.click(x=133, y=121)
        i = i+1
    keyboard.press('backspace')
    sleep(1)
    pyautogui.write(name)
    sleep(1)
    pyautogui.click(x=152, y=188)
    Speak(f'Calling {firstname} {lastname} now..')
    sleep(1)
    pyautogui.click(x=1265, y=77)
    Speak('Done boss...')
    return


def WhatsappVideoCall():
    '''
    Does a whatsapp video call.
    '''
    Speak('Please type the first name of the receiver as per you have saved it:')
    firstname = input('Enter the first name here: ')
    Speak('Please type the last name of the receiver as per you have saved it:')
    Speak('IMPORTANT: If you do not have saved his or her last name then leave it blank and press enter..')
    lastname = input('Enter the last name here: ')
    name = "".join((firstname+lastname).split())
    Speak('Processing your request...')
    pyautogui.press('win')
    sleep(1)
    pyautogui.write("Whatsapp")
    keyboard.press('enter')
    sleep(10)
    for i in range(0, 3):
        pyautogui.click(x=133, y=121)
        i = i+1
    keyboard.press('backspace')
    sleep(1)
    pyautogui.write(name)
    sleep(1)
    pyautogui.click(x=152, y=188)
    Speak(f'Calling {firstname} {lastname} now..')
    sleep(1)
    pyautogui.click(x=1211, y=64)
    Speak('Done boss...')
    return


def GoogleMaps(place):
    from geopy.distance import great_circle
    from geopy.geocoders import Nominatim
    import geocoder
    import webbrowser as web
    url_place = f'https://www.google.com/maps/place/{str(place)}'
    geolocator = Nominatim(user_agent='myGeocoder')
    location = geolocator.geocode(place, addressdetails=True)
    target_latlng = location.latitude, location.longitude
    web.open(url_place, 2)
    location = location.raw['address']
    target = {
        'city': location.get('city', ''),
        'state': location.get('state', ''),
        'country': location.get('country', '')
    }

    current_loc = geocoder.ip('me')
    current_latlng = current_loc.latlng
    distance = str(great_circle(current_latlng, target_latlng))
    distance = str(distance.split(' ', 1)[0])
    distance = round(float(distance), 2)

    Speak(target)
    Speak(f'Boss, {place} is {distance}km away from your location..')
    return


def NotePad():
    '''
    Writes and saves note for the user.
    '''
    import string
    Speak('Okay boss!')
    Speak('Once I start listening please tell me what you want to write in it...')
    
    write_text = string.capwords(TakeCommand().lower())

    time = datetime.datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
    filename = f'{str(time)}-note.txt'

    with open(filename, 'w') as file:
        file.write(write_text)

    path_1 = f'F:\\Ava - Personal AI Assistant\\{str(filename)}'
    path_2 = f'F:\\Ava - Personal AI Assistant\\Notes\\{str(filename)}'

    os.rename(path_1, path_2)

    os.startfile(path_2)
    return


def CloseNotePad():
    '''
    Closes the notepad.
    '''
    os.system('TASKKILL /F /IM notepad.exe /T')
    Speak('Notepad closed..')
    return


def MyLocation():
    '''
    Gets the current location of the user based on his/her IP Address.
    '''
    import requests
    from webbrowser import open
    ip_add = requests.get('https://api.ipify.org').text
    url = f'https://get.geojs.io/v1/ip/geo/{ip_add}.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    region = geo_d['region']
    city = geo_d['city']
    country = geo_d['country']
    latitude = geo_d['latitude']
    longitude = geo_d['longitude']
    query = f'https://www.google.com/maps/@{latitude},{longitude}'
    open(query, 2, True)
    Speak(f'Boss, you are in {city} city, {region}, {country}')


state = ''


class leviMainClass(QThread):
    def __init__(self):
        super(leviMainClass, self).__init__()

    def run(self):
        click_on_chat_button()
        self.TaskExe()

    def TaskExe(self):
        Speak("Hello boss, I am your personal AI Assistant..")
        Speak("How can I assist you..?")
        while True:
            query = TakeCommand().lower()
            if 'hello' in query:
                if 'how are you' in query:
                    Speak("I am fine boss! What about you..?")
                else:
                    Speak(
                        "Hello boss! This is your personal AI Assistant. How can I help you?")
            elif 'search' in query and 'box' in query:
                pyautogui.press(['ctrl', 'e'])
            elif 'type' in query:
                Speak('Okay boss!')
                Speak('Once I start listening please tell me what do you want to type..')
                
                type_query = TakeCommand().lower()
                t.sleep(1)
                pyautogui.write(type_query)
                Speak('Done boss!')
            elif 'break' in query or 'sleep' in query or 'exit' in query:
                Speak("Ok boss! You can call me any time.. Bye..")
                quit(0)
            elif 'thank you' in query:
                Speak("It's my pleasure boss!")
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime('%I:%M %p')
                Speak(f'Boss, the time is {strTime}')
            elif 'date' in query:
                strDate = datetime.datetime.now().strftime('%d/%m/%Y')
                Speak(f'Boss, today it is {strDate}')
            elif 'youtube' in query and 'search' in query:
                Speak(
                    "Boss, once I start listening please tell me what do you want to search on youtube?")
                
                new_query = TakeCommand()
                web = 'https://www.youtube.com/results?search_query=' + new_query
                webbrowser.open(web)
                t.sleep(2)
                Speak("Done boss!")
            elif 'website' in query:
                Speak("Enter the address of the website you want to open: ")
                web_query = input()
                webbrowser.open(web_query)
                Speak("Ok boss! Launching...")
                t.sleep(2)
                Speak("Launched boss, have a look..")
            elif 'music' in query or 'song' in query:
                PlayMusic()
            elif 'wikipedia' in query:
                WikipediaSearch(query=query)
            elif 'open' in query and 'application' in query:
                Speak('Okay boss!')
                query = query.replace('open', '')
                query = query.replace('application' or 'app', '')
                pyautogui.press('win')
                pyautogui.write(query)
                keyboard.press('enter')
                Speak("I tried my best, I hope  I fulfilled your request properly!")
            elif 'open' in query and 'new tab' in query:
                keyboard.press_and_release('ctrl + t')
                t.sleep(2)
                Speak('New tab has been opened..')
            elif 'open' in query and 'new window' in query:
                keyboard.press_and_release('ctrl + n')
                t.sleep(2)
                Speak('New window has been opened..')
            elif 'close' in query and 'application' in query:
                Speak('Okay boss!')
                query = query.replace('close', '')
                query = query.replace('application' or 'app', '')
                pyautogui.press('win')
                pyautogui.write(query)
                keyboard.press('enter')
                Speak("I tried my best, I hope fulfilled your request properly!")
            elif 'close' in query and 'this window' in query:
                keyboard.press_and_release('alt + f4')
                t.sleep(2)
                Speak('Current window has been closed..')
            elif 'close' in query and 'this tab' in query:
                keyboard.press_and_release('ctrl + w')
                t.sleep(2)
                Speak('Current tab has been closed..')
            elif 'screenshot' in query:
                Screenshot()
            elif 'youtube' in query:
                YoutubeAuto(query)
            elif 'restart' in query:
                keyboard.press('0')
            elif 'pause' in query:
                keyboard.press('k')
            elif 'resume' in query:
                keyboard.press('k')
            elif 'full screen' in query:
                keyboard.press('f')
            elif 'film screen' in query:
                keyboard.press('t')
            elif 'skip' in query or 'foward' in query or 'seek' in query:
                keyboard.press('l')
            elif 'back' in query or 'backward' in query or 'seek' in query:
                keyboard.press('j')
            elif 'increase' in query and ('speed' in query or 'playback rate' in query):
                keyboard.press_and_release('shift + ,')
            elif 'decrease' in query and ('speed' in query or 'playback rate' in query):
                keyboard.press_and_release('shift + .')
            elif 'mute' in query:
                keyboard.press('m')
            elif 'unmute' in query:
                keyboard.press('m')
            elif 'play' in query and 'previous' in query:
                keyboard.press_and_release('shift + p')
            elif 'play' in query and 'next' in query:
                keyboard.press_and_release('shift + n')
            elif 'play' in query or 'search' in query:
                Speak('Okay boss!')
                Speak('Once I start listening please tell me, what you want to search?')
                
                search_query = TakeCommand().lower()
                Speak('Processing your request...')
                pyautogui.press('/')
                t.sleep(0.7)
                pyautogui.press(['shift', 'home', 'backspace'])
                t.sleep(0.7)
                pyautogui.write(search_query)
                t.sleep(0.7)
                pyautogui.press('enter')
                t.sleep(3)
                pyautogui.click(x=813, y=238)
                Speak('Done boss!')
            elif 'chrome' in query in query:
                ChromeAuto(query)
            elif 'history' in query:
                keyboard.press_and_release('ctrl + h')
                Speak('This is your history boss..')
            elif 'bookmark' in query:
                if 'make' in query or 'save' in query:
                    keyboard.press_and_release('ctrl + d')
                    keyboard.press('enter')
                elif 'open' in query:
                    keyboard.press_and_release('ctrl + shift + o')
            elif 'incognito' in query:
                keyboard.press_and_release('ctrl + shift + n')
                Speak('Incognito tab has been opened..')
            elif 'switch tab' in query:
                Speak('To which tab boss?')
                Speak(
                    'Once I start listening, please mention the tab number only, for example: 1, 2, 3 and so on..')
                
                tab_num = int(TakeCommand())
                keyboard.press_and_release(f'ctrl + {tab_num}')
                t.sleep(2)
                Speak('Done boss!')
            elif 'open' in query:
                query = query.replace('open', '')
                query = query.replace('levi', '')

                website_name = str(query)
                if 'web whatsapp' in query or 'whatsapp web' in query:
                    webbrowser.open('https://web.whatsapp.com/')
                    t.sleep(2)
                    Speak('Done boss!')
                elif 'youtube' in query:
                    webbrowser.open('https://www.youtube.com/')
                    t.sleep(2)
                    Speak('Done boss!')
                elif 'instagram' in query:
                    webbrowser.open('https://www.instagram.com/')
                    t.sleep(2)
                    Speak('Done boss!')
                elif 'facebook' in query:
                    webbrowser.open('https://www.facebook.com/')
                    t.sleep(2)
                    Speak('Done boss!')
                elif 'maps' in query:
                    webbrowser.open('https://www.google.com/maps/')
                    t.sleep(2)
                    Speak('Done boss!')
                else:
                    os.startfile(
                        'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
                    t.sleep(4)
                    pyautogui.press('ctrl, t')
                    pyautogui.press('shift, /')
                    pyautogui.write(website_name)
                    pyautogui.press('enter')
                    t.sleep(2)
                    pyautogui.press(keys='tab', presses=21)
                    pyautogui.press('enter')
                    t.sleep(1)
                    Speak('Done boss!')
            elif 'zoom' in query:
                if 'in' in query:
                    keyboard.press_and_release('ctrl + plus')
                elif 'out' in query:
                    keyboard.press_and_release('ctrl + minus')
            elif 'print' in query:
                keyboard.press_and_release('ctrl + p')
            elif 'save' in query:
                keyboard.press_and_release('ctrl + s')
            elif 'reload' in query:
                keyboard.press_and_release('ctrl + r')
            elif 'scroll' in query:
                if 'up' in query:
                    keyboard.press_and_release('up arrow')
                elif 'down' in query:
                    keyboard.press_and_release('down arrow')
            elif 'joke' in query:
                get = pyjokes.get_joke()
                Speak(get)
            elif 'repeat my words' in query:
                Speak("That sounds as a fun to me! Speak boss...")
                rpt = TakeCommand()
                Speak(f"You Said : {rpt}")
            elif 'my location' in query:
                Speak("Ok boss... Wait a second")
                MyLocation()
            elif 'dictionary' in query or 'meaning' in query or 'antonym' in query or 'synonym' in query:
                Dict()
            elif 'alarm' in query:
                SetAlarm()
            elif 'translator' in query or 'translate' in query:
                Tran()
            elif 'remember that' in query:
                RememberMsg(query)
            elif 'what do you remember' in query:
                remember = open('data.txt', 'r')
                Speak("You told me to remind you that: ", remember.read())
            elif 'google' in query and 'search' in query:
                GoogleSearch()
            elif 'temperature' in query:
                Temp()
            elif 'internet speed' in query or 'speed' in query:
                SpeedTest(query)
            elif 'how to' in query:
                HowToFunc(query)
            elif 'whatsapp' in query or 'chat' in query:
                Speak('Okay boss!')
                if 'message' in query:
                    WhatsappMsg()
                elif 'open' in query or 'chat' in query:
                    OpenWhatsAppChat()
                elif 'video call' in query:
                    WhatsappVideoCall()
                elif 'call' in query:
                    WhatsappCall()
            elif 'home' in query and 'screen' in query:
                pyautogui.press(['win', 'm'])
            elif 'minimize' in query or 'minimise' in query:
                if 'all' in query:
                    pyautogui.press(['win', 'm'])
                else:
                    pyautogui.press(['win', 'down'])
            elif 'maximize' in query or 'maximise' in query:
                if 'all' in query:
                    pyautogui.press(['win', 'shift', 'm'])
                else:
                    pyautogui.press(['win', 'up'])
            elif 'open' in query or 'show' in query and ('start' in query or 'search' in query):
                pyautogui.press('win')
            elif 'open' in query or 'show' in query and ('setting' in query or 'settings' in query):
                pyautogui.press(['win', 'i'])
            elif 'open' in query or 'show' in query and ('file explorer' in query or 'my computer' in query):
                pyautogui.press(['win', 'e'])
            elif 'open' in query and 'taskbar' in query and ('app' in query or 'application' in query):
                Speak('Okay boss!')
                Speak(
                    'Once I start listening please tell me the position of your specified application [for example: 1, 2, 3 ans so on..]')
                
                position = int(TakeCommand())
                Speak('Processing...')
                pyautogui.press(['win', f'{position}'])
                Speak("Done boss...")
            elif 'search' in query and ('file explorer' in query or 'my computer' in query):
                Speak('Okay boss!')
                Speak(
                    'Once I start listening please tell me what you want to search. For example folder name, file name, etc..')
                
                search_query = TakeCommand().lower()
                Speak('Processing...')
                pyautogui.press(['win', 'e'])
                t.sleep(2)
                pyautogui.press(['ctrl', 'e'])
                t.sleep(2)
                pyautogui.write(search_query)
                pyautogui.press(['enter'])
                Speak('This is what i found boss..')
            elif 'where is' in query:
                Speak(
                    'Boss, once I start listening please tell me the name of the place..')
                
                place_name = TakeCommand().title()
                GoogleMaps(place_name)
                Speak('Your request has been completed successfully!!')
            elif 'note' in query:
                if 'write' in query:
                    NotePad()
                    Speak('Here is your note boss!')
                if 'close' in query or 'dismiss' in query:
                    CloseNotePad()
                    Speak('Done boss!')
            else:
                query = query.lower()
                sendQuery(query)
                isBubbleLoaderVisible()
                response = retriveData()
                Speak(response)


startExecution = leviMainClass()


class Ui_LEVI(QWidget):
    def __init__(self):
        super(Ui_LEVI, self).__init__()
        self.leviUI = Ui_finalAiGui()
        self.leviUI.setupUi(self)
        self.leviUI.exitButton.clicked.connect(self.close)
        self.leviUI.enterButton.clicked.connect(self.manualCodeFromTerminal)
        self.runAllMovies()

    def manualCodeFromTerminal(self):
        command = self.leviUI.inputText.toPlainText()
        if command:
            cmd = self.leviUI.inputText.toPlainText()
            self.leviUI.inputText.clear()
            self.leviUI.terminalText.appendPlainText(f'You typed: {cmd}')

    def terminalPrint(self, text):
        self.leviUI.terminalText.appendPlainText(text)

    def updateMoviesDynamically(self, state):
        if state == 'speaking':
            self.leviUI.speakLbl.raise_()
            self.leviUI.speakLbl.show()
            self.leviUI.listenLbl.hide()
            self.leviUI.loadingLbl.hide()
        elif state == 'listening':
            self.leviUI.listenLbl.raise_()
            self.leviUI.listenLbl.show()
            self.leviUI.speakLbl.hide()
            self.leviUI.loadingLbl.hide()
        elif state == 'loading':
            self.leviUI.loadingLbl.raise_()
            self.leviUI.loadingLbl.show()
            self.leviUI.listenLbl.hide()
            self.leviUI.speakLbl.hide()
        else:
            self.leviUI.loadingLbl.raise_()
            self.leviUI.loadingLbl.show()
            self.leviUI.listenLbl.hide()
            self.leviUI.speakLbl.hide()

    def runAllMovies(self):
        self.leviUI.codinglbl = QtGui.QMovie(
            "F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Code_Template.gif")
        self.leviUI.codingWindow.setMovie(self.leviUI.codinglbl)
        self.leviUI.codinglbl.start()

        self.leviUI.loadingLable = QtGui.QMovie(
            "F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Earth.gif")
        self.leviUI.loadingLbl.setMovie(self.leviUI.loadingLable)
        self.leviUI.loadingLable.start()

        self.leviUI.speakLable = QtGui.QMovie(
            "F:/Ava - Personal AI Assistant/G.U.I Material/ExtraGui/Jarvis_Gui (1).gif")
        self.leviUI.speakLbl.setMovie(self.leviUI.speakLable)
        self.leviUI.speakLable.start()

        self.leviUI.listenLable = QtGui.QMovie(
            "F:/Ava - Personal AI Assistant/G.U.I Material/VoiceReg/Siri.gif")
        self.leviUI.listenLbl.setMovie(self.leviUI.listenLable)
        self.leviUI.listenLable.start()

        startExecution.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_LEVI()
    ui.show()
    sys.exit(app.exec_())
