'''
8. Haz un programa que elimine símbolos especiales / signos de puntuación de una cadena.
Input: '*Hoy hace & un@ día'
Output: 'Hoy hace  un día'
'''
import string

if __name__ == '__main__':
    frase = input('Ingresa una frase: ')
    frase2 = frase.translate(str.maketrans('', '', string.punctuation))
    print(frase2)