class Pais:
    def __init__(self,pais,altura,pobcap,perpob):
        self.__pais=pais
        self.__altura=altura
        self.__pobcap=pobcap
        self.__perpob=perpob

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
