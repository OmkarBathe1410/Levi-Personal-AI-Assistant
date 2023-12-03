import speech_recognition as sr
import os

def TakeCommand():
    command = sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source :
        # command.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

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
        os.startfile('F:\Ava - Personal AI Assistant\ModernAI.py')
    else:
        pass

while True:
    WakeUpDetected()