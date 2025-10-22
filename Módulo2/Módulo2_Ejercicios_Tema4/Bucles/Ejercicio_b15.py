'''
15. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga
cuál es el número que hay antes de primer negativo encontrado.
'''
if __name__ == '__main__':
    num = int(input('Ingresa un numero: '))
    numant = None
    negativo = False
    while num > 0:
        num = int(input('Ingresa un numero: '))
        if num < 0:
            negativo = True# por si no se ingresa un valor negativo
            break
        numant = num

    while num != 0:
        num = int(input('Ingresa un numero: '))

    if numant is None:
        print('No existe número anterior al primer negativo.')
    elif not negativo:
        print('No se ingresó un número negativo.')
    else:
        print('El valor anterior al primer negativo es {}'.format(numant))
