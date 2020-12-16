from AlarmaLibro import AlarmaLibro
from Administracion import Administracion
from Biblioteca import Biblioteca
from Compras import Compras
from Libro import Libro
from Stock import Stock

a = AlarmaLibro()
a.attach(Compras())
a.attach(Administracion())
a.attach(Stock())


libro = Libro()
libro.setEstado("MALO")

biblioteca = Biblioteca()
biblioteca.devuelveLibro(libro,a)

