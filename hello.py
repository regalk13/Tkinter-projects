from tkinter import *

root = Tk()


e = Entry(root, width=50, bg="blue", fg="white")
e.pack()
e.insert(0, "Enter your Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello).pack()

myButton = Button(root, text="enter your name", padx=50, pady=50, command=myClick, fg="blue", bg="green").pack()

root.mainloop()
