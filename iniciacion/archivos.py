c = open("chanchito.txt")
print(c.read())

c = open("chanchito.txt", 'r') #<- permiso para leer
# c = open("chanchito.txt", 'a') #<- permiso para añadir
# c = open("chanchito.txt", 'w') #<- permiso para escribir, crea el archivo si no existe
# c = open("chanchito.txt", 'x') #<- permiso para crear archivo si no existe, error si existe

print(c.readline()) # <- lee líneas una a una

for x in c: # <- c es iterable por línea 
    print(x)

c.close() # <- cierra el archivo