import csv


class Pais:
    def __init__(self,pais,altura,pobcap,perpob):
        self.__pais=pais
        self.__altura=altura
        self.__pobcap=pobcap
        self.__perpob=perpob
        self.__caracteres=0

    def info(self):
        return f"{self.__pais} {self.__altura} {self.__pobcap} {self.__perpob}"
    
    def getPais(self):
        return self.__pais
    
    def getAltura(self):
        return self.__altura
    
    def getPobcap(self):
        return self.__pobcap
    
    def getPerpob(self):
        return self.__perpob
    
    def lector (self , file, indice):
        caracteres = 0

        with open(file , encoding="utf-8" ) as arch:
            leido = csv.reader(arch)

            for row in leido:
                indices = row [indice]
                for  i in indices:
                    caracteres += 1
        
        self.__caracteres = caracteres
        with open('C:\\TercertrimestreImbachi\\ARCHIVOS\\lector.txt' ,"a") as nuevo:
            nuevo.write (f"La columna del indice {indice} tiene {caracteres} caracteres\n")
        print(f"El indice {indice} tiene {caracteres} caracteres")
        
