'''
1. Haz un programa que lea un número decimal por pantalla, lo convierta a entero y lo imprima.
Input: 4.8
Output: 4
'''
print('-----Ejercicio 1-----')
decimal = float(input('Ingrese un número decimal: '))
entero = int(decimal)
print(entero)


'''
2. Haz un programa que lea un número decimal por pantalla e imprima su tipo y su valor redondeado en la misma línea.
Input: 4.8
Output: ",
    "Introduce un número decimal: 4.8",
    "Tipo: <class 'float'>, redondeo: 5"
'''

print('-----Ejercicio 2-----')
decimal = float(input('Introduce un número decimal: '))
#print('Tipo: ', type(decimal), ', redondeo: ', round(decimal))
print('Tipo: {} , redondeo: {}'.format(type(decimal), round(decimal)))


'''
3. Haz un programa que lea dos números por pantalla e imprima su diferencia en valor absoluto.
Input: 14 37
Output: Diferencia entre 14.0 y 37.0 es 23.0
'''

print('-----Ejercicio 3-----')
num1 = float(input('Ingrese el primer valor: '))
num2 = float(input('Ingrese el segundo valor: '))
diferencia = abs(num1 - num2)
print('Diferencia entre {} y {} es {}'.format(num1, num2, diferencia))
