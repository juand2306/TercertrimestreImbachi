

from os import strerror

try:
    file = open('c:\\Juan\\ datos.txt', 'wt')
    nombre=str(input('Ingrese su nombre: '))
    apellido= str(input('Ingrese su apellido: '))
    direccion= str(input('Ingrese su direccion: '))
    telefono= str(input('Ingrese su telefono:  '))

    for i in range(1):
        file.write( nombre+ "\n" )
        file.write(apellido + "\n")
        file.write(direccion + "\n")
        file.write( telefono+ "\n")

    file.close()
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
