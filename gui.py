from tkinter import *
import tkinter
from PIL import Image, ImageTk

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
    w.create_image(0, 0, anchor=tkinter.NW, image=photo)

    line = w.create_line(event.x, 0, event.x, 450,fill="red")
    # w.tag_raise(line)
    print('{}, {}'.format(x, y))

def callback(event):
    print ("clicked at", event.x, event.y)

def key(event):
    if event.char == '\uf703':
        print('right')
    elif event.char == '\uf702':
        print('left')
    elif event.char == '\uf701':
        print('down')
    else:
        print("pressed", repr(event.char))

root = Tk()

# b = Canvas(root, width=650, height=100)
# b.pack()


image = Image.open("/Users/zackakil/Desktop/capture clean/1489359289.22.jpg")
photo = ImageTk.PhotoImage(image)
# label = Label(b,image=photo)
# label.image = photo # keep a reference!
# label.pack()

line = None
root.bind('<Motion>', motion)
root.bind("<Button-1>", callback)
root.bind("<Key>", key)
w = Canvas(root, width=650, height=500)

w.pack()
w.create_image(0, 0, anchor=tkinter.NW, image=photo)
# w.place(relx=0.0, rely=0.0)

# photo = PhotoImage(file="image.gif")



app = Application(master=root)
app.mainloop()
root.destroy()