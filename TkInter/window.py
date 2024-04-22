from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hello, World!')

#solución 1
# def open():
#     img = ImageTk.PhotoImage(Image.open('1.png'))
#     top = Toplevel()
#     top.title('Hello, World! New window')
#     l = Label(top, text='Text from the second window')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()

#solución 2
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open('1.png'))
#     top = Toplevel()
#     top.title('Hello, World! New window')
#     l = Label(top, text='Text from the second window')
#     l2 = Label(top, image=img)
#     l.pack()
#     l2.pack()
#     top.mainloop()

#solución 3
def open(img):
    top = Toplevel()
    top.title('Hello, World! New window')
    l = Label(top, text='Text from the second window')
    l2 = Label(top, image=img)
    l.pack()
    l2.pack()
    top.mainloop()

img = ImageTk.PhotoImage(Image.open('1.png'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()
# btn = Button(root, text='Click', command=open).pack() #solu 1/2


root.mainloop() 

#CTRL + K + C para comentar varias líneas seleccionadas a la vez.
#CTRL + K + U para descomentar varias lineas 