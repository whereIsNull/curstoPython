primero = input("sumando1: ")
segundo = input("sumando2: ")
print(primero + segundo)

primeroInt = int(primero)
segundoInt = int(segundo)
print(primeroInt + segundoInt)

# si pasamos string:
primero = input("sumando1: ")
try:
     primero = int(primero)
except:
    primero = "chanchito feliz"

segundo = input("sumando2: ")
try:
     segundo = int(segundo)
except:
    segundo = "chanchito feliz"

if primero == 'chanchito feliz' or segundo == "chanchito feliz":
    print("Ingresaste mal un dato, sólo números please")
else:
    print(primero + segundo)