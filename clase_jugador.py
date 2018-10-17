class Jugador():
    def __init__(self):
        self.__jugadas = []

    def mover_disco(self, poste1, poste2):
        if poste1 == poste2:
            return False
        if len(poste1.getDiscos()) == 0:
            return False

        tam = poste1.getDiscos()[-1].getTamanio()
        if len(poste2.getDiscos()) != 0:
            tam_ult_disct_p2 = ((poste2.getDiscos())[-1]).getTamanio()
            if tam_ult_disct_p2 > tam:
                disco = poste1.sacarDisco()
                poste2.meterDisco(disco)
                self.__jugadas.append((poste1.getPosicion(), poste2.getPosicion(), disco.getTamanio()))
                return True
            else:
                return False    
        else:
            disco = poste1.sacarDisco()
            poste2.meterDisco(disco)
            self.__jugadas.append((poste1.getPosicion(), poste2.getPosicion(), disco.getTamanio()))
            return True

    def getJugadas(self):
        return(self.__jugadas)