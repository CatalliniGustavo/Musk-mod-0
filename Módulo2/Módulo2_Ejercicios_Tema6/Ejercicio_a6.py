'''
6. Haz un que cree una función que escriba el cuadrado y la raíz cuadrada de una secuencia de naturales.
Input: [10, 4, 1, 15]
Output:
[100, 16, 1, 225]
[3.1622776601683795, 2.0, 1.0, 3.872983346207417]
'''
import math


def cuentas(numeros):
    cuadrado = []
    raiz = []
    for numero in numeros:
        cuadrado.append(pow(numero, 2))
    for numero in numeros:
        raiz.append(math.sqrt(numero))
    return cuadrado, raiz


if __name__ == '__main__':
    numeros = [10, 4, 1, 15]

    c, r = cuentas(numeros)
    print(c)
    print(r)
