# class Gato():
#     def __init__(self, nombre, onomatopeya):
#         self.nombre = nombre
#         self.onomatopeya = onomatopeya
    
#     def saludo(self):
#         print("Hola, soy un gato, y mi sonido es el ", self.onomatopeya)

# class Perro():
#     def __init__(self, nombre, onomatopeya):
#         self.nombre = nombre
#         self.onomatopeya = onomatopeya
    
#     def saludo(self):
#         print("Hola, soy un perro, y mi sonido es el ", self.onomatopeya)

# gato = Gato('Fluffy', 'maullido')
# gato.saludo()
# perro = Perro('Firulais', 'ladrido')
# perro.saludo()

#Refactorizar código anterior
class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("Hola, soy un ", self.tipo ," y mi sonido es el ", self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'
    
gato = Gato('Fluffy', 'maullido')
gato.saludo()
perro = Perro('Firulais', 'ladrido')
perro.saludo()

class Canario(Animal):
    tipo = 'canario'

canario = Canario('Piolin', 'silbido')
canario.saludo()

#EXTENDER MÉTODO INIT
class GatoExtendido(Animal):
    tipo = 'gato'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('hola soy un gato extendido')

gatoExtendido = GatoExtendido('Fluffy', 'maullido')
gatoExtendido.saludo()

#otra forma de extenderlo
class PerroExtendido(Animal):
    tipo = 'perro'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya) # <- con super() no necesario pasar self
        print('Instanciando un perro')

perroExtendido = PerroExtendido('Fluffy', 'guau')
perroExtendido.saludo()