'''
6. Haz un programa que encuentre la última posición de una subcadena dada.
Input: mi casa, tu casa
Output: La segunda cadena empieza en la posición 12
'''
if __name__ == '__main__':
    frase1 = input("Ingresa una frase: ")
    frase2 = input("Ingresa la frase a buscar: ")
    posicion = frase1.lower().rfind(frase2)

    if posicion != -1:
        print('La segunda frase empieza en la posición {}'.format(posicion))
    else:
        print('No se ha encontrado la frase "{}"'.format(frase2))
