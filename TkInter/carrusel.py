from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('Carrusel')

img1 = ImageTk.PhotoImage(Image.open('images/1.png'))
img2 = ImageTk.PhotoImage(Image.open('images/2.png'))
img3 = ImageTk.PhotoImage(Image.open('images/3.png'))
img4 = ImageTk.PhotoImage(Image.open('images/4.png'))
img5 = ImageTk.PhotoImage(Image.open('images/5.png'))
img6 = ImageTk.PhotoImage(Image.open('images/6.JPG'))

lista = [img1, img2, img3, img4, img5, img6]

l = Label(root, image=img1)
l.grid(row=0, column=0, columnspan=5)

def adelante(img_num):
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    btn_atras = Button(root, text='<-', command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))

    if img_num == 5:
        btn_adelante = Button(root, text='N/A', state=DISABLED)

    l.grid(row=0, column=0, columnspan=5)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

def atras(img_num):
    global l
    global btn_atras
    global btn_adelante

    l.grid_forget()
    l = Label(root, image=lista[img_num])
    btn_atras = Button(root, text='<-', command=lambda: atras(img_num - 1))
    btn_adelante = Button(root, text='->', command=lambda: adelante(img_num + 1))

    if img_num == 0:
        btn_atras = Button(root, text='N/A', state=DISABLED)

    l.grid(row=0, column=0, columnspan=5)
    btn_atras.grid(row=1, column=0)
    btn_adelante.grid(row=1, column=2)

btn_atras = Button(root, text='N/A', state=DISABLED)
btn_adelante = Button(root, text='->', command=lambda: adelante(1))

btn_atras.grid(row=1, column=0)
btn_adelante.grid(row=1, column=2)

root.mainloop()