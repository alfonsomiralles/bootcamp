def verificar ():
    numeroIf = int(input("Introduzca un número: "))
    if numeroIf >= 0:
        print ("positivo")
    else:
        print ("negativo")
print("\nVerificando positivo o negativo")        
verificar()

print("\nComprobando While")
numeroWhile = 0
while numeroWhile < 3:
    numeroWhile +=1
    print (numeroWhile)

print("\nComprobando DoWhile")    
numeroDoWhile = 0
while numeroDoWhile < 3:
    numeroDoWhile +=1
    print (numeroDoWhile)   
    break

print("\nComprobando Bucle For")
numeroFor = 0
for x in range(10):
    if numeroFor <=3:
        numeroFor+=1
        print (numeroFor)


def estaciones():
    estacion = str(input("Escriba la estación del año: ")).lower()
    if estacion == 'primavera':
        return f'Estamos en {estacion}'
    elif estacion == 'verano':
        return f'Estamos en {estacion}'
    elif estacion == 'otoño':
        return f'Estamos en {estacion}'
    elif estacion == 'invierno':
        return f'Estamos en {estacion}'
    else:
        return f'E{estacion} no es una estación del año'
print("\nComprobando estaciones")        
print(estaciones())