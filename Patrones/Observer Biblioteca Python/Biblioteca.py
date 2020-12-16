
class Biblioteca():
    def devuelveLibro(self,libro,a):
        if (libro.getEstado() == "MALO"):
            a.notifyObservers()
            
