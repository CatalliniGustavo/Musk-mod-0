'''
1. Haz un programa que lea una secuencia de caracteres acabada en punto
y que escriba cuántas letras ‘a’ contiene.
Input: Hoy hace un buen día
Output: La secuencia contiene 2 as
'''


import string

print('-----Ejercicio 1-----')

frase = input("Ingresa una frase: ")
a = frase.lower().count('a')
print('La letra "a" aparece {} veces'.format(a))
# con bucles
contador = 0
for a in frase.lower():
    match a:  # cuenta las 'a' que tengan acento
        case 'a':
            contador += 1
        case 'á':
            contador += 1

print('La letra "a" aparece {} veces'.format(contador))

'''
2. Haz un programa que encuentre todas las apariciones de una subcadena en una cadena dada.
Input: Mi mamá me mima
Output: La subcadena mi aparece 2 en mi mamá me mima
'''
print('-----Ejercicio 2-----')

frase = input('Ingresa una frase: ')
subcadena = input('Ingresa una subcadena: ')

contador = frase.lower().count(subcadena.lower())

print('La subcadena "{}" aparece {} veces'.format(subcadena, contador))


'''
3. Haz un programa que invierta una cadena dada.
Input: hola y adios
Output: soida y aloh
'''
print('-----Ejercicio 3-----')

frase = input('Ingresa una frase: ')
# con un bucle
for i in range(len(frase)-1, -1, -1):
    print(frase[i], end='')
print('')
# otras opciones
reversa = frase[::-1]
print(reversa)
reversa = ''
reversa = ''.join(reversed(reversa))
print(frase[::-1])

'''
4. Haz un programa que divida una cadena en guiones.
Input: 'hola-y-adios'
Output:
hola
y
adios
'''
print('-----Ejercicio 4-----')

frase = input('Ingresa una frase: ')
frase = frase.split('-')

for i in frase:
    print(i)

'''
5. Haz un programa que añada una nueva cadena en medio de una cadena dada.
Input: 'hola hola'
Output: 'hola adioshola'
'''
print('-----Ejercicio 5-----')

frase1 = input('Ingrese una frase: ')
frase2 = input('Ingrese la frase a añadir: ')
mitad = int(len(frase1) / 2)
parte1 = frase1[:mitad]
parte2 = frase1[mitad:]
frasefinal = parte1 + frase2 + parte2
print(frasefinal)


'''
6. Haz un programa que encuentre la última posición de una subcadena dada.
Input: mi casa, tu casa
Output: La segunda cadena empieza en la posición 12
'''
print('-----Ejercicio 6-----')

frase1 = input("Ingresa una frase: ")
frase2 = input("Ingresa la frase a buscar: ")
posicion = frase1.lower().rfind(frase2)

if posicion != -1:
    print('La segunda frase empieza en la posición {}'.format(posicion))
else:
    print('No se ha encontrado la frase "{}"'.format(frase2))


'''
7. Haz un programa que elimine cadenas vacías de una lista de cadenas.
Input: 'Esta cadena tiene espacios en blanco'
Output: 'Estacadenatieneespaciosenblanco'
'''
print('-----Ejercicio 7-----')

frase = input('Ingresa una frase: ')
frase = frase.replace(' ', '')
print(frase)


'''
8. Haz un programa que elimine símbolos especiales / signos de puntuación de una cadena.
Input: '*Hoy hace & un@ día'
Output: 'Hoy hace  un día'
'''

print('-----Ejercicio 8-----')

frase = input('Ingresa una frase: ')
frase2 = frase.translate(str.maketrans('', '', string.punctuation))
print(frase2)

'''
9. Haz un programa que encuentre palabras con letras y números.
Input: 'hoy25 hace un b4uen5 día'
Output: 'hoy25 b4uen5'
'''
print('-----Ejercicio 9-----')

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


'''
10. Haz un programa que sustituya cada símbolo especial por # en la siguiente cadena.
Input: 'hoy* h$ace un b&uen dia@'
Output: 'hoy# h#ace un b#uen dia#'
'''

print('-----Ejercicio 10-----')

frase = input('Ingresa una frase: ')

for c in string.punctuation:
    frase = frase.replace(c, '#')

print(frase)
