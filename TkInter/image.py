from tkinter import * 
from PIL import ImageTk, Image

#instalamos Pillow para trabajar con imágenes.

root = Tk()
root.title('Hello, World!')

# imagen = Image.open('filmimage.png')
# imagen.show()

img = ImageTk.PhotoImage(Image.open('filmimage.png'))
l =  Label(image=img)
l.pack()

root.mainloop()