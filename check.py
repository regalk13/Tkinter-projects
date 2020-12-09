from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("check")
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("400x400")


def show():
    mylabel = Label(root, text=var.get()).pack()
    
var = StringVar()

c = Checkbutton(root, text="check", variable=var, onvalue="yes", offvalue="Noo")
c.deselect()
c.pack()

myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()

