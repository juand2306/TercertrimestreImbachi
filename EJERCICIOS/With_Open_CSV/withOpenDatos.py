from os import strerror

try:
    with open('c:\\Juan\\ datos.txt', 'wt') as datosp:
        nombre=str(input('Ingrese su nombre: '))
        apellido= str(input('Ingrese su apellido: '))
        direccion= str(input('Ingrese su direccion: '))
        telefono= str(input('Ingrese su telefono:  '))

        for i in range(1):
            datosp.write( nombre+ "\n" )
            datosp.write(apellido + "\n")
            datosp.write(direccion + "\n")
            datosp.write( telefono+ "\n")

except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))