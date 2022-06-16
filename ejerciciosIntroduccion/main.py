def sumar(x,y):
    return x+y

print(sumar(3,2))   


class Coche:

    def __init__(self):
        puertas = input("Introduzca Número de puertas: ")
        self.puertas = puertas
        

    def __str__(self):
        pass
            
    def valor(self):
        return f'El coche tiene {self.puertas} puertas'    



miCoche = Coche()

print(str(miCoche.valor()))




        