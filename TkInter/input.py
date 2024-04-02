from tkinter import *

root = Tk()
root.title('Hello, World:')
root.geometry('500x500')

e = Entry(root, width=40)
e.pack()
e.insert(0, 'Ingrese texto:')

def click():
    texto = e.get()
    l = Label(root, text=texto)
    l.pack()
    e.delete(0, END)
    #l.configure(text=texto)

btn = Button(root, text='click', command=click)
btn.pack()

#l = Label(root, text='Texto de la etiqueta')
#l.pack()

root,mainloop()
