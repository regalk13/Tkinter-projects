import tkinter as tk
from tkinter import *
root = tk.Tk()
root.title("Count words")

e2 = tk.StringVar()
e = tk.Entry(root, textvariable=e2, width=35, borderwidth=5)
e.pack()

def button_count():
    text = e2.get()
    words = text.split()

    frecuency = [words.count(w) for w in words]
    count = "Number of times the words are repeated: \n" + str(list(zip(words, frecuency)))
    myLabel = Label(root, text=count)
    myLabel.pack()

button = Button(root, text="Count your words.", command=button_count)
button.pack()
exit_button = Button(root, text="Exit", command=root.quit).pack()) 

root.mainloop()