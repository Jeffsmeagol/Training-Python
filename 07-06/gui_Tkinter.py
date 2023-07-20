from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd

'''class Window(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    self.pack(fill=BOTH, expand=1)
    exitButton = Button(self, text='Exit', command=self.clickExitButton)
    exitButton.pack(x=0, y=0)

  def clickExitButton(self):
    print('gooooodmiiip')
    exit()

root = Tk()
app = Window(root)

root.wm_title('Tkinter button')
root.geometry('320x200')
root.mainloop()

class Window(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    menu = Menu(self.master)
    self.master.config(menu=menu)
    fileMenu = Menu(menu)
    fileMenu.add_command(label='item')
    fileMenu.add_command(label='Exit', command=self.exitProgram)
    menu.add_cascade(label='File', menu=fileMenu)
    editMenu = Menu(menu)
    editMenu.add_command(label='Undo')
    editMenu.add_command(label='Redo')
    menu.add_cascade(label='Edit', menu=editMenu)

    databaseMenu = Menu(menu)
    databaseMenu.add_command(label='insert', command=self.clickInsert)
    databaseMenu.add_command(label='update', command=self.clickUpdate)
    databaseMenu.add_command(label='print', command=self.clickPrint)
    databaseMenu.add_command(label='delete', command=self.clickDelete)
    menu.add_cascade(label='DB', menu=databaseMenu)

  def exitProgram(self):
    print('gooooodmiiip')
    exit()
  
  def clickInsert(self):
    print('inserted')

  def clickUpdate(self):
    print('updated')

  def clickPrint(self):
    print('print')

  def clickDelete(self):
    print('deleted')
root = Tk()
app = Window(root)
root.wm_title('Tkinter Window')
# root.geometry('320x200')
root.mainloop()

class Window(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    self.pack(fill=BOTH, expand=1)
    
    text = Label(self, text='Just do it')
    text.place(x=70,y=90)
    #text.pack()

root = Tk()
app = Window(root)
root.wm_title('Tkinter button')
root.geometry('200x200')
root.mainloop()

import time

class App(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    self.label = Label(text='', fg='Red', font=('Arial', 18))
    self.label.place(x=50, y=80)
    self.update_clock()
    
  def update_clock(self):
    now = time.strftime('%H:%M:%S')
    self.label.configure(text=now)
    self.after(1000, self.update_clock)

root = Tk()
app = App(root)
root.wm_title('Tkinter button')
root.geometry('200x200')
root.after(1000, app.update_clock)
root.mainloop()

from PIL import Image, ImageTk

class Window(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.master = master
    self.pack(fill=BOTH, expand=1)
    
    load = Image.open('Screenshot 2023-05-30 121014.png')
    render = ImageTk.PhotoImage(load)
    img = Label(self, image=render)
    img.image = render
    img.place(x=0, y=0)
    #text.pack()

root = Tk()
app = Window(root)
root.wm_title('Tkinter button')
root.geometry('200x200')
root.mainloop()

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

l = tk.Label(window, bg='white', fg='black', width=20, text='empty')
l.pack()

def print_selection(v):
  l.config(text='you have selected' + v)

s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection, fg='blue')
s.pack()
window.mainloop()

def say_hi():
  print('hello ~ !')

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

label = Label(frame1, text='Label', justify=LEFT, bg='red')
label.pack(side=LEFT)

hi_there = Button(frame2, text='say hi~', command=say_hi, bg='blue')
hi_there.pack()

frame1.pack(padx=1, pady=1)
frame2.pack(padx=10, pady=10)

root.mainloop()

root = Tk()
textLabel = Label(root,
                  text='Label',
                  justify=LEFT,
                  padx=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='Screenshot 2023-05-30 121014.png')
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)
mainloop()

import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

var1 = tk.StringVar()
l =tk.Label(window, bg='green', fg='yellow', font=('Arial', 12), width=10, textvariable=var1)
l.pack()

def print_selection():
  value = lb.get(lb.curselection())
  var1.set(value)

b1 = tk.Button(window, text='print selection',
               width=15, height=2, command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((1,2,3,4))
lb = tk.Listbox(window, listvariable=var1)

list_items = [11,22,33,44]
for item in list_items:
  lb.insert('end', 'item')
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()

window.mainloop()

import tkinter
import tkinter.messagebox

def buttonClick():
  tkinter.messagebox.showinfo('title', 'message')
  tkinter.messagebox.showwarning('title', 'message')
  tkinter.messagebox.showerror('title', 'message')

root = tkinter.Tk()
root.title('GUI')
root.geometry('100x100')
root.resizable(False, False)
tkinter.Button(root, text='hello button', command=buttonClick).pack()
root.mainloop()

import tkinter as tk
from tkinter import filedialog as fd

def callback():
  name = fd.askopenfilename()
  print(name)

errmsg = 'Error!'
tk.Button(text='Click to Open File',
          command=callback).pack(fill=tk.X)
tk.mainloop()
'''
