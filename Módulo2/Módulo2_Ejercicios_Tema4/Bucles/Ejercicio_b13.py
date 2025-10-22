'''
13. Haz un programa que dada una secuencia de valores acabada en 0
compruebe que ningún valor supera 50 y que no hay más de tres que superen 40.
Input: 50 43 42 21 0
Output:
Ningún elemento en la secuencia supera el valor 50
No existen más de tres elementos en la secuencia que superan el valor 40
'''
if __name__ == '__main__':
    num = int(input('Ingresa un numero: '))
    numax = False
    contador = 0
    while num != 0:
        if num > 50:
            numax = True
        if num > 40:
            contador += 1
        num = int(input('Ingresa un numero: '))

    if numax:
        print('Existe un elemento en la secuencia que supera el valor 50')
    else:
        print('No existe un elemento que supera el valor 50')
    if contador > 3:
        print('Existen más de 3 elemento que supera el valor 40')
    else:
        print('No existe más de 3 elemento que supera el valor 40')