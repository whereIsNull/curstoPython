lista = [1, 2, 3];
lista2 = lista.copy();
lista.append(4);
print(lista, lista2.count(3));
print(len(lista), len(lista))

largoLista = len(lista)
largoLista2 = len(lista2)

print(largoLista, largoLista2)

# acceder al primer elemento
print(lista[0])

# eliminar elemento de una lista
lista.pop() # <-elimina el último elemento
print(lista)
lista.remove(2) # <- elimina el elemento indicado, no por índice
print(lista)

# ordenar la lista
lista.reverse()
print(lista)

lista.append('chanchito feliz')
print(lista)

lista.sort()  # <- error la lista debe tener el mismo tipo de datos 