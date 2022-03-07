from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('500x500')

e = Entry(root, width=60)
e.pack()
e.insert(0, "Ingresa texto")

def click():
    texto = e.get()
    textvariable.set(texto)
    # l.configure(text=texto)
    # e.delete(0, END)

btn = Button(root, text='click', command=click)
btn.pack()

textvariable = StringVar()

l = Label(root, textvariable=textvariable)
l.pack()

root.mainloop()