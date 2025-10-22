'''
9. Haz un programa que encuentre palabras con letras y números.
Input: 'hoy25 hace un b4uen5 día'
Output: 'hoy25 b4uen5'

s = input('Introduce una cadena: ')

seq = s.split()

resultado = ''

for item in seq:
    # Si tiene algun caracter que pertenece al alfabeto y contiene algún número
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        resultado = resultado + ' ' + item
        
# Eliminamos el espacio del inicio
resultado = resultado[1:]
print(resultado)
'''
if __name__ == '__main__':
    frase = input('Ingresa una frase: ')
    frase2 = frase.split()
    frasefinal = ''

    for palabra in frase2:
        l = False
        n = False
        for letra in palabra:
            if letra.isalpha():
                l = True
            if letra.isdigit():
                n = True
        if l and n:
            frasefinal += palabra + ' '

    print(frasefinal)