'''
6. Haz un programa que devuelva la concatenación de v1 y v2, v1 y v2
son dos listas de tamaño n y m. Es decir, hay que devolver un vector
que tenga los elementos de v1 seguidos de los elementos de v2.
Input:
3
2
a b c
d e
Output: ['a', 'b', 'c', 'd', 'e']
'''
if __name__ == '__main__':
    n = int(input('Ingrese la cantidad de elementos de la lista 1: '))
    m = int(input('Ingrese la cantidad de elementos de la lista 2: '))
    lista1 = []
    for i in range(0,n):
        lista1.append(input('valor lista 1: '))

    for i in range(0,m):
        lista1.append(input('valor lista 2: '))

    print(lista1)
