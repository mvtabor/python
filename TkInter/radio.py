from tkinter import *

root = Tk()
root.title('Hello, World!')

r = IntVar()
r.set('2')

#Radiobutton(root, text='Opción 1', variable=r, value=1).pack()
#Radiobutton(root, text='Opción 2', variable=r, value=2).pack()

RUNNERS = [
    ('Veloz', 'Veloz'),
    ('Lento', 'Lento'),
    ('Animado', 'Animado'),    
    ('Cansado', 'Cansado')    
]

runner = StringVar()
runner.set('Cansado')

for text, run in RUNNERS:
    Radiobutton(root, text=text, variable=runner, value=run).pack()

#l = Label(root, textvariable=r)
l = Label(root, textvariable=runner)
l.pack()

root.mainloop()

