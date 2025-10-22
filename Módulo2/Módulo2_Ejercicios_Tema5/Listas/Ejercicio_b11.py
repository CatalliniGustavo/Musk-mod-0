'''
11. Haz un programa que itere ambas listas de tamaños n y m
(siendo n y m números distintos) simultáneamente e imprima sus elementos.
'''
if __name__ == '__main__':
    n = int(input('Ingresa el tamaño de la lista 1: '))
    m = int(input('Ingresa el tamaño de la lista 2: '))
    lista1 = []
    for i in range(0,n):
        lista1.append(input('Ingresa un elemento a la lista 1: '))

    lista2 = []
    for i in range(0,m):
        lista2.append(input('Ingresa un elemento a la lista 2: '))

    maxi = max(n,m)
    for i in range(0,maxi):
        if i < len(lista1):
            print(lista1[i])
        if i < len(lista2):
            print(lista2[i])

