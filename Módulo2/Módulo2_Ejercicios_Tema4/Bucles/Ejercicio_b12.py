'''
12. Haz un programa que dada una secuencia de valores
acabada en 0 compruebe que ningún valor supera 50.
Input: 30 50 40 51
Output: 'Existe un elemento en la secuencia que supera el valor 50'
'''
if __name__ == '__main__':
    num = int(input('Ingresa un numero: '))
    numax = False
    while num != 0:
        if num > 50:
            numax = True
        num = int(input('Ingresa un numero: '))

    if numax:
        print('Existe un elemento en la secuencia que supera el valor 50')
    else:
        print('No existe un elemento que supera el valor 50')
