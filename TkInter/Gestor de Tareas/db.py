from tkinter import *
import sqlite3 #gestor de base de datos.

root = Tk()
root.title('Hello, world: todo list')
root.geometry('500x500')

conn = sqlite3.connect('todo.db') #creamos la conexion a la bd

c = conn.cursor() #abrimos un cursor.

c.execute("""
    CREATE  TABLE if not todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        description text NOT NULL,
        completed BOOLEAN NOT NULL
    );
""")

conn.commit()

def addTodo():
    todo = e.get()
    c.execute("""
            INSERT INTO todo (description, completed) VALUES(?, ?)
            """, (todo, False))
    conn.commit()
    e.delete(0, END) #podemos ingresar el string 'end' o  usar la constante END

l = Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)

btn = Button(root, text='Agregar', command=addTodo)
btn.grid(row=0, column=2)

frame = LabelFrame(root, text='Mis tareas', padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=5)

e.focus()

root.bind('<Return>',  lambda event: addTodo())
root.mainloop()
