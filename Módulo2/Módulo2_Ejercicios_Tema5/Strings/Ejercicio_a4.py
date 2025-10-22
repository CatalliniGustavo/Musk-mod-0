'''
4. Haz un programa que divida una cadena en guiones.
Input: 'hola-y-adios'
Output:
hola
y
adios
'''
if __name__ == '__main__':
    frase = input('Ingresa una frase: ')
    frase = frase.split('-')

    for i in frase:
        print(i)