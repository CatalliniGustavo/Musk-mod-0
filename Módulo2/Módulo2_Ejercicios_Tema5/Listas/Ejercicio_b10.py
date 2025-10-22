'''
10. Haz un programa que concatene dos listas del
mismo tamaño n alternando elementos de una lista y otra.
'''
if __name__ == '__main__':
    n = int(input('Ingresa el largo de las listas: '))
    lista1 = []
    for i in range(0,n):
        lista1.append(input('Ingresa un elemento a la lista 1: '))

    lista2 = []
    for i in range(0,n):
        lista2.append(input('Ingresa un elemento a la lista 2: '))

    listaf = []
    for i in range(0,n):
        listaf.append(lista1[i])
        listaf.append(lista2[i])
    print(listaf)
