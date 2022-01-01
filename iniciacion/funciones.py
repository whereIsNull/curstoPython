def miFuncion():
    print('Mi primera función')

miFuncion()

def imprimeDato(argumento1):
    print('Mi argumento es ', argumento1)

imprimeDato('parametro 1')

def imprimeDato(nombre, apellido):
    print('El nombre completo es ', nombre, apellido)

imprimeDato('Chanchito', 'feliz')

# imprimeDato('Chanchito') #<- error, número de parámetros tiene que corresponderse con la definición

def imprimeDato(*nombre): # <- los argumentos se reciben como una lista 
    print('El nombre completo es: ', nombre)

imprimeDato('Chanchito', 'Feliz', 'lala', 'lele')

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

nombreCompleto(nombre='Chanchito', apellido='feliz')

def nombreCompleto2(**keywordArgs):
    print(keywordArgs['nombre'], keywordArgs['apellido'])

nombreCompleto2(nombre='Chanchito', apellido='feliz')

def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

miFuncion2()
miFuncion2('Batman')

def miFuncionLista(lista):
    for elemento in lista:
        print(elemento)

miFuncionLista(['chanchito', 'feliz'])

def concatenaNombres(lista):
    i = ''
    for elemento in lista:
        i = i + ' ' + elemento
    return i

nombres = concatenaNombres(['chanchito', 'feliz'])
print(nombres)

#Recursividad
def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i-1)

recursion(6)