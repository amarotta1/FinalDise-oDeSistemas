from Observer import Observer

class Emergencia(Observer):
    
    def update(self):
        print('Emergencia: Prendiendo alarmas')