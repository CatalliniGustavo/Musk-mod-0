'''
1. Haz un programa que lea una lista dado su tamaño e imprima el segundo elemento (si existe).
'''
import statistics
print('-----Ejercicio 1-----')
num = int(input('Ingresa el tamaño de la lista: '))
lista = []

for i in range(num):
    elemento = input('Ingresa un elemento a la lista: ')
    lista.append(elemento)

print(lista)
if len(lista) > 1:
    print('el segundo elemento de la lista es {}'.format(lista[1]))
else:
    print('no existe segundo elemento de la lista')


'''
2. Haz un programa que lea una secuencia no vacía de enteros acabada en -1,
y que escriba cuántos son iguales al último.
Input: 3 4 -2 3 -7 3 -1
Output: Existen 2 elementos iguales al último elemento
'''
print('-----Ejercicio 2-----')
lista = []
num = int(input('Ingresa un número a la lista: '))

while True:  # para que la lista no esté vacía
    if num != -1:
        break
    else:
        num = int(input('Ingresa un número a la lista: '))

while num != -1:
    lista.append(num)
    num = int(input('Ingresa un número a la lista: '))

print(lista)
contador = -1
for num in lista:
    if num == lista[len(lista)-1]:
        contador += 1
if contador >= 1:
    print('{} se repite {} veces'.format(lista[len(lista)-1], contador))


'''
3. Haz un programa que lea secuencias de enteros acabada en -1,
y que escriba cada una invirtiendo la orden de sus elementos.
Input: 3 -4 -5 6 -1
Output: [6, -5, -4, 3]
'''
print('-----Ejercicio 3-----')
lista = []
num = int(input('Ingresa un número a la lista: '))

while True:  # para que la lista no esté vacía
    if num != -1:
        break
    else:
        num = int(input('Ingresa un número a la lista: '))

while num != -1:
    lista.append(num)
    num = int(input('Ingresa un número a la lista: '))

lista.reverse()
print(lista)


'''
4. Haz un programa que lea n palabras, y que escriba
cada una invirtiendo la orden de sus caracteres.
Input:
hola
adios
hasta pronto
hasta luego
Output: ['aloh', 'soida', 'otnorp atsah', 'ogeul atsah']
'''
print('-----Ejercicio 4-----')
lista = []
n = int(input('Ingrese el largo de la lista: '))

for i in range(n):
    lista.append(input('ingresa la frase: '))
print(lista)

cont = 0
for x in lista:
    m = ''.join(reversed(x))
    lista[cont] = m
    cont += 1

print(lista)


'''
5. Haz un programa que lea una secuencia de números mientras sean positivos y que escriba la media.
Input: 4 10 5 12 -1
Output: 7.75
'''

print('-----Ejercicio 5-----')
num = int(input('Ingresa un numero: '))
while True:
    if num >= 0:
        break
    else:
        num = int(input('Ingresa un numero: '))
lista = []
while num >= 0:
    lista.append(num)
    num = int(input('Ingresa un numero: '))

promedio = statistics.mean(lista)
print('El promedio de la lista es: {}'.format(promedio))


'''
6. Haz un programa que devuelva la concatenación de v1 y v2, v1 y v2
son dos listas de tamaño n y m. Es decir, hay que devolver un vector
que tenga los elementos de v1 seguidos de los elementos de v2.
Input:
3
2
a b c
d e
Output: ['a', 'b', 'c', 'd', 'e']
'''
print('-----Ejercicio 6-----')
n = int(input('Ingrese la cantidad de elementos de la lista 1: '))
m = int(input('Ingrese la cantidad de elementos de la lista 2: '))
lista1 = []
for i in range(0, n):
    lista1.append(input('valor lista 1: '))

for i in range(0, m):
    lista1.append(input('valor lista 2: '))

print(lista1)


'''
7. Haz un programa que almacene en una lista los
siguientes precios, 50, 75, 46, 22, 80, 65, 8,
y muestre por pantalla el menor y el mayor de los precios.
'''
print('-----Ejercicio 7-----')
lista = [50, 75, 46, 22, 80, 65, 8]
print('menor {} mayor {}'.format(min(lista), max(lista)))


'''
8. Haz un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
en una lista y la muestre por pantalla.
'''
print('-----Ejercicio 8-----')
lista = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']

for item in lista:
    print(item)


'''
9. Haz un programa que almacene en una lista los números del 1 al 10
y los muestre por pantalla en orden inverso separados por comas.
'''
print('-----Ejercicio 9-----')
lista = list(range(1, 11))

for i in range(len(lista), 0, -1):
    if i == 1:
        print('{}'.format(lista[0]))
    else:
        print('{}, '.format(lista[i-1]), end='')


'''
10. Haz un programa que concatene dos listas del
mismo tamaño n alternando elementos de una lista y otra.
'''
print('-----Ejercicio 10-----')
n = int(input('Ingresa el largo de las listas: '))
lista1 = []
for i in range(0, n):
    lista1.append(input('Ingresa un elemento a la lista 1: '))

lista2 = []
for i in range(0, n):
    lista2.append(input('Ingresa un elemento a la lista 2: '))

listaf = []
for i in range(0, n):
    listaf.append(lista1[i])
    listaf.append(lista2[i])
print(listaf)


'''
11. Haz un programa que itere ambas listas de tamaños n y m
(siendo n y m números distintos) simultáneamente e imprima sus elementos.
'''
print('-----Ejercicio 11-----')
n = int(input('Ingresa el tamaño de la lista 1: '))
m = int(input('Ingresa el tamaño de la lista 2: '))
lista1 = []
for i in range(0, n):
    lista1.append(input('Ingresa un elemento a la lista 1: '))

lista2 = []
for i in range(0, m):
    lista2.append(input('Ingresa un elemento a la lista 2: '))

maxi = max(n, m)
for i in range(0, maxi):
    if i < len(lista1):
        print(lista1[i])
    if i < len(lista2):
        print(lista2[i])

'''
12. Haz un programa que añada un nuevo elemento 60
a la lista [10, 50, 40, 20, 30] después de un
elemento especificado por el usuario. Si el elemento
introducido no está presente en la lista debe mostrar el mensaje:
'Elemento no presente en la lista'.
'''
print('-----Ejercicio 12-----')
lista = [10, 50, 40, 20, 30]
num = int(input('Ingresa un numero: '))

lista2 = []
if num in lista:
    for i in range(0, 5):
        if lista[i] == num:
            lista2.append(lista[i])
            lista2.append(60)
        else:
            lista2.append(lista[i])
    print(lista2)
else:
    print('Elemento no está presente en la lista')


'''
13. Haz un programa que elimine todas las apariciones
de un elemento específico introducido por el usuario
de la lista [10, 50, 40, 20, 60, 30].
'''
print('-----Ejercicio 13-----')
lista = [10, 50, 40, 20, 60, 30]
num = int(input('Ingresa un numero que quiera eliminar de la lista: '))
if num in lista:
    while num in lista:
        lista.remove(num)
    print(lista)
else:
    print('Elemento no está presente en la lista')
