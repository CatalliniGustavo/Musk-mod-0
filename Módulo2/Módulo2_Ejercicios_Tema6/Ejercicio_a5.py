'''
5. Haz un programa que cree una función interna para calcular la suma
de la siguiente manera: Crea una función externa que acepte dos
parámetros, a y b. Crea una función interna dentro de una función
externa que calculará la suma de a y b. Por último, una función
externa que sumará 5 en la suma y la devolverá.
Input: 5 10
Output: 20
'''


def externa(a, b):
    def suma():
        return a + b

    r = suma()
    return r + 5


if __name__ == '__main__':
    print(externa(5, 10))
