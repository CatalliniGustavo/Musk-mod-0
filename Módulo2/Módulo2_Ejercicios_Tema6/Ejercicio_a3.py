'''
3. Haz un programa que devuelva múltiples valores desde una función.
Crea la función calculaion() de modo que pueda aceptar dos variables y
calcular sumas y restas. Además, debe devolver tanto la suma como la resta en una sola llamada.
Input: 40 10
Output: 50 30
'''


def calculaion(num1, num2):
    return num1 + num2, num1 - num2


if __name__ == '__main__':
    num1 = 40
    num2 = 10
    print(calculaion(num1, num2))
