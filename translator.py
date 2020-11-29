from tkinter import *
import winsound 


alphabet = {
	1: "a",
	2: "b",
	3: "c",
	4: "d",
	5: "e",
	6: "f",
	7: "g",
	8: "h",
	9: "i",
	10: "j",
	11: "k",
	12: "l",
	13: "m",
	14: "n",
	15: "o",
	16: "p",
	17: "q",
	18: "r",
	19: "s",
	20: "t",
	21: "u",
	22: "v",
	23: "w",
	24: "x",
	25: "y",
	26: "z"
}

alphabet_morse = {
	1: ".-",
	2: "-...",
	3: "-.-.",
	4: "-..",
	5: ".",
	6: "..-.",
	7: "--.",
	8: "....",
	9: "..",
	10: ".---",
	11: "-.-",
	12: ".-..",
	13: "--",
	14: "-.",
	15: "---",
	16: ".--.",
	17: "--.-",
	18: ".-.",
	19: "...",
	20: "-",
	21: "..-",
	22: "...-",
	23: ".--",
	24: "-..-",
	25: "-.--",
	26: "--.."
}
#functions
tt = ''

def translate_letter(l):
		letter_translate = ""
		for i in range(1, 27):

			if l == alphabet_morse[i]:
				letter_translate = alphabet[i]
				break
			
			elif l == " ":
				letter_translate = " "
				break
			
			else:
				continue
		return letter_translate
		
 		
def translate_morse(f):
	letter = ""
	translate_final = ""
	for x in f:
	 	if x != "/":
	 	 	letter = letter + x

	 	elif x == "/":
	 		translate_final = translate_final + translate_letter(letter)
	 		letter = ""
	return translate_final


def translate(sentence):
		translate = ""
		for letter in sentence:
			for i in range(1, 27):
				if letter == alphabet[i]:
					translate += alphabet_morse[i] + '/'
					break

				elif letter == ' ':
					translate += ' ' + '/'
					break

				else:
					continue
					
		return translate


def button1():
	global tt
	tt = translate(mainWindow.e.get())	
	entrytt = Entry(root, width=50, bg="#f1f1f1", borderwidth=0)
	entrytt.insert(0, "The text in morse is: " + tt)
	entrytt.grid(row=2, column=0)
    

def button2():
	tm = translate_morse(mainWindow.e1.get())
	entrytm = Entry(root, width=50, bg="#f1f1f1", borderwidth=0)
	entrytm.insert(0, "Morse in text is: " + tm)
	entrytm.grid(row=5, column=0)


def play(mt):
	for x in mt:
		if x == '.':
			winsound.Beep(3799, 500)

		elif x == '-':
			winsound.Beep(3799, 1000)
	
		else:
			continue


root = Tk()
root.title("Translator Morse")
root.geometry("460x450")
img = PhotoImage(file='images/morse.png')
root.tk.call('wm', 'iconphoto', root._w, img)

class Window:

	def __init__(self, root):
		self.root = root

		self.mylabel1 = Label(self.root, text="Note: Write a clean text, without commas or dots", fg="#ff0000")
		self.mylabel1.grid(row=0, column=0)
		self.e = Entry(self.root, width=50)
		self.e.grid(row=1, column=0)
		self.mybutton1 = Button(self.root, text="Translate", command=button1)
		self.mybutton1.grid(row=1, column=1)

		self.mylabel2 = Label(self.root, text='Note: To separate the letters use "/"', fg="#ff0000")
		self.mylabel2.grid(row=3, column=0)
		self.e1 = Entry(self.root, width=50)
		self.e1.grid(row=4, column=0)
		self.mybutton2 = Button(self.root, text="Translate", command=button2)
		self.mybutton2.grid(row=4, column=1)
    
		self.mybutton3 = Button(self.root, text='Listen', command= lambda: play(tt))
		self.mybutton3.grid(row=1, column=3)

button_exit = Button(root, text="Exit", command=root.quit)
button_exit.grid(row=10, column=0)

if __name__ == '__main__':
	mainWindow = Window(root)


root.mainloop()
