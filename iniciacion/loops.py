i=0

while i < 5:
    print(i)
    if i==3:
        break #Si aquí ponemos continue -> bucle infinito
    i += 1


usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']

for usuario in usuarios:
    print(usuario)

usuario = 'Chanchito feliz'
for c in usuario:
    print(c)

for usuario in usuarios:
    if usuario == 'roberto':
        break
    print(usuario)

for usuario in usuarios:
    if usuario == 'roberto':
        continue
    print(usuario)

for x in range(3, 30):
    print(x)

for x in range(3, 30, 3):
    print(x)
else:
    print('Hemos terminado')

usuarios = ['Chanchito feliz', 'felipe', 'roberto', 'nicolas']
edades = [24, 25, 26, 35]

for usuario in usuarios:
    for edad in edades:
        print(usuario, edad)