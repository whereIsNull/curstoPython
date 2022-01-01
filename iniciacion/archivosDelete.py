import os

if(os.path.exists("chanchito.txt")):
    os.remove("chanchito.txt") # <- error si el archivo no existe 
else:
    print('El archivo no existe')


if(os.path.exists("micarpeta")):
    os.rmdir("micarpeta") # <- error si el archivo no existe 
else:
    print('El directorio no existe')