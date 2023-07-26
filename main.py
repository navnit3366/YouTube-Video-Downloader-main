from tkinter import * #installed pytube- python youtube package, imported tkinter
import tkinter.font
from pytube import YouTube
root = Tk()
Desired_font = tkinter.font.Font( family = "Comic Sans MS",size = 20,  weight = "bold") #standardizing format
root.geometry('700x300') #size of window
root.resizable(0,0)
root.title("Team U16 - Youtube Video Downloader") 

lbl = Label(root,text = 'Youtube Video Downloader')
lbl.pack()
 
link = StringVar()

lbl2 = Label(root, text = 'Paste Link Here:')
lbl2.pack()

link_enter = Entry(root, width = 70,textvariable = link) #entry widget
link_enter.pack()
 
def Downloader():     #function that downloads the file in mp4 format
    url =YouTube(str(link.get())) #url entered by user from entry widget
    video = url.streams.first()
    video.download()
    lbl3 = Label(root, text = 'DOWNLOADED')
    lbl3.pack()  
    lbl3.configure(font = Desired_font)
    lbl6 = Label(root, text = 'Check your home directory')
    lbl6.pack()

btn =Button(root,text = 'DOWNLOAD',bg = 'bisque2', padx = 2, command = Downloader)
btn.pack()
btn.configure(font = Desired_font) #configuring/assigning widgets with desired format

lbl.configure(font = Desired_font)
lbl2.configure(font = Desired_font) 
link_enter.configure(font = Desired_font)

root.mainloop()
