from os import strerror

# Inicializa 26 contadores para cada letra latina.
# Nota: hemos usado una comprensión para esto.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)} #Crea un diccionario que se llama counters y para cada letra establece un contador que inicia en 0
file_name = input("Ingresa el nombre del archivo a analizar: ") #Pide al usuario que ingrese el nombre archivo que quiere analizar y lo guarda en la variable file_name

#Bloque de codigo que puede lanzar una excepcion 
try:
    file = open(file_name, "rt") #El archivo que se abrio anteriormente es asignado a la variable file e indica que es una rt(solo lectura de texto)
    for line in file:   #Hace que recorra cada linea del texto 
        for char in line: # Hce que recorra cada caracter de la linea 
            # Si es una letra...
            if char.isalpha(): #Verifica si el caracter es una letra utilizando el metodo isalpha
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                counters[char.lower()] += 1  #Si el caracter es una letra, lo convierte a minúscula y se actualiza el contador correspondiente de la letra en el diccionario (counters). Si el caracter ya ha sido encontrado antes, su contador se incrementa en 1.
    file.close() #Cuando acaba de recorrer todas las lineas cierrra el archivo en el bloque try 
    # Demos salida a los contadores.
    for char in counters.keys(): #Recorre las claves del diccionario (counters) 
        c = counters[char] #Asigna el valor del contador de la letra actual a la variable c.
        if c > 0: #Verifica si el valor del contador(c) es mayor que 0 y si es asi lo imprime 
            print(char, '->', c) #Imprime el caracter con su valor del contador 
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno)) #Valida un error 
