
paises= []
cont = 5
print(f'Se le van a solicitar {cont} países que no se pueden repetir')
for i in range (cont):
    print(f'Quedan {cont} países')
    pais = input("Introduzca nombre de un país: ")
    cont-=1
    paises.append(pais)
    if cont==0:
        countries = list(set(paises))
        countries.sort()
        print(countries)
