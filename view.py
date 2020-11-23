from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image

root = Tk()
root.title('view image')
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)


the_img1 = ImageTk.PhotoImage(Image.open("images/mountain.jpeg"))
the_img2 = ImageTk.PhotoImage(Image.open("images/mountain2.jpeg"))
the_img3 = ImageTk.PhotoImage(Image.open("images/mountain3.jpeg"))
the_img4 = ImageTk.PhotoImage(Image.open("images/mountain4.jpeg"))
the_img5 = ImageTk.PhotoImage(Image.open("images/mountain5.jpeg"))
the_img6 = ImageTk.PhotoImage(Image.open("images/mountain6.jpeg"))

image_list = [the_img1, the_img2, the_img3, the_img4, the_img5, the_img6]

status = Label(root, text="Image 1 of " + str(len(image_list)), border=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

my_label = Label(image=the_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number+1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))
    
    if image_number == 4:
        button_forward = Button(root, text=">>", state=DISABLED)
        
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), border=1, relief=SUNKEN, anchor=E)
    

    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    if image_number > 0:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<", command=lambda: forward(image_number-1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)
    
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), border=1, relief=SUNKEN, anchor=E)

    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=back, state=DISABLED)
buton_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0)
buton_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
