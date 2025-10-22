'''
1_Implementa una función generadora que dadas
dos listas del mismo tamaño, devuelva la
multiplicación entre los elementos de cada una,
el primer elemento de la lista 1 por el primero de
la lista 2, el segundo con el segundo y así
sucesivamente. Sigue la siguiente estructura:
def prod(l1, l2):
    ...
    except StopIteration:
        pass
    return solution
Añadiendo el bloque except capturamos la
excepción de Stop Iteration que se produce al
acabar de leer todos los elementos de un
generador.

'''
import random
print('-----Ejercicio 1-----')


def prod(l1, l2):
    solution = []
    try:
        for i in range(len(l1)):
            yield l1[i] * l2[i]
    except StopIteration:
        pass
    return solution


l1 = [1, 2, 3]
l2 = [4, 5, 6]
solution = prod(l1, l2)

for n in solution:
    print(n)

'''
2_Implementa un generador, que dado un entero n,
genere n números aleatorios. Puedes usar el
método random de la librería random para
generar números aleatorios.
'''
print('-----Ejercicio 2-----')


def numAleatorios(n):
    print('Números aleatorios')
    i = 0
    while i < n:
        yield random.randint(1, 9)
        i += 1


nums = numAleatorios(5)

for n in nums:
    print(n)

'''
3_Implementa un generador de Fibonacci que
genere n números de la secuencia de Fibonaccі,
que tiene la forma:
0, 1, 1, 2, 3, 5, 8, 13, ...
Cuyos dos primeros valores son 0 y 1 por
definición y el resto se calculan sumando los dos
últimos valores de la sucesión.
'''
print('-----Ejercicio 3-----')


def fibonacci(n):
    print(f'Los primeros {n} números Fibonacci')
    x, y = 0, 1
    yield x
    for _ in range(n-1):
        x, y = y, x+y
        yield x


f = fibonacci(10)

for n in f:
    print(n)

'''
4_Implementa un generador, que dado un entero n,
imprima todos los números inferiores a n
multiplicados por dos.
'''

print('-----Ejercicio 4-----')


def numerosInf(n):

    print(f'Numeros inferiores a {n}, multiplicados por dos')
    for i in range(n):
        yield i*2


nI = numerosInf(10)

for i in nI:
    print(i)

'''
5_Implementa un generador, que dado un entero n,
genere n número senares.
'''
print('-----Ejercicio 5-----')

def numeroSenares(n):
    print(f'Los primeros {n} números Senares')
    num = 1
    for _ in range(n):
        yield num
        num += 2


nS = numeroSenares(10)

for i in nS:
    print(i)
