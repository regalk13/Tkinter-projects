from tkinter import *
from PIL import Image,ImageTk
import numpy as np 
import matplotlib.pyplot as plt


root = Tk()
root.title("Maths")
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(20000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

mybt = Button(root, text="Graph", command=graph)
mybt.grid(row=0, column=0)

root.mainloop()