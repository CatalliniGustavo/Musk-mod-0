'''
7. Haz un programa que cree una función que deje a, b y c ordenados
de pequeño a grande. Por ejemplo, si a =7, b = −3 y c = 1, los valores
después de la llamada deben ser a =−3, b = 1 y c = 7.
Input: 7 -3 1
Output: -3 1 7
'''
import sys

def ordenados(lista):
    lista.sort()
    return lista


if __name__ == '__main__':
    lista = [7, -3, 1]
    s = '''hola
    mundo
    '''
    print(ordenados(lista))
    print(s)