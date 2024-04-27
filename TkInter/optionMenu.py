from tkinter import *

root = Tk()
root.title('Hello, world: dropdown')
root.geometry('500x500')

def enviar():
    l = Label(root, text=value.get())
    l.pack()

lista = [ 
    'Lomito Salchicha',
    'Lomito Gordito', 
    'Lomito KFC',
    'Lomito Tiburón'
]

value = StringVar()
value.set(lista[0]) #valor predeterminado 0 en la lista

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()