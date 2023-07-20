'''from tkinter import *

top = Tk()
L1 = Label(top, text='Label')
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side=RIGHT)

top.mainloop()
'''
import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

# e1 = tk.Entry(window, show=None, font=('Arial', 14))
# e2 = tk.Entry(window, show='*', font=('Arial', 14))
# e1.pack()
# e2.pack()

# window.mainloop()

var = tk.StringVar()
l = tk.Label(window, bg='white', width=20, text='empty')
l.pack()

def print_selection():
  l.config(text='you have selected  ' + var.get())

r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A')
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B')
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C')
r3.pack()
bt = tk.Button(window, text='Just Press', command=print_selection)
bt.pack()
var.set('B')

window.mainloop()