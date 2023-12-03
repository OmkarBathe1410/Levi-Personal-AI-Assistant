import os
from playsound import playsound
import datetime

extracted_time = open("F:\\Ava - Personal AI Assistant\\AlarmData.txt", "rt")
time_to_set = extracted_time.read()
extracted_time.close()

time_to_set = str(time_to_set)

delete_time = open("F:\\Ava - Personal AI Assistant\\AlarmData.txt", "r+")
delete_time.truncate(0)
delete_time.close()

def convert24(time):
    t = datetime.datetime.strptime(time, '%I:%M %p')
    return t.strftime('%H:%M')

def Ringer(time_to_set):
  time_to_print = time_to_set
  if 'p.m.' in time_to_set:
    time_to_set = time_to_set.replace('p.m.', 'pm')
  elif 'a.m.':
    time_to_set = time_to_set.replace('a.m.', 'am')
  
  time_to_set = convert24(time_to_set)

  while True:
    current_time = datetime.datetime.now().strftime('%H:%M')

    if current_time == time_to_set:
      print(f"It's {time_to_print} boss! Wake up...")
      playsound("F:\\Ava - Personal AI Assistant\\alarm.mp3")
    elif current_time > time_to_set:
      break

Ringer(time_to_set)