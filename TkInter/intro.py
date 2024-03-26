from tkinter import *

root =Tk()
root.title('Hola Mundo')
root.geometry('400x500')

#label = Label(root, text='¡Hola mundo! Mi primera etiqueta.')
#Label(root, text='¡Hola mundo! Mi primera etiqueta.').pack()
#label.pack() #no es necesario crear una nueva instancia de label y asignarla a una variable para luego agregarla con pack
#  Esta forma es un poco límitada porque no le podemos entregar un orden. Por eso, podemos utilizar .grid.

l1= Label(root, text='¡Hola, mundo! Mi primera etiqueta.')
l2= Label(root, text='¡Adiós, mundo! Segunda etiqueta.')

l1.grid(row=0, column=0)
l2.grid(row=1, column=1)

root.mainloop()
