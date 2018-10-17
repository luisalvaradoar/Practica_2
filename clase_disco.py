class Disco():
    def __init__(self, tam):
        self.__tamanio = tam
        self.__posicion = None

    def getTamanio(self):
    	return(self.__tamanio)

    def setPosicion(self, pos):
        self.__posicion = pos

    def getPosicion(self):
        return(self.__posicion)