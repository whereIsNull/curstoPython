from tkinter import *

root = Tk()
root.title('Hola mundo: option menu')
root.geometry('500x500')

def enviar():
    l = Label(root, text=value.get())
    l.pack()

value =StringVar()
# value.set('Chanchito feliz')

lista = ['Chanchito Feliz', 'Chanchito triste', 'Chanchito emocionado']
value.set(lista[1])

# drop = OptionMenu(root, value, 'Chanchito Feliz', 'Chanchito triste', 'Chanchito emocionado')
lista = ['Chanchito Feliz', 'Chanchito triste', 'Chanchito emocionado']
drop = OptionMenu(root, value, *lista) #Pasa la lista con cada elemento como un parámetro

drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()