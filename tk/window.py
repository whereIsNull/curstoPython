from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola mundo')


# # Solucion1
# def open():
#     img = ImageTk.PhotoImage(Image.open('cascada.png'))
#     top = TopLevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='Soy texto en una segunda ventana')
#     l2 = Label(top, image = img)
#     l.pack()
#     l2.pack()

# # Solucion2
# def open():
#     global img
#     img = ImageTk.PhotoImage(Image.open('cascada.png'))
#     top = TopLevel()
#     top.title('Hola mundo, nueva ventana')
#     l = Label(top, text='Soy texto en una segunda ventana')
#     l2 = Label(top, image = img)
#     l.pack()
#     l2.pack()

def open(img):
    top = TopLevel(root)
    top.title('Hola mundo, nueva ventana')
    l = Label(top, text='Soy texto en una segunda ventana')
    l2 = Label(top, image = img)
    l.pack()
    l2.pack()

img = ImageTk.PhotoImage(Image.open('cascada.png'))
btn = Button(root, text='Click', command=lambda: open(img)).pack()

root.mainloop()