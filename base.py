from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Base")
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

def open():
    global my_img
    top = Toplevel()
    top.title("New window")
    img2 = PhotoImage(file='images/icon.png')
    top.tk.call('wm', 'iconphoto', top._w, img2)
    my_img = ImageTk.PhotoImage(Image.open("images/mountain.jpeg"))
    lbl = Label(top, image=my_img).pack()
    btn2 = Button(top, text="Exit", command=top.destroy).pack()


btn = Button(root, text="Open window", command=open).pack()

root.mainloop()