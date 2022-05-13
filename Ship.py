from pickle import *

class StarShip:

    def __init__(self, nombre, escudo, vida):
        self.nombre= nombre
        self.escudo = escudo
        self.vida = vida

    def __str__(self):
        return self.nombre + " "+ self.escudo + " " + self.vida

nave1 = StarShip("Nave1", "Activo", "10")
print(nave1)

f = open('SpaceShips', 'w+b')
dump(nave1, f)

f.seek(0)
nave2= load(f)
print(nave2)
f.close
