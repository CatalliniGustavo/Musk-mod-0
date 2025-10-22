'''
16. Haz un programa que dada una secuencia de valores
enteros acabada en 0 diga cuántos son múltiples del primero.
Input: 3 9 12 4 0
Output: 'Existen 2 múltiples de 3'
'''
if __name__ == '__main__':
    num = int(input('Ingresa un numero: '))
    num1 = num
    contador = -1
    while num != 0:
        if num % num1 == 0:
            contador += 1
        num = int(input('Ingresa un numero: '))


    if contador > 0:
        print('Hay {} números múltiplos de {}'.format(contador, num1))
    else:
        print('No existen números múltiplos de {}'.format(num1))