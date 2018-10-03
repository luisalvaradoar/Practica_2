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


class Disco():
    def __init__(self, tam):
        self.__tamanio = tam
        self.__posicion = None

    def setPosicion(self, pos):
        self.__posicion = pos

    def getPosicion(self):
        return(self.__posicion)

def mover_disco(poste1, poste2):
    tam = poste1.getDiscos()[-1].getTamanio()
    if len(poste2.getDiscos()) != 0:
        tam_ult_disct_p2 = ((poste2.getDiscos())[-1]).getTamanio()
        if tam_ult_disct_p2 > tam:
            disco = poste1.sacarDisco()
            poste2.meterDisco(disco)
            return True
        else:
            return False    
    else:
        disco = poste1.sacarDisco()
        poste2.meterDisco(disco)
        return True


def main():
    p1 = Poste(1)
    p2 = Poste(2)
    p3 = Poste(3)

    d1 = Disco(1)
    d2 = Disco(2)
    d3 = Disco(3)
    d4 = Disco(4)
    d5 = Disco(5)
    d6 = Disco(6)
    d7 = Disco(7)
    d8 = Disco(8)

    p1.setDiscos(d1, d2, d3, d4, d5, d6, d7, d8)

    print(p1.getDiscos())
    print(p2.getDiscos())
    print(p3.getDiscos())

    mover_disco(p1, p2)
    mover_disco(p2, p3)
    print('\n')
    print(p1.getDiscos())
    print(p2.getDiscos())
    print(p3.getDiscos())

main()