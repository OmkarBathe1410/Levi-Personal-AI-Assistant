# import webbrowser
# import keyboard
# import pyjokes
# import os
# import pyautogui
# import datetime      
# import time as t
# from GoogleMaps import GoogleMaps
# from YoutubeAutomation import YoutubeAuto
# import MusicModule as Music
# import Temp
# import Dict
# import Screenshot
# import Tran
# import CloseApps
# import SpTest
# import Remember
# import GoogleSearch
# import HowTo
# import WikipediaSearch
# import Whatsapp
# from Speak import Speak
# from TakeCommand import TakeCommand
# import AlarmSetter
# import ChromeAutomation
# from NotePad import NotePad, CloseNotePad
# from googletrans import Translator
# from LeviChatBot import *

# # def TranslateInHindi(query, src):
# #     translate = Translator()
# #     result = translate.translate(text=query, dest='hi')
# #     result = result.text
# #     return result

# # def TranslateInMarathi(query, src):
# #     translate = Translator()
# #     result = translate.translate(text=query, dest='mr', src=src)
# #     result = result.text
# #     return result

# click_on_chat_button()
# def TaskExe():
#     Speak("Hello boss, I am your personal AI Assistant..")
#     Speak("How can I assist you..?")

#     while True:
#         query = TakeCommand()
#         if 'hello' in query:
#             if 'how are you' in query:
#                 Speak("I am fine boss! What about you..?")
#             else:
#                 Speak("Hello boss! This is your personal AI Assistant. How can I help you?")
#         elif 'search' in query and 'box' in query:
#             pyautogui.press(['ctrl', 'e'])
#         elif 'type' in query:
#             Speak('Okay boss!')
#             Speak('Once I start listening please tell me what do you want to type..')
#             Speak('Listening...')
#             type_query = TakeCommand().lower()
#             t.sleep(1)
#             pyautogui.write(type_query)
#             Speak('Done boss!')
#         elif 'break' in query or 'sleep' in query or 'exit' in query:
#             Speak("Ok boss! You can call me any time.. Bye..")
#             quit(0)
#         elif 'thank you' in query:
#             Speak("It's my pleasure boss!")
#         elif 'time' in query:
#             strTime = datetime.datetime.now().strftime('%I:%M %p')
#             Speak(f'Boss, the time is {strTime}')
#         elif 'date' in query:
#             strDate = datetime.datetime.now().strftime('%d/%m/%Y')
#             Speak(f'Boss, today it is {strDate}')
#         elif 'youtube' in query and 'search' in query:
#             Speak("Boss, once I start listening please tell me what do you want to search on youtube?")
#             Speak('Listening...')
#             new_query = TakeCommand()
#             web = 'https://www.youtube.com/results?search_query=' + new_query
#             webbrowser.open(web)
#             t.sleep(2)
#             Speak("Done boss!")
#         elif 'website' in query:
#             Speak("Enter the address of the website you want to open: ")
#             web_query = input()
#             webbrowser.open(web_query)
#             Speak("Ok boss! Launching...")
#             t.sleep(2)
#             Speak("Launched boss, have a look..")     
#         elif 'music' in query or 'song' in query:
#             Music.PlayMusic()
#         elif 'wikipedia' in query:
#             WikipediaSearch.WikipediaSearch(query)
#         elif 'open' in query and 'application' in query:
#             Speak('Okay boss!')
#             query = query.replace('open', '')
#             query = query.replace('application' or 'app', '')
#             pyautogui.press('win')
#             pyautogui.write(query)
#             keyboard.press('enter')
#             Speak("I tried my best, I hope fulfilled your request properly!")
#         elif 'open' in query and 'new tab' in query:
#             keyboard.press_and_release('ctrl + t')
#             t.sleep(2)
#             Speak('New tab has been opened..')
#         elif 'open' in query and 'new window' in query:
#             keyboard.press_and_release('ctrl + n')
#             t.sleep(2)
#             Speak('New window has been opened..')
#         elif 'close' in query and 'application' in query:
#             Speak('Okay boss!')
#             query = query.replace('close', '')
#             query = query.replace('application' or 'app', '')
#             pyautogui.press('win')
#             pyautogui.write(query)
#             keyboard.press('enter')
#             Speak("I tried my best, I hope fulfilled your request properly!")
#         elif 'close' in query and 'this window' in query:
#             keyboard.press_and_release('alt + f4')
#             t.sleep(2)
#             Speak('Current window has been closed..')
#         elif 'close' in query and 'this tab' in query:
#             keyboard.press_and_release('ctrl + w')
#             t.sleep(2)
#             Speak('Current tab has been closed..')
#         elif 'screenshot' in query:
#             Screenshot.Screenshot()  
#         elif 'youtube' in query:
#             YoutubeAuto(query)
#         elif 'restart' in query:
#             keyboard.press('0')
#         elif 'pause' in query:
#             keyboard.press('k')
#         elif 'resume' in query:
#             keyboard.press('k')
#         elif 'full screen' in query:
#             keyboard.press('f')
#         elif 'film screen' in query:
#             keyboard.press('t')
#         elif 'skip' in query or 'foward' in query or 'seek' in query:
#             keyboard.press('l')
#         elif 'back' in query or 'backward' in query or 'seek' in query:
#             keyboard.press('j')
#         elif 'increase' in query and ('speed' in query or 'playback rate' in query):
#             keyboard.press_and_release('shift + ,')
#         elif 'decrease' in query and ('speed' in query or 'playback rate' in query):
#             keyboard.press_and_release('shift + .')
#         elif 'mute' in query:
#             keyboard.press('m') 
#         elif 'unmute' in query:
#             keyboard.press('m') 
#         elif 'play' in query and 'previous' in query:
#             keyboard.press_and_release('shift + p')
#         elif 'play' in query and 'next' in query:
#             keyboard.press_and_release('shift + n')
#         elif 'play' in query or 'search' in query:
#             Speak('Okay boss!')
#             Speak('Once I start listening please tell me, what you want to search?')
#             Speak('Listening...')
#             search_query = TakeCommand().lower()
#             Speak('Processing your request...')
#             pyautogui.press('/')
#             t.sleep(0.7)
#             pyautogui.press(['shift', 'home', 'backspace'])
#             t.sleep(0.7)
#             pyautogui.write(search_query)
#             t.sleep(0.7)
#             pyautogui.press('enter')
#             t.sleep(3)
#             pyautogui.click(x=813, y=238)
#             Speak('Done boss!')                         
#         elif 'chrome' in query in query:
#             ChromeAutomation.ChromeAuto(query)
#         elif 'history' in query:
#             keyboard.press_and_release('ctrl + h')
#             Speak('This is your history boss..')
#         elif 'bookmark' in query:
#             if 'make'in query or 'save' in query:
#                 keyboard.press_and_release('ctrl + d')
#                 keyboard.press('enter')
#             elif 'open' in query:
#                 keyboard.press_and_release('ctrl + shift + o')
#         elif 'incognito' in query:
#             keyboard.press_and_release('ctrl + shift + n')
#             Speak('Incognito tab has been opened..')
#         elif 'switch tab' in query:
#             Speak('To which tab boss?')
#             Speak('Once I start listening, please mention the tab number only, for example: 1, 2, 3 and so on..')
#             Speak('Listening...')
#             tab_num = int(TakeCommand())
#             keyboard.press_and_release(f'ctrl + {tab_num}')
#             t.sleep(2)
#             Speak('Done boss!')
#         elif 'open' in query:
#             query = query.replace('open', '')
#             query = query.replace('levi', '')
            
#             website_name = str(query)
#             if 'web whatsapp' in query or 'whatsapp web' in query:
#                 webbrowser.open('https://web.whatsapp.com/')
#                 t.sleep(2)
#                 Speak('Done boss!')
#             elif 'youtube' in query:
#                 webbrowser.open('https://www.youtube.com/')
#                 t.sleep(2)
#                 Speak('Done boss!')
#             elif 'instagram' in query:
#                 webbrowser.open('https://www.instagram.com/')
#                 t.sleep(2)
#                 Speak('Done boss!')
#             elif 'facebook' in query:
#                 webbrowser.open('https://www.facebook.com/')
#                 t.sleep(2)
#                 Speak('Done boss!')
#             elif 'maps' in query:
#                 webbrowser.open('https://www.google.com/maps/')
#                 t.sleep(2)
#                 Speak('Done boss!')
#             else:
#                 os.startfile('C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
#                 t.sleep(4)
#                 pyautogui.press('ctrl, t')
#                 pyautogui.press('shift, /')
#                 pyautogui.write(website_name)
#                 pyautogui.press('enter')
#                 t.sleep(2)
#                 pyautogui.press(keys='tab', presses=21)
#                 pyautogui.press('enter')
#                 t.sleep(1)
#                 Speak('Done boss!')
#         elif 'zoom' in query:
#             if 'in' in query:
#                 keyboard.press_and_release('ctrl + plus')
#             elif 'out' in query:
#                 keyboard.press_and_release('ctrl + minus')
#         elif 'print' in query:
#             keyboard.press_and_release('ctrl + p')
#         elif 'save' in query:
#             keyboard.press_and_release('ctrl + s')
#         elif 'reload' in query:
#             keyboard.press_and_release('ctrl + r')
#         elif 'scroll' in query:
#             if 'up' in query:
#                 keyboard.press_and_release('up arrow')
#             elif 'down' in query:
#                 keyboard.press_and_release('down arrow') 
#         elif 'joke' in query:
#             get = pyjokes.get_joke()
#             Speak(get)    
#         elif 'repeat my words' in query:
#             Speak("That sounds as a fun to me! Speak boss...")            
#             rpt = TakeCommand()
#             Speak(f"You Said : {rpt}")
#         elif 'my location' in query:
#             Speak("Ok boss... Wait a second") 
#             webbrowser.open("https://www.google.com/maps/")
#         elif 'dictionary' in query or 'meaning' in query or 'antonym' in query or 'synonym' in query:
#             Dict.Dict()
#         elif 'alarm' in query:
#             AlarmSetter.SetAlarm()
#         elif 'translator' in query or 'translate' in query:
#             Tran.Tran()
#         elif 'remember that' in query:
#             Remember.RememberMsg(query)
#         elif 'what do you remember' in query:
#             remember = open('data.txt','r')
#             Speak("You told me to remind you that: ", remember.read())
#         elif 'google' in query and 'search' in query:
#             GoogleSearch.GoogleSearch()
#         elif 'temperature' in query:
#             Temp.Temp()
#         # elif 'read book' in query:
#         #     Reader()
#         elif 'internet speed' in query or 'speed' in query:
#             SpTest.SpeedTest(query)
#         elif 'how to' in query:
#             HowTo.HowToFunc(query)
#         elif 'whatsapp' in query or 'chat' in query:
#             Speak('Okay boss!')
#             if 'message' in  query:
#                 Whatsapp.WhatsappMsg()
#             elif 'open' in query or 'chat' in query:
#                 Whatsapp.OpenWhatsAppChat()
#             elif 'video call' in query:
#                 Whatsapp.WhatsappVideoCall()
#             elif 'call' in query:
#                 Whatsapp.WhatsappCall()
#         elif 'home' in query and 'screen' in query:
#             pyautogui.press(['win', 'm'])
#         elif 'minimize' in query or 'minimise' in query:
#             if 'all' in query:
#                 pyautogui.press(['win', 'm'])
#             else:
#                 pyautogui.press(['win', 'down'])
#         elif 'maximize' in query or 'maximise' in query:
#             if 'all' in query:
#                 pyautogui.press(['win', 'shift', 'm'])
#             else:
#                 pyautogui.press(['win', 'up'])
#         elif 'open' in query or 'show' in query and ('start' in query or 'search' in query):
#             pyautogui.press('win')
#         elif 'open' in query or 'show' in query and ('setting' in query or 'settings' in query):
#             pyautogui.press(['win','i'])
#         elif 'open' in query or 'show' in query and ('file explorer' in query or 'my computer' in query):
#             pyautogui.press(['win', 'e'])
#         elif 'open' in query and 'taskbar' in query and ('app' in query or 'application' in query):
#             Speak('Okay boss!')
#             Speak('Once I start listening please tell me the position of your specified application [for example: 1, 2, 3 ans so on..]')
#             Speak('Listening...')
#             position = int(TakeCommand())
#             Speak('Processing...')
#             pyautogui.press(['win', f'{position}'])
#             Speak("Done boss...")
#         elif 'search' in query and ('file explorer' in query or 'my computer' in query):
#             Speak('Okay boss!')
#             Speak('Once I start listening please tell me what you want to search. For example folder name, file name, etc..')
#             Speak('Listening...')
#             search_query = TakeCommand().lower()
#             Speak('Processing...')
#             pyautogui.press(['win', 'e'])
#             t.sleep(2)
#             pyautogui.press(['ctrl', 'e'])
#             t.sleep(2)
#             pyautogui.write(search_query)
#             pyautogui.press(['enter'])
#             Speak('This is what i found boss..')
#         elif 'where is' in query:
#             Speak('Boss, once I start listening please tell me the name of the place..')
#             Speak('Listening...')
#             place_name = TakeCommand().title()
#             GoogleMaps(place_name)
#             Speak('Your request has been completed successfully!!')
#         elif 'note' in query:
#             if 'write' in query:
#                 NotePad()
#                 Speak('Here is your note boss!')
#             if 'close' in query or 'dismiss' in query:
#                 CloseNotePad()
#                 Speak('Done boss!')
#         else:
#             query = query.lower()
#             sendQuery(query)
#             isBubbleLoaderVisible()
#             response = retriveData()
#             Speak(response)
    
# TaskExe()