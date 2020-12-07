from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()
root.title('File')
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="tkinter-projects/images", title="Select a file", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    label_image = Label(root, image=my_image).pack()


button = Button(root, text="Open file", command=open).pack()
root.mainloop()