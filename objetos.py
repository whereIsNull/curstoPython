class Usuario:
    nombre = "Felipe"
    apellido = "feliz"

usuario = Usuario()
print(usuario)
print(usuario.nombre)
print(usuario.apellido)

usuario2 = Usuario()
print(usuario2.nombre)
print(usuario2.apellido)

class Usuario2:
    def __init__(self, nombre, apellido): #No necesario llamarse self, el primer parámetro es siempre el objeto implícito 
        self.nombre = nombre
        self.apellido = apellido
    nombre = "Felipe"
    apellido = "feliz"
 
# usuario3 = Usuario2() <- ERROR, constructor necesita dos parámetros, self no se manda explícitamente
usuario3 = Usuario2('felipe', 'segundo')
print(usuario3.nombre, usuario3.apellido)

#CON MÉTODOS
class Usuario3:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    nombre = "Felipe"
    apellido = "feliz"

    def saludo(self):
        print('Hola, mi nombre es ', self.nombre, self.apellido)

usuario4 = Usuario3('felipe', 'feliz')
usuario5 = Usuario3('chanchito', 'feliz')
usuario4.saludo()
usuario5.saludo()

usuario4.nombre = 'Chanchito'
usuario4.saludo()
usuario5.saludo()

# del usuario.nombre #Elimina la propiedad, error si se invoca
print(usuario.nombre) 
# del usuario4 #Elimina el objeto por completo 

#HERENCIA
class Admin(Usuario3):
    def superSaludo(self):
        print('Hola, me llamo ', self.nombre, ' y soy administrador')

admin = Admin('Super', 'Feliz')
admin.saludo()
admin.superSaludo()