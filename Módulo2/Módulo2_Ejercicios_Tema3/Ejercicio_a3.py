'''
3. Haz un programa que lea dos números por pantalla e imprima su diferencia en valor absoluto.
Input: 14 37
Output: Diferencia entre 14.0 y 37.0 es 23.0
'''
if __name__ == '__main__':
    num1 = float(input('Ingrese el primer valor: '))
    num2 = float(input('Ingrese el segundo valor: '))
    diferencia = abs(num1 - num2)
    print('Diferencia entre {} y {} es {}'.format(num1, num2, diferencia))
