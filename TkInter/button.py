from tkinter import *

root = Tk()
root.title("Hello, world!")

l = Label(root, text="Hello, world.")
def click():
    l.pack()

btn = Button(root, text="Click on me", command=click, fg="#ffff00", bg="blue")
btn.pack()

root.mainloop()