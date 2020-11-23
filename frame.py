from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Frame leccion')
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

frame = LabelFrame(root, text="new frame", padx=5, pady=5)
frame.pack()

b = Button(text="Click, click")
b.pack


root.mainloop()
