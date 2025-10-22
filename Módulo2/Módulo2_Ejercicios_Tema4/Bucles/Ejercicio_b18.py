'''
18. Haz un programa que lea un natural n, y que escriba el resultado de la
suma siguiente: 1^2 + 2^2 + … + (n−1)^2 + n^2 y el aspecto de la secuencia.
'''
if __name__ == '__main__':
    num = int(input('Introduce un numero: '))
    suma = 0
    print('El resultado de la secuencia', end='')
    for i in range(num + 1):
        suma += pow(i,2)
        if i == 0:
            print('', i,'^2 ', end='')
        else:
            print('+', i, '^2 ', end='')
    print(' es {}'.format(suma))
