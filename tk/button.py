from tkinter import *

root = Tk()
root.title("Hola Mundo")

l = Label(root, text=" Hola Mundo")

def click():
    l.pack()

btn = Button(root, text="Clickeame", command=click, fg='#fff000', bg='blue')
btn.pack()

root.mainloop()
