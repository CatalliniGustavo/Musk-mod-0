'''
1. Haz un programa que lea dos palabras y que indique el orden lexicográfico. Escribe en una línea indicando
si a < b, a > b o a = b. Ejemplo: a = Anna, b = Javier, Anna < Javier.
Input: 'Anna' 'Javier'
output: Anna < Javier
'''

print('-----Ejercicio 1-----')
palabra1 = input('Ingrese la 1° palabra: ')
palabra2 = input('Ingrese la 2° palabra: ')

if palabra1 < palabra2:
    print('{} < {}'.format(palabra1, palabra2))
else:
    print('{} < {}'.format(palabra2, palabra1))


'''
2. Haz un programa que lea una letra y que indique por pantalla si es una mayúscula, si es una minúscula,
si es una vocal, y si es una consonante.
'''
print('-----Ejercicio 2-----')
letra = input('Ingrese una letra: ')
l = letra[0]

if l.islower():
    print('{} es minúscula'.format(l))
else:
    print('{} es mayúscula'.format(l))
if l.lower() in ['a', 'e', 'i', 'o', 'u']:
    print('{} es vocal'.format(l))
else:
    print('{} es consonante'.format(l))

'''
3. Haz un programa que lea un entero que representa una temperatura en grados Celsius,
y que diga si hace calor, si hace frío, o si se está bien. Suponed que hace calor si
la temperatura es más alta que 30 grados, que hace frío si es más baja que 10 grados,
y que se está bien en otro caso.
Input: 25
Output: 'Se está bien'
'''

print('-----Ejercicio 3-----')

celsius = int(input('Ingresa la temperatura: '))
if celsius > 30:
    print('Hace calor')
elif celsius < 10:
    print('Hace frio')
else:
    print('Está bien')

'''
4. Haz un programa que, dados dos intervalos, calcule el intervalo correspondiente a la
intersección o indique que esta es vacía.
'''

print('-----Ejercicio 4-----')
i1min = int(input('Introduce el minimo del 1° intervalo: '))
i1max = int(input('Introduce el máximo del 1° intervalo: '))
i2min = int(input('Introduce el minimo del 2° intervalo: '))
i2max = int(input('Introduce el máximo del 2° intervalo: '))
aux = i1max

   # ordena los intervalos
if i1max < i1min:
    i1max = i1min
    i1min = aux

aux = i2max
if i2max < i2min:
    i2max = i2min
    i2min = aux

# determina el minimo y máximo de la intersección
minimo = i1min
if i1min < i2min:
    minimo = i2min
maximo = i2max
if i2max > i1max:
    maximo = i1max

if minimo <= maximo:
    print('[{} , {}]'.format(minimo, maximo))
else:
    print('[]')


'''
5. Haz un programa que indique si un año es bisiesto o no. Un año bisiesto tiene 366 días.
Después de la reforma gregoriana, los años bisiestos son los múltiplos de cuatro que no
acaban en dos ceros, y también los acabados en dos ceros tales que el número que queda
después de sacar los dos ceros finales es divisible por cuatro. Así, 1800 y 1900, a pesar
de ser múltiples de cuatro, no fueran bisiestos; en cambio, 2000 lo fue.
'''

print('-----Ejercicio 5-----')
fecha = int(input("Ingresa un año: "))
if fecha % 4 == 0:
    if fecha % 100 != 0 and fecha % 400 != 0:
        print("Bisiesto")
    else:
        print("no bisiesto")
else:
    print("no bisiesto")


'''
6. Haz un programa que añada un segundo en una hora del día, dadas sus horas, minutos y segundos.
'''

print('-----Ejercicio 6-----')
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

#para que los datos ingresados estén dentro de los parámetros
while 0 > horas or horas > 24:
    horas = int(input("Horas: "))
while 0 > minutos or minutos > 59:
    minutos = int(input("Minutos: "))
while 0 > segundos or segundos > 59:
    segundos = int(input("Segundos: "))

segundos += 1
if segundos > 59:
    segundos = 0
    minutos += 1
    if minutos > 59:
        minutos = 0
        horas += 1
        if horas >= 24:
            horas = 0
print('Horas: {} , Minutos: {} , Segundos: {}'.format(horas, minutos, segundos))


'''
7. Haz un programa que lea un real x≥0 y que escriba
⌊x⌋ (la parte entera inferior de x),
⌈x⌉ (la parte entera superior de x),
y el redondeo de x.
'''

print('-----Ejercicio 7-----')
real = float(input('Ingrese un número real: '))
inferior = int(real)
superior = int(real) + 1
redondeo = int(real + 0.5)
print('Parte inferior: [{}]\nParte superior: [{}]\nRedondeo: [{}]'.format(inferior, superior, redondeo) )
