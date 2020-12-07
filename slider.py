from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Slider")
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide():
    label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)

btn = Button(root, text="Change geometry", command=slide).pack()

horizontal.pack()

horizontal.get()


root.mainloop()