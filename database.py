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

def update():
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        record_id = delete_box.get()

        c.execute("""UPDATE addresses SET
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode

                WHERE oid = :oid""",
                {'first': f_name_editor.get(),
                'last': l_name_editor.get(),
                'address': address_editor.get(),
                'city': city_editor.get(),
                'state': state_editor.get(),
                'zipcode': zip_editor.get(),
                'oid': record_id         
                })

        conn.commit()
        conn.close()

        editor.destroy()

       
def edit():
        global editor
        editor = Toplevel()
        editor.title("Edit data")
        img2 = PhotoImage(file='images/icon.png')
        editor.tk.call('wm', 'iconphoto', editor._w, img2)

        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        record_id = delete_box.get()

        c.execute("SELECT *, oid FROM addresses WHERE oid =" + record_id)
        records = c.fetchall()
        
        global f_name_editor
        global l_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zip_editor

        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1, padx=20)
        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1, padx=20)
        city_editor = Entry(editor, width=30)
        city_editor.grid(row=3, column=1, padx=20)
        state_editor = Entry(editor, width=30)
        state_editor.grid(row=4, column=1, padx=20)
        zip_editor = Entry(editor, width=30)
        zip_editor.grid(row=5, column=1, padx=20)
       
        f_label = Label(editor, text="First Name")
        f_label.grid(row=0, column=0)
        l_label = Label(editor, text="Last Name")
        l_label.grid(row=1, column=0)
        address_label = Label(editor, text="Address")
        address_label.grid(row=2, column=0)
        city_label = Label(editor, text="City")
        city_label.grid(row=3, column=0)
        state_label = Label(editor, text="State")
        state_label.grid(row=4, column=0)
        zip_label = Label(editor, text="Zip Code")
        zip_label.grid(row=5, column=0)

        for record in records:
                f_name_editor.insert(0, record[0])
                l_name_editor.insert(0, record[1])
                address_editor.insert(0, record[2])
                city_editor.insert(0, record[3])
                state_editor.insert(0, record[4])
                zip_editor.insert(0, record[5])

        edit_bnt = Button(editor, text="Update record", command=update)
        edit_bnt.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

def delete():
        conn = sqlite3.connect('address_book.db')
        c = conn.cursor()

        c.execute("DELETE FROM addresses WHERE oid= " + delete_box.get())

        delete_box.delete(0, END)
         
        conn.commit()
        conn.close()


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
                print_records += str(record[0]) + " " + str(record[1]) + "\t" + str(record[6]) + "\n"

        query_label = Label(root, text=print_records)
        query_label.grid(row=12, column=0, columnspan=2)

        conn.commit()
        
        conn.close()

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
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
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

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
delete_label = Label(root, text="Select ID")
delete_label.grid(row=9, column=0, pady=5)



sub_b = Button(root, text="Add record to database", command=submit)
sub_b.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query = Button(root, text="Show records", command=query)
query.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=128)


delete = Button(root, text="Delete record", command=delete)
delete.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=129)

edit = Button(root, text="Edit record", command=edit)
edit.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=136)


exit_ = Button(root, text="Exit", command=root.quit)
exit_.grid(row=13, column=0, columnspan=2)


conn.commit() 
conn.close()

root.mainloop()