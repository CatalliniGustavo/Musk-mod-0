'''
10. Haz un programa que sustituya cada símbolo especial por # en la siguiente cadena.
Input: 'hoy* h$ace un b&uen dia@'
Output: 'hoy# h#ace un b#uen dia#'
'''
import string

if __name__ == '__main__':
    frase = input('Ingresa una frase: ')

    for c in string.punctuation:
        frase = frase.replace(c, '#')

    print(frase)