from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Frame leccion')
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

frame = LabelFrame(root, text="new frame", padx=5, pady=5)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Click, click")
b2 = Button(frame, text="Now here")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
