class Poste():
    def __init__(self, posicion):
        self.__posicion = posicion
        self.__discos = []
    
    def getPosicion(self):
        return(self.__posicion)

    def setDiscos(self, *discos):
        for i in discos:
            self.__discos.append(i)
            i.setPosicion(self.getPosicion())

    def getDiscos(self):
        return(self.__discos)

    def sacarDisco(self):
        l = len(self.__discos) - 1
        disc = self.__discos[l]
        (self.__discos).remove(disc)
        return(disc)
    
    def meterDisco(self, disco):
        (self.__discos).append(disco)
        disco.setPosicion(self.getPosicion())