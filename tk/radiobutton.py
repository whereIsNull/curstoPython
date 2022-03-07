from tkinter import *

root = Tk()
root.title('Hola mundo')

r = IntVar()
r.set('2')

# Radiobutton(root, text='Opción 1', variable=r, value=1).pack()
# Radiobutton(root, text='Opción 2', variable=r, value=2).pack()

# Desde lista
CHANCHITOS = [
    ('Feliz', 'Feliz'),
    ('Triste', 'Triste'),
    ('Guay', 'Guay'),
    ('Amadeus', 'Amadeus')
]

chanchito = StringVar()
chanchito.set('Amadeus')

for text, chancho in CHANCHITOS:
    Radiobutton(root, text=text, variable=chanchito, value=chancho).pack()

l = Label(root, textvariable=chanchito)
l.pack()

root.mainloop()