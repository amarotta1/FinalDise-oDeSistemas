
public class Conexion {
	
	//Declaración, debe ser estatica para que puede ser accedida por un metodo estatico
	private static Conexion instancia;
	//private static Conexion instancia = new Conexion();
	
	//PRIVADO ara evitar instancia mediante operador "new"
	private Conexion() {
		
	}
	
	//Para obtener la instancia unicamente por este metodo
	//Notese la palabra reservada "static" hace posible el acceso mediante Clase.metodo
	public static Conexion getInstancia() {
		if(instancia == null) {
			instancia = new Conexion();
		}
		return instancia;
	}
	
	//Método de prueba
	public void conectar() {
		System.out.println("Me conecté a la BD");
	}
	
	//Método de prueba
	public void desconectar() {
		System.out.println("Me desconecté de la BD");
	}

}

//ESTO DEBE IR EN UN ARCHIVO APARTE LLAMADO Main
public class Main {

	public static void main(String[] args) {
		//Instanciación por constructor prohíbido por ser "private"
		//Conexion c = new Conexion();
		Conexion c = Conexion.getInstancia();
		c.conectar();
		c.desconectar();
		
	}
	
	//Otro ejemplo en: https://www.youtube.com/watch?v=qiFeiYLzIH8
	//Spring Framework gestiona sus beans como Singleton por defecto
}