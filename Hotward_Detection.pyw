import speech_recognition as sr
import os

def TakeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source, 0, 8)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio,language='en-in')
            print(f"You: {query}")

        except :
            return "None"

        return query.lower()

def WakeUpDetected():
    wake_up = TakeCommand().lower()
    if 'wake up' in wake_up:
        os.startfile('F:/Ava - Personal AI Assistant/main.py')
    else:
        pass

while True:
    WakeUpDetected()