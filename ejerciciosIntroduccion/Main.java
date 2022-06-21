package ejerciciosIntroduccion;


public class Main {
    public static void main(String[] args){
        Persona persona = new Persona();
        persona.setNombre("Fonss");
        System.out.println("Hola! me llamo " + persona.getNombre());
        persona.setEdad(35);
        System.out.println("Tengo: " + persona.getEdad() + " tacos");
        persona.setTelefono(661775782);
        System.out.println("My phone number is: " + persona.getTelefono());

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