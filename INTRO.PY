from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
import pygame
from pygame import mixer
import threading
from jarvis import Main
# mixer.init()

root = Tk()
root.geometry("1400x800")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open(r"C:\Users\shree\Desktop\projects\ML project\static\jarvis.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i=0
    # mixer.music.load("music path")
    # mixer.music.play()

    for img_frame in ImageSequence.Iterator(img):
        img_frame = img_frame.resize((1400,800))
        img_tk = ImageTk.PhotoImage(img_frame)
        lbl.config(image=img_tk)
        lbl.img = img_tk
        root.update()
        time.sleep(0.05)
    
    root.destroy()
    
def start_gif_thread():
    gif_thread = threading.Thread(target=play_gif)
    gif_thread.start()
    

def start_jarvis_thread():
    jarvis_thread = threading.Thread(target=Main)
    jarvis_thread.start()

start_button = Button(root, text="Start Gif", command=start_gif_thread)
start_jarvis_button = Button(root, text="Start Jarvis", command=start_jarvis_thread)

start_button.pack()
start_jarvis_button.pack()

root.mainloop()