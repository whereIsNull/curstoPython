from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('400x400')

label1 = Label(root, text='Hola mundo! mi primera etiqueta')
label2 = Label(root, text='Ciao mundo! mi segunda etiqueta')
label3 = Label(root, text='               ')

# label1.pack()
# label2.pack()

label1.grid(row=0, column=0)
label3.grid(row=1, column=1)
label2.grid(row=10, column=10)

root.mainloop()