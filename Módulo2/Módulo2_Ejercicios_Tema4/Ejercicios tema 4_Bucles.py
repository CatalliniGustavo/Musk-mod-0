'''
1. Haz un programa que lea dos números a y b, y que escriba todos los números enteros a y b.
Debe cumplirse que a < b. En caso que a > b, escribe los número de manera descendente.
'''
import math
print('-----Ejercicio 1-----')
num1 = int(input('Ingresa el 1° numero: '))
num2 = int(input('Ingresa el 2° numero: '))

if num1 < num2:
    for num in range(num1, num2 + 1):
        print('[{}] '.format(num), end="")
else:
    for num in range(num1, num2 - 1, -1):
        print('[{}] '.format(num), end="")

print('')

'''
2. Haz un programa que lea una secuencia de 10 números y que escriba la media.
'''
print('-----Ejercicio 2-----')
lista = []

for i in range(10):
    lista.insert(i, int(input('Ingrese el {}° número: '.format(i + 1))))


suma = sum(lista)/10
print('El promedio es: {}'.format(suma))


'''
3. Haz un programa que dada una lista de naturales de tamaño n, indique la posición del primer número par.
'''

print('-----Ejercicio 3-----')
largo = int(input('Ingrese la longitud de la lista: '))
lista = list(range(largo))

for i in range(largo):
    lista.insert(i, int(input('Ingrese el {}° número: '.format(i + 1))))
    if lista[i] % 2 == 0:
        print(lista[i], ' en la posición: {}'.format(i))
        break  # finaliza cuando se ingresa el primer valor par de la lista

'''
4. Haz un programa que lea un número n y que escriba la “tabla de multiplicar” de n.
'''
print('-----Ejercicio 4-----')
num = int(input('Ingrese un número: '))
for i in range(11):
    print('{} x {} = {}'.format(num, i, num * i))

'''
5. Haz un programa que lea un número y que lo escriba del revés.
'''
print('-----Ejercicio 5-----')
num = input('Ingrese un número de tres cifras: ')
for i in range(len(num), 0, -1):
    print(num[i-1], end="")


'''
6. Haz un programa que lea un número y que escriba el número de dígitos.
'''
print('-----Ejercicio 6-----')
num = input('Ingrese un número: ')
print('{} tiene {} cifras'.format(num, len(num)))

print('Con un bucle:')
numb = int(num)
# con un bucle
contador = 0
while numb > 0:
    numb = numb // 10
    contador += 1
print('{} tiene {} cifras'.format(num, contador))


'''
7. Haz un programa que diga si un natural n es capicua o no.
'''
print('-----Ejercicio 7-----')
num = input('Ingrese un número: ')
numpost = ''
for i in range(len(num) - 1, -1, -1):
    numpost = numpost + num[i]

print('{} {} '.format(num, numpost))
if num == numpost:
    print('Es capicua!!!')
else:
    print('No es capicua!!!')


'''
8. Haz un programa que dada una secuencia de años acabada en 0 nos diga cuántos hay del siglo 20.
Input: 1950 1900 2000 1910 1800 0
Output: Existen 3 años que pertenecen al siglo XX
'''
print('-----Ejercicio 8-----')
anio = int(input('Ingresa un año terminados en cero: '))

contador = 0
while anio != 0:
    anioaux = anio
    anio = anio // 100
    if anio + 1 == 20:
        contador += 1
        print(anioaux, ' Pertenece al siglo xx')
    anio = int(input('Ingresa un año terminados en cero: '))

print('Existe {} años que pertenecen al siglo xx'.format(contador))


'''
9. Haz un programa que reciba una secuencia de naturales de tamaño n
y nos devuelva cuál es el primer natural que tiene un valor inferior al primer natural leído.
'''
print('-----Ejercicio 9-----')
largo = int(input('Ingrese el largo de la lista de números: '))
lista = [] * largo
nreferencia = 0
# llenado de la lista y toma el número de referencia
for i in range(largo):
    if i == 0:
        nreferencia = int(input('Ingrese el {}° número: '.format(i + 1)))
        lista.insert(i, nreferencia)
    else:
        lista.insert(i, int(input('Ingrese el {}° número: '.format(i + 1))))

# Busca el menor si hay
haymenor = False
nmenor = nreferencia
for i in lista:
    if i < nreferencia:
        nmenor = i
        haymenor = True
        break

for i in lista:
    print(i, end=' ')

print('')

if haymenor:
    print('El primer meno a "{}" es el "{}"'.format(nreferencia, nmenor))
else:
    print('No se ha encontrado ningún valor menor.')


'''
10. Haz un programa que cuente cuántos valores hay en una secuencia de enteros acabada en 0.
'''
print('-----Ejercicio 10-----')
contador = 0
numero = int(input('Ingresa un numero: '))
# simula un do_while por si no se ingresa ningún valor
while True:
    if numero == 0:
        break
    else:
        numero = int(input('Ingresa un numero: '))
        contador += 1

print('La lista tiene {} valores'.format(contador))


'''
11. Haz un programa que devuelva el máximo de una secuencia de temperaturas acabada en 1000.
Input: 45 34 23 34 50 35 1000
Output: El máximo de la secuencia es 50
'''
print('-----Ejercicio 11-----')
num = 0
numant = 0
while num != 1000:
    num = int(input('Ingresa un numero: '))
    if num > numant and num != 1000:
        numant = num
print('El máximo de la secuencia es {}'.format(numant))


'''
12. Haz un programa que dada una secuencia de valores
acabada en 0 compruebe que ningún valor supera 50.
Input: 30 50 40 51
Output: 'Existe un elemento en la secuencia que supera el valor 50'
'''
print('-----Ejercicio 12-----')
num = int(input('Ingresa un numero: '))
numax = False
while num != 0:
    if num > 50:
        numax = True
    num = int(input('Ingresa un numero: '))

if numax:
    print('Existe un elemento en la secuencia que supera el valor 50')
else:
    print('No existe un elemento que supera el valor 50')


'''
13. Haz un programa que dada una secuencia de valores acabada en 0
compruebe que ningún valor supera 50 y que no hay más de tres que superen 40.
Input: 50 43 42 21 0
Output:
Ningún elemento en la secuencia supera el valor 50
No existen más de tres elementos en la secuencia que superan el valor 40
'''
print('-----Ejercicio 13-----')
num = int(input('Ingresa un numero: '))
numax = False
contador = 0
while num != 0:
    if num > 50:
        numax = True
    if num > 40:
        contador += 1
    num = int(input('Ingresa un numero: '))

if numax:
    print('Existe un elemento en la secuencia que supera el valor 50')
else:
    print('No existe un elemento que supera el valor 50')
if contador > 3:
    print('Existen más de 3 elemento que supera el valor 40')
else:
    print('No existe más de 3 elemento que supera el valor 40')


'''
14. Haz un programa que dada una secuencia de valores acabada en 0 diga si hay más positivos o negativos.
'''
print('-----Ejercicio 14-----')
num = int(input('Ingresa un numero: '))
neg = 0
pos = 0
while num != 0:
    if num > 0:
        pos += 1
    else:
        neg += 1
    num = int(input('Ingresa un numero: '))

if pos > neg:
    print('Hay más positivos que negativos.')
elif pos == neg:
    print('Hay la misma cantidad')
else:
    print('Hay más negativos que positivos.')


'''
15. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga
cuál es el número que hay antes de primer negativo encontrado.
'''
print('-----Ejercicio 15-----')
num = int(input('Ingresa un numero: '))
numant = None
negativo = False
while num > 0:
    num = int(input('Ingresa un numero: '))
    if num < 0:
        negativo = True  # por si no se ingresa un valor negativo
        break
    numant = num

while num != 0:
    num = int(input('Ingresa un numero: '))

if numant is None:
    print('No existe número anterior al primer negativo.')
elif not negativo:
    print('No se ingresó un número negativo.')
else:
    print('El valor anterior al primer negativo es {}'.format(numant))


'''
16. Haz un programa que dada una secuencia de valores
enteros acabada en 0 diga cuántos son múltiples del primero.
Input: 3 9 12 4 0
Output: 'Existen 2 múltiples de 3'
'''
print('-----Ejercicio 16-----')
num = int(input('Ingresa un numero: '))
num1 = num
contador = -1
while num != 0:
    if num % num1 == 0:
        contador += 1
    num = int(input('Ingresa un numero: '))


if contador > 0:
    print('Hay {} números múltiplos de {}'.format(contador, num1))
else:
    print('No existen números múltiplos de {}'.format(num1))


'''
17. Haz un programa que lea varias descripciones de rectángulos y de círculos,
y que para cada una escriba el área correspondiente. La entrada empieza con un
número n, seguido de n descripciones. Si es de un rectángulo, se tiene la
palabra “rectángulo” seguida de dos reales estrictamente positivos que indican
la longitud y la anchura. Si es de un círculo, se tiene la palabra “círculo”
seguida de un real estrictamente positivo que indica el radio.
Input:
Introduce la longitud de la secuencia: 2
Introduce el nombre del polígono: rectangulo
Introduce la longitud del rectángulo: 10
Introduce la anchura del rectángulo: 5
El rectangulo tiene area 50.0
Introduce el nombre del polígono: circulo
Introduce el radio del círculo: 4
El circulo tiene area 50.26548245743669
'''

print('-----Ejercicio 17-----')
num = int(input('Introduce la longitud de la secuencia: '))
'''
 for i in range(num):
     opc = input('Introduce el nombre del polígono: ')
     match opc:
         case 'rectangulo':
             longrec = int(input('Introduce la longitud del rectángulo: '))
             anchrec = int(input('Introduce la anchura del rectángulo: '))
             print('El rectángulo tiene un area de {}'.format(longrec * anchrec))
         case 'circulo':
             radio = float(input('Introduce el radio del círculo: '))
             print('El círculo tiene un area de {}'.format(math.pi * pow(radio, 2)))
         case _:
             i -= 1
             print('La opción no existe {}'.format(i))
'''  # opción usando la función match

for i in range(0, num):
    opc = input('Introduce el nombre del polígono: ')
    if opc.lower() == 'rectangulo':
        longrec = int(input('Introduce la longitud del rectángulo: '))
        anchrec = int(input('Introduce la anchura del rectángulo: '))
        print('El rectángulo tiene un area de {}'.format(longrec * anchrec))
    elif opc.lower() == 'circulo':
        radio = float(input('Introduce el radio del círculo: '))
        print('El círculo tiene un area de {}'.format(math.pi * pow(radio, 2)))
    else:
        i -= 1  # Descuenta una opción fallida
        print('La opción no existe')


'''
18. Haz un programa que lea un natural n, y que escriba el resultado de la
suma siguiente: 1^2 + 2^2 + … + (n-1)^2 + n^2 y el aspecto de la secuencia.
'''
print('-----Ejercicio 18-----')
num = int(input('Introduce un numero: '))
suma = 0
print('El resultado de la secuencia', end='')
for i in range(num + 1):
    suma += pow(i, 2)
    if i == 0:
        print('', i, '^2 ', end='')
    else:
        print('+', i, '^2 ', end='')
print(' es {}'.format(suma))
