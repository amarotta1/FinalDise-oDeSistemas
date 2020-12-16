from Subject import Subject

class SensorTemperatura(Subject):

    def __init__(self):
        self.observadores = []
        self.temperatura = 0

    def agregar(self, observer):
        self.observadores.append(observer)

    def eliminar(self,observer):
        self.observadores.remove(observer)

    def set_temperatura(self,t):
        self.temperatura = t

        if t>1200:
            print('Temperatura mayor a 1200 ...Alertando...')
            self.notificar()

    def notificar(self):
        for observer in self.observadores:
            observer.update()