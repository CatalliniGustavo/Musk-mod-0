'''
2. Haz un programa que encuentre todas las apariciones de una subcadena en una cadena dada.
Input: Mi mamá me mima
Output: La subcadena mi aparece 2 en mi mamá me mima
'''
if __name__ == '__main__':
    frase = input('Ingresa una frase: ')
    subcadena = input('Ingresa una subcadena: ')

    contador = frase.lower().count(subcadena.lower())

    print('La subcadena "{}" aparece {} veces'.format(subcadena, contador))