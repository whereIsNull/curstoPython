from tkinter import *
#Instalar pillow - pip install Pillow
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo')

# Sistema de SO
# imagen = Image.open('image.jpg')
# imagen.show()

img = ImageTk.PhotoImage(Image.open('image.jpg'))
l = Label(image=img)
l.pack()

root.mainloop()