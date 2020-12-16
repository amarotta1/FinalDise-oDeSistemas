from src.Lavado import *
from src.Enjuagado import *
from src.Centrifugado import *

class Lavarropa:
    def __init__(self):
        self.lavado = Lavado()
        self.enjuagado = Enjuagado()
        self.centrifugado = Centrifugado()

    def comenzarLavado(self):
        self.lavado.lavar()
        self.enjuagado.enjuagar()
        self.centrifugado.centrifugar()