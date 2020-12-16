from Destileria import Destileria
from Ingenieria import Ingenieria
from Emergencia import Emergencia
from SensorTemperatura import SensorTemperatura

if __name__ == "__main__":

    d = Destileria()
    i = Ingenieria()
    e = Emergencia()

    sensor = SensorTemperatura()
    
    sensor.agregar(e)
    sensor.agregar(d)
    sensor.agregar(i)    

    print('Temperatura subiendo a 100')
    sensor.set_temperatura(100)
    print('Temperatura subiendo a 500')
    sensor.set_temperatura(500)
    print('Temperatura subiendo a 1000')
    sensor.set_temperatura(1000)
    print('Temperatura subiendo a 1500\n')
    sensor.set_temperatura(1500)
