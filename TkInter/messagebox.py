from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hello, World!')

#def click():
#    messagebox.showwarning('Popup', 'You cliked the button!')

#def click():
#    messagebox.showinfo('Popup', 'You cliked the button!')

#def click():
#    messagebox.showerror('Popup', 'You cliked the button! :(')

#def click():
#    respuesta = messagebox.askquestion('Popup', 'Are you cliked the button?')
#    if respuesta == 'yes':
#        messagebox.showinfo('Respuesta', 'La respuesta fue ' + respuesta)
#    else:
#        messagebox.showinfo('Respuesta', 'La respuesta fue ' + respuesta)

#def click():
#    respuesta = messagebox.askokcancel('Hello, World!', '¿Desea realizar acción?')
#    if respuesta:
#        messagebox.showinfo('Hello, World!', 'La respuesta fue Ok')
#    else:
#        messagebox.showinfo('Hello, World!', 'La respuesta fue cancelar')

def click():
    respuesta = messagebox.askyesno('Hello, World!', '¿Desea realizar acción?')
    if respuesta:
        messagebox.showinfo('Hello, World!', 'La respuesta fue Yes')
    else:
        messagebox.showinfo('Hello, World!', 'La respuesta fue No')

btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()