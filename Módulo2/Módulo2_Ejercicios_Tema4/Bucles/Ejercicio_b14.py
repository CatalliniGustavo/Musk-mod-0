'''
14. Haz un programa que dada una secuencia de valores acabada en 0 diga si hay más positivos o negativos.
'''
if __name__ == '__main__':
    num = int(input('Ingresa un numero: '))
    neg = 0
    pos = 0
    while num != 0:
        if num > 0:
            pos += 1
        else:
            neg += 1
        num = int(input('Ingresa un numero: '))

    if pos > neg:
        print('Hay más positivos que negativos.')
    elif pos == neg:
        print('Hay la misma cantidad')
    else:
        print('Hay más negativos que positivos.')