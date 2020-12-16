from Banco import Banco
from Empleado import Empleado
from SectorAdministrativo  import SectorAdministrativo
from SectorCajas import SectorCajas
from SectorContaduria import SectorContaduria
from SectorGerencia import SectorGerencia

banco = Banco()
administracion  =SectorAdministrativo()
cajas = SectorCajas()
contaduria = SectorContaduria()
gerencia = SectorGerencia()

banco.agregar(administracion)
administracion.agregar(cajas) #porque hereda de banco
banco.agregar(contaduria)
banco.agregar(gerencia)

cajero1 = Empleado("Juan Perez", "Cajero",2000)
cajero2 = Empleado("Alejandro Gomez", "Cajero",2000)
cajero3 = Empleado("Roberto Martinez", "Cajero",1500)

cajas.agregar(cajero1)
cajas.agregar(cajero2)
cajas.agregar(cajero3)

gerente = Empleado("Martin Sanchez","Gerente",5000)
gerencia.agregar(gerente)
       
contador = Empleado("Ignacio Hernandez","Contador",3000)
contaduria.agregar(contador)
       
print(banco.getSueldo())