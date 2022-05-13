from functools import reduce
lista = int(input('Introduce el rago de la lista: '))
lista = list(range(lista))
def ej2(lista): 
    
    resultado = list(filter((lambda x: x % 2), lista)) 
    print(f'La lista de impares es {resultado}')
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(f'La suma de todos los impares es {resultado}')


ej2(lista)