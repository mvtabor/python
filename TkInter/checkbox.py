from tkinter import *

root = Tk()
root.title('Hello, world: checkbox')

root.geometry('500x500')

var = StringVar() #contiene el v de nuestro checkbox; si se encuentra press o no.
var.set('Ajedrecista')

def mostrar():
    l = Label(root, text=var.get())
    l.pack()

c = Checkbutton(root, text='I am a checkbox', variable=var, onvalue='sí', offvalue='Ajedrecista')
c.pack()

btn = Button(root, text='Click', command=mostrar)
btn.pack()

root.mainloop()