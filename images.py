from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image

root = Tk()
root.title('Regalk is the best')
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)    

the_img = ImageTk.PhotoImage(Image.open("images/icon.png"))
my_label = Label(image=the_img)
my_label.pack()

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()
