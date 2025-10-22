'''
1. Haz un programa que lea dos palabras y que indique el orden lexicográfico. Escribe en una línea indicando
si a < b, a > b o a = b. Ejemplo: a = Anna, b = Javier, Anna < Javier.
Input: 'Anna' 'Javier'
output: Anna < Javier
'''
if __name__ == '__main__':
    palabra1 = input('Ingrese la 1° palabra: ')
    palabra2 = input('Ingrese la 2° palabra: ')

    if palabra1 < palabra2:
        print('{} < {}'.format(palabra1, palabra2))
    else:
        print('{} < {}'.format(palabra2, palabra1))
