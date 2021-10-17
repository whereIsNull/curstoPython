#No se pueden modificar una vez creadas
tupla = ('hola', 'mundo', 'somos', 'tupla')

listaDeTupla = list(tupla)

rango = range(6)

diccionario = {
    "nombre": "Chanchito feliz",
    "raza": "Persa",
    "edad": 5
}
print(diccionario)
print(diccionario['nombre'])

print(diccionario.get('nombre'))
diccionario['nombre'] = 'Fluffy'
print(diccionario)

###################
print(len(diccionario))
diccionario['ronronea'] = 'Sí'
print(diccionario)

diccionario.pop('ronronea')
print(diccionario)

diccionario.popitem() # <- Elimina el último valor añadido
print(diccionario)

diccionario['ronronea'] = 'Sí'
copiaGatito = diccionario.copy()
del diccionario['ronronea'] # <- equivalente a diccionario.pop('ronronea')

print(diccionario, copiaGatito)

print(diccionario, copiaGatito)

copiaGatito = dict(diccionario) # <- crea copia
print(diccionario, copiaGatito)

diccionario.clear()
print(diccionario, copiaGatito)

# Diccionarios anidados
gatitos = {
    "Fluffy": {
        'nombre': "Fluffy",
        'edad': 4
    },
    "Mamba": {
        'nombre': "Black mamba",
        'edad': 12
    }
}
print(gatitos)

fluffy = {
    'nombre': "Fluffy",
    'edad': 4
}
mamba = {
    'nombre': "Black mamba",
    'edad': 12
}

gatitos = {
    "fluffy": fluffy,
    "mamba": mamba
} 

# diccionarios usando el constructor dict
perritos = dict(nombre='Chanchito feliz')
print(perritos)

perritos = dict(nombre='Chanchito feliz', edad=6)
print(perritos)