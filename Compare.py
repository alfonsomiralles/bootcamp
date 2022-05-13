from functools import reduce

def ej2(lista): 
    lista = int(input('Introduce el rago de la lista: '))
    lista = list(range(lista))
    resultado = list(filter((lambda x: x % 2), lista)) 
    print(f'La lista de impares es {resultado}')
    resultado = reduce( (lambda x, y: x + y), resultado) 
    print(f'La suma de todos los impares es {resultado}')

