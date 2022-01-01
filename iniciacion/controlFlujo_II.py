if 2 == 5:
    print('lalala')
elif 2 < 5:
    print("2 < 5 en elif")

if 2 != 5:
    print('lalala')
elif 2 < 5:
    print("2 < 5 en elif") # no se ejecuta porque ya es verdadera la primera

if 2 == 5:
    print('lalala')
elif 2 > 5:
    print("2 > 5 en elif")
else:
    print("me imprimo cuando todo anterior evalúa en falso")

if 2 == 5:
    print('lalala')
elif 2 > 5:
    print("2 > 5 en elif")
elif 2 < 5:
    print("2 < 5 en segundo elif")
else:
    print("me imprimo cuando todo anterior evalúa en falso")

# en una sola linea
if 2 < 5: print('if de una línea')

print("if devuelve true") if 5 > 2 else print("cuando devuelve false") # <- operador ternario

if 2 < 5 and 3 > 2: 
    print("ambas devuelven true")

if 2 < 5 and 3 < 1:
    print("hay una falsa, esto no se muestra")

if 2 < 5 or 3 < 1:
    print("hay una verdadera, esto se muestra")