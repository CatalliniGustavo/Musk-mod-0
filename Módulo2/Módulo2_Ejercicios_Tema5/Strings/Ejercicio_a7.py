'''
7. Haz un programa que elimine cadenas vacías de una lista de cadenas.
Input: 'Esta cadena tiene espacios en blanco'
Output: 'Estacadenatieneespaciosenblanco'
'''
if __name__ == '__main__':
    frase = input('Ingresa una frase: ')
    frase = frase.replace(' ', '')
    print(frase)
    