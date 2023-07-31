
import csv 

character_counter = line_counter = 0
with open ('c:\\Juan\\ separados.csv', 'r', newline='') as separados:
    contenido= separados.readline()

    while contenido != '':
        line_counter += 1
        for char in contenido:
            print(char, end='')
            character_counter += 1
        contenido = separados.readline()

    print("\n\nCaracteres en el archivo:", character_counter)
    print("Líneas en el archivo:     ", line_counter)
