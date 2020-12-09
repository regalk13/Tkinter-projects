from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title("Data")
img = PhotoImage(file='images/icon.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("400x400")

conn = sqlite3.connect('address_book.db')

c = conn.cursor()

c.execute("""CREATE TABLE addresses(
        first_name text, 
        last_name text,
        city text,
        address text,
        state text,
        zipcode integer
        )""")

conn.commit()

conn.close()


root.mainloop()