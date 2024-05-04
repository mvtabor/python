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

def render_costumers():
    rows = c.execute("SELECT * FROM costumer").fetchall()

    tree.delete(*tree.get_children())
    
    for row in rows:
        tree.insert('', 'end', row[0], values=(row[1], row[2], row[3]))

def insertar(costumer):
    c.execute("""
            INSERT INTO costumer (name, phone, company) VALUES(?, ?, ?)
            """, (costumer['name'], costumer['phone'], costumer['company']))
    conn.commit()
    render_costumers()

def new_costumer():
    def save():
        if not name.get():
            messagebox.showerror('Error', 'Name is required')
            return
        if not phone.get():
            messagebox.showerror('Error', 'Phone is required')
            return
        if not company.get():
            messagebox.showerror('Error', 'Company is required')
            return

        # if not  name.get() or not phone.get() or not company.get():
        #     messagebox.showwarning('Error','Fill out  all fields')
        #     return
        
        costumer = {
            'name': name.get(),
            'phone': phone.get(),
            'company': company.get()
        }
        insertar(costumer)
        top.destroy()


    top = Toplevel()
    top.title('New Costumer')

    lname = Label(top, text='Name')
    name =  Entry(top, width=40)
    lname.grid(row=0, column=0)
    name.grid(row=0, column=1)

    lphone = Label(top, text='Phone')
    phone =  Entry(top, width=40)
    lphone.grid(row=1, column=0)
    phone.grid(row=1, column=1)

    lcompany = Label(top, text='Company')
    company =  Entry(top, width=40)
    lcompany.grid(row=2, column=0)
    company.grid(row=2, column=1)

    save  = Button(top, text="Save", command=save)
    save.grid(row=3, column=1)

    top.mainloop()

def delete_costumer():
        id = tree.selection()[0]
        costumer = c.execute("SELECT * FROM costumer WHERE id = ?",  (id, )).fetchone()
        respuesta = messagebox.askokcancel('Sure?','Are you sure to delete the costumer ' + costumer[1] + '?')
        if respuesta:
                c.execute("DELETE FROM costumer WHERE id = ?", (id, ))
                conn.commit()
                render_costumers()
        else:
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

render_costumers()

root.mainloop()
