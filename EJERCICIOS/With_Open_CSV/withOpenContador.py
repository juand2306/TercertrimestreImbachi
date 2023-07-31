
from os import strerror

try:
    character_counter = line_counter = 0
    with open('c:\\Juan\\ datos.txt', 'rt') as datosc:
        line = datosc.readline()
        while line != '':
            line_counter += 1
            for char in line:
                print(char, end='')
                character_counter += 1
            line = datosc.readline()

        print("\n\nCaracteres en el archivo:", character_counter)
        print("Líneas en el archivo:     ", line_counter)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))