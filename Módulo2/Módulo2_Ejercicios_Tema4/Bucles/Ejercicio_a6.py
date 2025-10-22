'''
6. Haz un programa que lea un número y que escriba el número de dígitos.
'''
if __name__ == '__main__':
    num = input('Ingrese un número: ')
    print('{} tiene {} cifras'.format(num, len(num)))

    print('Con un bucle:')
    numb = int(num)
    # con un bucle
    contador = 0
    while numb > 0:
        numb = numb // 10
        contador += 1
    print('{} tiene {} cifras'.format(num, contador))
