'''
11. Haz un programa que devuelva el máximo de una secuencia de temperaturas acabada en 1000.
Input: 45 34 23 34 50 35 1000
Output: El máximo de la secuencia es 50
'''
if __name__ == '__main__':
    num = 0
    numant = 0
    while num != 1000:
        num = int(input('Ingresa un numero: '))
        if num > numant and num != 1000:
            numant = num
    print('El máximo de la secuencia es {}'.format(numant))