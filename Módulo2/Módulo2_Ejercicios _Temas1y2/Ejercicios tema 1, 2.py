'''
1. Haz un programa que escriba una línea con el mensaje “Buenos días a todo el mundo!"
Output: Buenos dias a todo el mundo!
'''
print('-----Ejercicio 1-----')
print('"Buenos días a todo el mundo!"')
'''

2. Haz un programa que declare tres palabras a, b y c, y que escriba una línea con c, b y a en este orden.
Input: 'hola' 'adios' 'hasta pronto'
Output: hasta pronto adios hola
'''

print('-----Ejercicio 2-----')
a = 'hola'
b = 'adios'
c = 'hasta pronto'
print('{} {} {}'.format(c, b, a))


'''
3. Haz un programa que declare dos números y que escriba la suma.
Input: 10 20 
Output: 30
'''

print('-----Ejercicio 3-----')
num1 = 10
num2 = 20
suma = num1 + num2
print('La suma es: {}'.format(suma))


'''
4. Haz un programa que declare dos números y que escriba el máximo.
Input: 10 20
Output: 20
'''

print('-----Ejercicio 4-----')
num1 = 10
num2 = 20
maximo = max(num1, num2)
print('El máximo es: {}'.format(maximo))


'''
5. Haz un programa que declare tres números, todos diferentes, y que escriba el máximo.
Input: 10 20 30
Output: 30
'''

print('-----Ejercicio 5-----')
num1 = 10
num2 = 20
num3 = 30
maximo = max(num1, num2, num3)
print('El máximo es: {}'.format(maximo))


'''
6. Hacer un programa que dado un valor calcule su cuadrado y el cubo.
Input: 10
Output: 100 1000
'''

print('-----Ejercicio 6-----')
num1 = 10
cuadrado = pow(num1, 2)
cubo = pow(num1, 3)
print("El cuadrado es: {} \nEl cubo es: {}".format(cuadrado, cubo))


'''
7. Haz un programa que devuelva el valor absoluto de un número.
Input: -10
Output: 10
'''

print('-----Ejercicio 7-----')
num1 = -10
absoluto = abs(num1)
print("El valor absoluto es: {}".format(absoluto))

'''
8. Haz un programa que lea dos naturales a y b, con b > 0, y que escriba la división entera d y el residuo r de a 
entre b. Recordad que, por definición, d y r tienen que ser los únicos enteros tales que 0 ≤ r < b y d · b + r = a. 
Ejemplo: a=32, b=5, d=6, r=2 ya que 32 = 5 * 6 + 2
Input: 32 5
Output: dividendo: 32, divisor: 5, residuo: 2, cociente: 6
'''

print('-----Ejercicio 8-----')
a = 32
b = 5
d = a // b
r = a % b
print("Dividendo: {}\nDivisor: {}\nResiduo: {}\nCociente: {}".format(a, b, r, d))


'''
9. Haz un programa que, dada una cantidad de segundos, diga cuántas horas, minutos y segundos representa.
Input: 3600
Output: 3600 segundos son 60.0 minutos y 1.0 horas
'''

print('-----Ejercicio 9-----')
segundos = 3600
minutos = segundos / 60
horas = segundos / 3600
print('{} segundos son {} minutos y {} horas'.format(segundos, minutos, horas))


'''
10. Haz un programa que dada una temperatura en grados Celsius la muestre en grados Fahrenheit y en grados Kelvin. 
(F= 1.8C + 32 y  ºK =°C + 273ºK).
Input: 40
Output:    
    "Temperatura en Celsius: 40",
    "Temperatura en Fahrenheit: 104.0",
    "Temperatura en Kelvin: 313",
'''

print('-----Ejercicio 10-----')
c = 40
f = 1.8 * c + 32
k = c + 273
print('Temperatura en Celcius: {}\nTemperatura en Fahrenheit: {}\nTemperatura en Kelvin: {}'.format(c, f, k))
