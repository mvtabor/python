from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3 

root = Tk()
root.title('Hello, world: CRM')

conn = sqlite3.connect('crm.db')

c = conn.cursor()

c.execute("""
        CREATE TABLE if  not exists  customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            company TEXT NOT NULL 
            );
""")

def new_costumer():
    pass

def delete_costumer():
    pass

btn = Button(root, text='New costumer', command=new_costumer)
btn.grid(column=0, row=0)

btn_delete = Button(root, text='Delete costumer', command=delete_costumer)
btn_delete.grid(column=1, row=0)

tree = ttk.Treeview(root)
tree['columns'] = ('Name', 'Phone', 'Company')
tree.column('#0', width=0, stretch='no')
tree.column('Name')
tree.column('Phone')
tree.column('Company')

tree.heading('Name', text='Name')
tree.heading('Phone', text='Phone')
tree.heading('Company', text='Company')
tree.grid(column=0, row=1, columnspan=2)

root.mainloop()