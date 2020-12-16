from Numero import Numero
from Suma import Suma
from Resta import Resta
from Multiplicacion import Multiplicacion
from Division import Division

num1 = Numero(5)
num2 = Numero(6)
num3 = Numero(8)
num4 = Numero(11)


suma = Suma(num1,num2)
resta = Resta(num4,num3)
mult = Multiplicacion(suma,resta)

print(mult.imprimir(), "=",mult.calcular())