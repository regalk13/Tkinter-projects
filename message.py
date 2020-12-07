from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()
root.title("Message")
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askquestion("This is my Popup", "Hello world")
    if response == "yes":
        Label(root, text="Yess!").pack()
    else:
        Label(root, text="Nooo!").pack()

Button(root, text="Popup", command=popup).pack()

mainloop()