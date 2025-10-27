'''
1. Haz un programa que cree una función en Python
que dada una secuencia devuelva únicamente los números pares.
Input: [5, 7, 3, 4, 2, 1]
Output: [4, 2]
'''

import math


print('-----Ejercicio 1-----')
def numeros_pares(lista: list) -> list:
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares


lista = [5, 7, 3, 4, 2, 1]

listapares = numeros_pares(lista)
print(listapares)


'''
2. Haz un programa que cree una función con longitud variable de argumentos.
Input: func1(20, 40, 60)
Output:
20
40
60
'''

print('-----Ejercicio 2-----')


def imprimirLista(*lista):
    for elemento in lista:
        print(elemento)


imprimirLista(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


'''
3. Haz un programa que devuelva múltiples valores desde una función.
Crea la función calculaion() de modo que pueda aceptar dos variables y
calcular sumas y restas. Además, debe devolver tanto la suma como la resta en una sola llamada.
Input: 40 10
Output: 50 30
'''

print('-----Ejercicio 3-----')


def calculaion(num1, num2):
    return num1 + num2, num1 - num2


num1 = 40
num2 = 10
print(calculaion(num1, num2))


'''
4. Haz un programa que cree una función con un argumento por defecto.
Crea una función show_employee() usando las siguientes condiciones.
-Debe aceptar el nombre y el salario del empleado y mostrar ambos.
-Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al salario.
Input:
showEmployee("Ben", 12000)
showEmployee("Jessa")
Output:
Name: Ben salary: 12000
Name: Jessa salary: 9000
'''

print('-----Ejercicio 4-----')


def show_employee(employee, salary=9000):
    print(f'{employee}: {salary}')


show_employee("Ben", 12000)
show_employee("Jessa")


'''
5. Haz un programa que cree una función interna para calcular la suma
de la siguiente manera: Crea una función externa que acepte dos
parámetros, a y b. Crea una función interna dentro de una función
externa que calculará la suma de a y b. Por último, una función
externa que sumará 5 en la suma y la devolverá.
Input: 5 10
Output: 20
'''

print('-----Ejercicio 5-----')


def externa(a, b):
    def suma():
        return a + b

    r = suma()
    return r + 5


print(externa(5, 10))


'''
6. Haz un que cree una función que escriba el cuadrado y la raíz cuadrada de una secuencia de naturales.
Input: [10, 4, 1, 15]
Output:
[100, 16, 1, 225]
[3.1622776601683795, 2.0, 1.0, 3.872983346207417]
'''

print('-----Ejercicio 6-----')


def cuentas(numeros):
    cuadrado = []
    raiz = []
    for numero in numeros:
        cuadrado.append(pow(numero, 2))
    for numero in numeros:
        raiz.append(math.sqrt(numero))
    return cuadrado, raiz


numeros = [10, 4, 1, 15]

c, r = cuentas(numeros)
print(c)
print(r)


'''
7. Haz un programa que cree una función que deje a, b y c ordenados
de pequeño a grande. Por ejemplo, si a =7, b = −3 y c = 1, los valores
después de la llamada deben ser a =−3, b = 1 y c = 7.
Input: 7 -3 1
Output: -3 1 7
'''
print('-----Ejercicio 7-----')


def ordenados(lista):
    lista.sort()
    return lista


lista = [7, -3, 1]
print(ordenados(lista))
