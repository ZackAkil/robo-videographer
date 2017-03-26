from tkinter import *
import tkinter
from PIL import Image, ImageTk
from os import listdir
from os.path import isfile, join
import pandas as pd
import image_label_nav
import os.path


LABEL_CSV = 'rugby_image_labels.csv'

if os.path.exists(LABEL_CSV):
    ilc = image_label_nav.Image_Label_Cycler("/Users/zackakil/Desktop/capture clean", LABEL_CSV)
else: 
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
    w.create_line(event.x, 0, event.x, 450,fill="red")
    display_photo_label_line()

    print('{}, {}'.format(x, y))

def display_photo_label_line():
    photo_line_pos = ilc.get_current_pos_value()
    if photo_line_pos:
        w.create_line(photo_line_pos, 0, photo_line_pos, 450,fill="blue")

def callback(event):
    ilc.set_current_pos_value(event.x)
    display_photo_label_line()
    ilc.next_photo()
    display_image(ilc.current_image_name)
    print ("clicked at", event.x, event.y)
    ilc.save_labels(LABEL_CSV)

def callback2(event):
    ilc.set_current_pos_value(None)
    display_photo_label_line()
    ilc.next_photo()
    display_image(ilc.current_image_name)
    print ("dump clicked at", event.x, event.y)
    ilc.save_labels(LABEL_CSV)

def display_image(file_name):
    print('file to open', file_name)
    image = Image.open(IMAGE_FOLDER_PATH + file_name)
    photo = ImageTk.PhotoImage(image)
    w.delete("all")
    w.create_image(0, 0, anchor=tkinter.NW, image=photo)
    display_photo_label_line()
    global current_photo
    current_photo = photo

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


root = Tk()
IMAGE_FOLDER_PATH = "/Users/zackakil/Desktop/capture clean/"
current_photo = None
# mouse_line = None
# photo_line = None

w = Canvas(root, width=650, height=500)
w.pack()

w.bind('<Motion>', motion)
w.bind("<Button-1>", callback)
w.bind("<Button-2>", callback2)
root.bind("<Key>", key)


display_image(ilc.current_image_name)



app = Application(master=root)
app.mainloop()
root.destroy()