'''
1. Haz un programa que lea una secuencia de caracteres acabada en punto
y que escriba cuántas letras ‘a’ contiene.
Input: Hoy hace un buen día
Output: La secuencia contiene 2 as
'''

if __name__ == '__main__':
    frase = input("Ingresa una frase: ")
    a = frase.lower().count('a')
    print('La letra "a" aparece {} veces'.format(a))
    # con bucles
    contador = 0
    for a in frase.lower():
        match a:# cuenta las 'a' que tengan acento
            case 'a':
                contador += 1
            case 'á':
                contador += 1

    print('La letra "a" aparece {} veces'.format(contador))

