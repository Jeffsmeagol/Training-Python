from pytube import YouTube

from tkinter import *




def Download():

    youtubeObject = YouTube(link.get())

    youtubeObject = youtubeObject.streams.get_lowest_resolution()

    try:

        youtubeObject.download()

    except:

        print("An error has occurred")

    print("Download is completed successfully")




top = Tk()

top.geometry('500x300')

L1 = Label(top,text="Paste the link")

L1.pack(anchor="center")

link = StringVar()

E1 = Entry(top,bd= 10,textvariable=link)

E1.pack(anchor="center")

B1 = Button(top,text="download",command=Download)

B1.pack(anchor="center")





#link = input("Enter the YouTube video URL: ")

#Download(link)




top.mainloop()