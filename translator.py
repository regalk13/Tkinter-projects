import tkinter as tk
import winsound
from tkinter import *

root = tk.Tk()
root.title("Translator Morse")
root.geometry("460x450")
img = PhotoImage(file='images/morse.png')
root.tk.call('wm', 'iconphoto', root._w, img)

letter = tk.StringVar()
morse = tk.StringVar()

alphabet_morse = {
	"a": ".-/",
	"b": "-.../",
	"c": "-.-./",
	"d": "-../",
	"e": "./",
	"f": "..-./",
	"g": "--./",
	"h": "..../",
	"i": "../",
	"j": ".---/",
	"k": "-.-/",
	"l": ".-../",
	"m": "--/",
	"n": "-./",
	"o": "---/",
	"p": ".--./",
	"q": "--.-/",
	"r": ".-./",
	"s": ".../",
	"t": "-/",
	"u": "..-/",
	"v": "...-/",
	"w": ".--/",
	"y": "-..-/",
	"x": "-.--/",
	"z": "--../",
	" ": "/"
}

letter_to_morse = {
	".-": "A",
	"-...": "B",
	"-.-.": "C",
	"-..": "D",
	".": "E",
	"..-. ": "F",
	"--. ": "G",
	"....": "H",
	"..": "I",
	".---": "J",
	"-.-": "K",
	".-..": "L",
	"--": "M",
	"-.": "N",
	"---": "O",
	".--.": "P",
	"--.-": "Q",
	".-.": "R",
	"...": "S",
	"-": "T",
	"..-": "U",
	"...-": "V",
	".--": "W",
	"-..-": "X",
	"-.--": "Y",
	"--..": "Z",
}

def translate(letter):
	try:
		inp = letter
		res = ""
		for part in inp:
			res += alphabet_morse[part]
		return res

	except KeyError:
		return "Insert a valid string"
    
def translate_morse(message):
	try:
		inp = message
		res = ""
		for part in inp.split("/"):
			res += letter_to_morse[part]
		print(res)

		return res

	except KeyError:
		return "Insert a valid morse"

def play(morse):
		for x in morse:
			if x == '.':
				winsound.Beep(3799, 500)

			elif x == '-':
				winsound.Beep(3799, 1000)
	
			else:
				continue

def button1():
	global tt
	tt = translate(letter.get())	
	entrytt = Entry(root, width=50, bg="#f1f1f1", borderwidth=0)
	entrytt.insert(0, "The text in morse is: " + str(tt))
	entrytt.grid(row=2, column=0)

def button2():
	tm = translate_morse(morse.get())
	entrytm = Entry(root, width=50, bg="#f1f1f1", borderwidth=0)
	entrytm.insert(0, "Morse in text is: " + tm)
	entrytm.grid(row=5, column=0)

mylabel1 = Label(root, text="Note: Write a clean text, without commas or dots", fg="#ff0000")
mylabel1.grid(row=0, column=0)
e = Entry(root, textvariable=letter, width=50)
e.grid(row=1, column=0)
mybutton1 = Button(root, text="Translate", command=button1)
mybutton1.grid(row=1, column=1)

mylabel2 = Label(root, text='Note: To separate the letters use "/"', fg="#ff0000")
mylabel2.grid(row=3, column=0)
e1 = Entry(root, textvariable=morse, width=50)
e1.grid(row=4, column=0)
mybutton2 = Button(root, text="Translate", command=button2)
mybutton2.grid(row=4, column=1)
    
mybutton3 = Button(root, text='Listen', command= lambda: play(tt))
mybutton3.grid(row=1, column=3)

button_exit = Button(root, text="Exit", command=root.quit)
button_exit.grid(row=10, column=0)


root.mainloop()
