import modulos as xs
from camelcase import CamelCase # Para importar módulo de repositorio instalar pip -> en ubutntu: https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/

print(xs.mascotas)
xs.saludo('Nicolas')

c = CamelCase()
s = 'esta oración necesita camelcase'

camelcased = c.hump(s)
print(camelcased)