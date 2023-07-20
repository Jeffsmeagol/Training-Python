import wikipedia
import os
from tkinter import *
from gtts import gTTS

# result = wikipedia.summary('canton concourse', sentences=5)
# print(result)

def dowork():
  result = wikipedia.summary(var.get(), sentences=5)
  print(result)
  language = 'en'
  myobj = gTTS(text=result,lang=language,slow=False)
  myobj.save("voice2.mp3")
  # os.system("MediaPlayer voice2.mp3")

top = Tk()
L1 = Label(top,text="Label")
L1.pack(side=LEFT)
var = StringVar()
E1 = Entry(top,bd= 5,textvariable=var)
E1.pack(side=LEFT)
B1 = Button(top,text="Process",command=dowork)
B1.pack()

top.mainloop()