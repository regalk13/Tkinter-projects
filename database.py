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
        
c.execute("""CREATE TABLE IF NOT EXISTS addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")


def submit():
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()
        
        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zip_)", 
                {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zip_': zip_.get()     
                })
        
        conn.commit()
        
        conn.close()

        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zip_.delete(0, END)


def query():
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()

        print_records = ''
        for record in records:
                print_records += str(record[0]) + " " + str(record[1]) + "\n" #" " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + str(record[5]) + " " + str(record[6])

        query_label = Label(root, text=print_records)
        query_label.grid(row=8, column=0, columnspan=2)

        conn.commit()
        
        conn.close()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
zip_ = Entry(root, width=30)
zip_.grid(row=5, column=1, padx=20)

f_label = Label(root, text="First Name")
f_label.grid(row=0, column=0)
l_label = Label(root, text="Last Name")
l_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zip_label = Label(root, text="Zip Code")
zip_label.grid(row=5, column=0)


sub_b = Button(root, text="Add record to database", command=submit)
sub_b.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query = Button(root, text="Show records", command=query)
query.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

exit_ = Button(root, text="Exit", command=root.quit)
exit_.grid(row=8, column=0, columnspan=2)


conn.commit() 
conn.close()

root.mainloop()