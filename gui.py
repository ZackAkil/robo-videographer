from tkinter import *
import tkinter
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile, join
import pandas as pd

import image_label_nav

ilc = image_label_nav.Image_Label_Cycler("/Users/zackakil/Desktop/capture clean")

class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

def motion(event):
    x, y = event.x, event.y
    w.delete("all")
    w.create_image(0, 0, anchor=tkinter.NW, image=current_photo)
    line = w.create_line(event.x, 0, event.x, 450,fill="red")
    print('{}, {}'.format(x, y))

def callback(event):
    print ("clicked at", event.x, event.y)

root = Tk()
IMAGE_FOLDER_PATH = "/Users/zackakil/Desktop/capture clean/"
current_photo = None

def display_image(file_name):
    print('file to open', file_name)
    image = Image.open(IMAGE_FOLDER_PATH + file_name)
    photo = ImageTk.PhotoImage(image)
    w.delete("all")
    w.create_image(0, 0, anchor=tkinter.NW, image=photo)
    global current_photo
    current_photo = photo

line = None
root.bind('<Motion>', motion)
root.bind("<Button-1>", callback)

w = Canvas(root, width=650, height=500)
w.pack()

display_image(ilc.current_image_name)

def key(event):
    if event.char == '\uf703':
        print('right')
        ilc.next_photo()
        display_image(ilc.current_image_name)
    elif event.char == '\uf702':
        ilc.next_photo(-1)
        display_image(ilc.current_image_name)
        print('left')
    elif event.char == '\uf701':
        print('down')
    else:
        print("pressed", repr(event.char))

root.bind("<Key>", key)

app = Application(master=root)
app.mainloop()
root.destroy()