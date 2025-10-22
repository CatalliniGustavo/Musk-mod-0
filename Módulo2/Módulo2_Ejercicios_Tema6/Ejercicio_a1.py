'''
1. Haz un programa que cree una función en Python
que dada una secuencia devuelva únicamente los números pares.
Input: [5, 7, 3, 4, 2, 1]
Output: [4, 2]
'''


def numeros_pares(lista: list) -> list:
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares


if __name__ == '__main__':
    lista = [5, 7, 3, 4, 2, 1]

    listapares = numeros_pares(lista)
    print(listapares)
