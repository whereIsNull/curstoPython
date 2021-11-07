c = open("chanchito.txt", 'a') 

c.write('\agraremos nueva línea')
c.close()

x = open("chanchito.txt")
print(x.read())
x.close()

print('Escribir en el archivo')
c = open("chanchito.txt", 'w') 
c.write('\agraremos nueva línea')
c.close()

x = open("chanchito.txt")
print(x.read())