import speech_recognition as sr
import wikipedia
import os
from tkinter import *
from gtts import gTTS

def spt():
  # Initialize the recognizer
  r = sr.Recognizer()

  # Open the microphone and start recording
  with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

  try:
    # Use Google Speech Recognition to convert audio to text
    text = r.recognize_google(audio)
    print("You said:", text)
    return "You said:", text
  
  except sr.UnknownValueError:
    print("Sorry, I could not understand your speech.")
    return "Sorry, I could not understand your speech."

  except sr.RequestError as e:
    print("Sorry, an error occurred. Error: ", str(e))
    return "Sorry, an error occurred. Error: ", str(e)

def dowork():
  var1 = spt()
  L1.config(text=var1)
  result = wikipedia.summary(var1, sentences=2)
  print(result)
  L1.config(text='your search result  ' + result)
  language = 'en'
  myobj = gTTS(text=result, lang=language, slow=False)
  myobj.save("voice1.mp3")

top = Tk()
L1 = Label(top,text="Your Word... ")
L1.pack(side=LEFT)
# var = StringVar()
# E1 = Entry(top,bd= 5,textvariable=var)
# E1.pack(side=LEFT)
B1 = Button(top,text="Speak",command=dowork)
B1.pack()

top.mainloop()