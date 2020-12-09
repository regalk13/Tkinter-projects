from tkinter import *
from PIL  import Image,ImageTk

root = Tk()
root.title("dropdown")
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("400x400")

def show():
    label = Label(root, text=clicked.get()).pack()


options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "All days"
]

clicked = StringVar()
clicked.set(options[0])


drop = OptionMenu(root, clicked, *options)
drop.pack()

myB = Button(root, text="Show selection", command=show).pack()

root.mainloop()