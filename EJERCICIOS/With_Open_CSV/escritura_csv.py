

import csv 

with open ('c:\\Juan\\ separados.csv', 'w', newline='') as separados:
    archivo=csv.writer(separados)

    archivo.writerow(['Nombre', 'Profesion','Edad'])
    archivo.writerow(['Jose', 'Docente', '25'])
    archivo.writerow(['Samuel','Docente','30'])

    