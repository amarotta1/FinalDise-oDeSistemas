from Subject import Subject

class AlarmaLibro(Subject):
    def __init__(self):
        self.observadores = []

    def attach(self,observador):
        self.observadores.append(observador)

    def dettach(self,observador):
        self.observadores.remove(observador)

    def notifyObservers(self):
        for observador in self.observadores:
            observador.update()

    def getO(self):
        return self.observadores

    