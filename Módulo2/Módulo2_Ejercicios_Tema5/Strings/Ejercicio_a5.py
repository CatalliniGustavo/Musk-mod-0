'''
5. Haz un programa que añada una nueva cadena en medio de una cadena dada.
Input: 'hola hola'
Output: 'hola adioshola'
'''
if __name__ == '__main__':
    frase1 = input('Ingrese una frase: ')
    frase2 = input('Ingrese la frase a añadir: ')
    mitad = int(len(frase1) / 2)
    parte1 = frase1[:mitad]
    parte2 = frase1[mitad:]
    frasefinal = parte1 + frase2 + parte2
    print(frasefinal)