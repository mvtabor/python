from tkinter import *

root = Tk()
root.title('Hello, World')

#frame = LabelFrame(root, text='Login', padx=10, pady=10, borderwidth=10)
frame = Frame(root, padx=10, pady=10, borderwidth=10) #si queremos un frame sin texto podemos simplemente utilizar esta etiqueta
frame.pack(padx=50, pady=50)

l = Label(frame, text='Into a frame')
btn = Button(frame, text='Salir', command=root.quit)
l.pack()
btn.pack()

root.mainloop()