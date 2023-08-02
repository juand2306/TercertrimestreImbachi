import os 

try:
    strem=open('c:\\Juan\\prueba1.txt', 'r', encoding='utf-8')

    for x in strem:
        file=strem.redline()

        print (strem.redline())


except IOError:
    print("Paila mi so")

