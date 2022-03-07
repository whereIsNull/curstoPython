from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo')

# def click():
#     messagebox.showwarning('Popup', 'Hola mundo')

# def click():
#     messagebox.showinfo('Popup', 'Hola mundo')

# def click():
#     messagebox.showerror('Popup', 'Hola mundo')

# def click():
#     respuesta = messagebox.askquestion('Popup', 'Hola mundo')
#     print(respuesta)
#     if respuesta == 'yes':
#         messagebox.showinfo('Respuesta', 'La respuesta fue ' + respuesta)
#     else:
#         messagebox.showinfo('Respuesta', ':(  ' + respuesta)

# def click():
#     respuesta = messagebox.askokcancel('Hola mundo', 'Desea realizar acción?') #Devuelve booleano
#     if respuesta:
#         messagebox.showinfo('Hola mundo', 'La respuesta fue OK')
#     else:
#         messagebox.showinfo('Hola mundo', 'La respuesta fue cancel')

def click():
    respuesta = messagebox.askyesno('Hola mundo', 'Desea realizar acción?') #Devuelve booleano
    if respuesta:
        messagebox.showinfo('Hola mundo', 'La respuesta fue Yes')
    else:
        messagebox.showinfo('Hola mundo', 'La respuesta fue No')


btn = Button(root, text='Presióname', command=click)
btn.pack()

root.mainloop()