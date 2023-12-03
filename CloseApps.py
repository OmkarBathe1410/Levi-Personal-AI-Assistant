import os
import keyboard
from pyautogui import press, write
from time import sleep
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180) 

def Speak(audio):
    engine.say(audio)
    print(f"Levi: {audio}")   
    engine.runAndWait()

def CloseApps(query):
  Speak("Ok boss... wait a second")
  if 'chrome' in query:
    os.system("TASKKILL /F /IM chrome.exe /T")   
    Speak("Your request has successfully been completed...")
    return
  elif 'whatsapp' in query:
    press('win')
    sleep(1)
    write('Whatsapp')
    sleep(1)
    keyboard.press('enter')    
    sleep(1)
    keyboard.press_and_release('alt + f4')
    Speak("Your request has successfully been completed...")
    return
  elif 'code' in query:
      os.system("TASKKILL /F /IM code.exe /T")
      Speak("Your request has successfully been completed...")
      return
  elif 'firefox' in query:
     os.system('TASKKILL /F /IM firefox.exe /T')
     Speak("Your request has successfully been completed...")
     return
  # Here you can add more applications as per your need...
  else:
      Speak("I am sorry boss! I can't process your demand.. I have limited functionalities, and I am in an experimental phase.")
      return
  



  