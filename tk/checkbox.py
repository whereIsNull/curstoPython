from tkinter import *

root = Tk()
root.title('Hola mundo: checkbox')
root.geometry('500x500')

var = StringVar()
var.set("chanchito feliz")

c = Checkbutton(root, text='Soy un checkbox', variable=var, onvalue='si', offvalue='chanchito feliz')
c.pack()

def mostrar():
    print('pinchado')
    l=Label(root, text=var.get())
    l.pack()

btn = Button(root, text='Click', command=mostrar)
btn.pack()

root.mainloop()