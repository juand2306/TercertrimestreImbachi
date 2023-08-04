from Pais import *
import csv 

listapaises=[]

with open('C:\\TercertrimestreImbachi\\ARCHIVOS\\pais.csv', encoding='utf-8') as archivo:

    lectura=csv.reader(archivo)
    for row in lectura:
        ob=Pais(row[1], row[7], row[8], row[9])
        listapaises.append(ob)
        #print(row )
        
ob.lector('C:\\TercertrimestreImbachi\\ARCHIVOS\\pais.csv', 7) 
      
"""for apr in listapaises:
    #print(apr)
    print('Pais:',apr.getPais())
    print('Altura:',apr.getAltura())
    print('Poblacion de la capital:',apr.getPobcap())
    print('Per pob:',apr.getPerpob(),"\n")"""
    


