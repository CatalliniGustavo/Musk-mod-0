'''
2. Haz un programa que lea un número decimal por pantalla e imprima su tipo y su valor redondeado en la misma línea.
Input: 4.8
Output: ",
    "Introduce un número decimal: 4.8",
    "Tipo: <class 'float'>, redondeo: 5"
'''
if __name__ == '__main__':
    decimal = float(input('Introduce un número decimal: '))
    #print('Tipo: ', type(decimal), ', redondeo: ', round(decimal))
    print('Tipo: {} , redondeo: {}'.format(type(decimal), round(decimal)))
