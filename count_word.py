import tkinter as tk
from tkinter import *
from collections import Counter
root = tk.Tk()
root.title("Count words")

e2 = tk.StringVar()
e = tk.Entry(root, textvariable=e2, width=35, borderwidth=5)
e.pack()

def countWords(s):
    signos = [',', '.', ';', ':']
    cleanstr = ''
    for letra in s.lower():
        if letra in signos:
            cleanstr += ''
        else:
            cleanstr += letra
    strlist = cleanstr.split(' ')
    return Counter(strlist)

def button_count():
    text = e2.get()

    count = countWords(text)
    myLabel = Label(root, text=count)
    myLabel.pack()

button = Button(root, text="Count words", command=button_count)
button.pack()
exit_button = Button(root, text="Exit", command=root.quit).pack()


root.mainloop()