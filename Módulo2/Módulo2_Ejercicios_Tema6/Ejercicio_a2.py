'''
2. Haz un programa que cree una función con longitud variable de argumentos.
Input: func1(20, 40, 60)
Output:
20
40
60
'''


def imprimirLista(*lista):
    for elemento in lista:
        print(elemento)


if __name__ == '__main__':
    imprimirLista(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
