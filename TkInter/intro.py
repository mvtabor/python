from tkinter import *

root =Tk()
root.title('Hola Mundo')
root.geometry('400x500')

label = Label(root, text='¡Hola mundo! Mi primera etiqueta.')
#Label(root, text='¡Hola mundo! Mi primera etiqueta.').pack()

label.pack() #no es necesario crear una nueva instancia de label y asignarla a una variable para luego agregarla con pack

root.mainloop()
