package ejerciciosIntroduccion;

public class tema9 {
    public static void main(String[] args){
        Cliente cliente = new Cliente();
        cliente.setNombre("Cliente");
        System.out.println("Hola! me llamo " + cliente.getNombre());
        cliente.setEdad(35);
        System.out.println("Tengo: " + cliente.getEdad() + " tacos");
        cliente.setTelefono(661775782);
        System.out.println("My phone number is: " + cliente.getTelefono());
        cliente.setCredito(2350);
        System.out.println("Mi credito es: " + cliente.getCredito());

        System.out.println("----------------------");
        System.out.println("----------------------");

        Trabajador trabajador = new Trabajador();
        trabajador.setNombre("Trabajador");
        System.out.println("Hola! me llamo " + trabajador.getNombre());
        trabajador.setEdad(25);
        System.out.println("Tengo: " + trabajador.getEdad() + " tacos");
        trabajador.setTelefono(626626626);
        System.out.println("My phone number is: " + trabajador.getTelefono());
        trabajador.setSalario(1500);
        System.out.println("Mi salario es: " + trabajador.getSalario());

    }
    
}

class Persona {
    private String nombre;
    private int edad;
    private int telefono;

    public void setNombre (String nombre){
        this.nombre = nombre;
    }
    public String getNombre (){
        return nombre;
    }

    public void setEdad (int edad){
        this.edad = edad;
    }
    public int getEdad (){
        return edad;
    }

    public void setTelefono (int telefono){
        this.telefono = telefono;
    }
    public int getTelefono (){
        return telefono;
    }
}

class Cliente extends Persona{
    private int credito;

    public void setCredito (int credito){
        this.credito = credito;
    }
    public int getCredito (){
        return credito;
    }    
}


class Trabajador extends Persona{
    private int salario;

    public void setSalario (int salario){
        this.salario = salario;
    }
    public int getSalario (){
        return salario;
    }    
}



