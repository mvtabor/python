from tkinter import *

root = Tk()
root.title('Hello, World!')

r = IntVar()
r.set('2')

Radiobutton(root, text='Opción 1', variable=r, value=1).pack()
Radiobutton(root, text='Opción 2', variable=r, value=2).pack()

l = Label(root, textvariable=r)
l.pack()

root.mainloop()

