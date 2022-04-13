
# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada 
# Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para 
# inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    _nombre = None
    _nota = None
    def __init__(self):
        self._nombre = input("Introduzca su nombre: ") 
        self._nota = int(input("Introduzca su calificación: "))
        print ("El alumno",self._nombre, "ha obtenido un",self._nota, "en su calificación")
        if self._nota >= 5:
            print("El alumno ha aprobado")
        else:
            print ("El alumno ha suspendido")    

al = Alumno()
#print(dir(al))
al.__init__
