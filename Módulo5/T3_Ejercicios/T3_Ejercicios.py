'''
1_Crea un array de enteros 4X2 e imprime sus
atributos. Nota: El elemento debe ser de tipo
unsignedint16. Imprime los siguientes atributos:
La shape del array.
Las dimensiones del array.
El tamaño de cada elemento del array en bytes.
'''

import numpy as np

print('-----Ejercicio 1-----')
array1 = np.array([[1, 2],
                   [3, 4],
                   [5, 6],
                   [7, 8]])
print(array1)
array1 = array1.astype(np.uint16)
print(f'Tipo de datos: {array1.dtype}')
print(f'Shape: {array1.shape}')
print(f'Dimensiones: {array1.ndim}')
print(f'Cantidad de datos: {array1.size}')
print(f'Tamaño en bits de cada elemento: {array1.itemsize}')

'''
2_Crea una matriz de enteros 5X2 de un rango
entre 100 y 200 tal que la diferencia entre cada
elemento sea 10
'''

print('-----Ejercicio 2-----')
array2 = np.linspace(100, 200, 10)
array2 = array2.reshape((5, 2))
print(array2)

'''
3_A continuación se muestra el array Numpy
proporcionado. Devuelve un array de elementos
tomando la tercera columna de todas las filas.
sampleArray = numpy.array([[11,22, 33], [44, 55, 66], [77, 88, 99]])
'''
print('-----Ejercicio 3-----')
sampleArray = np.array([[11, 22, 33],
                        [44, 55, 66],
                        [77, 88, 99]])
array3 = sampleArray[:, 2]
print(array3)


'''
4_Devuelve un array de filas impares y columnas
pares dado el siguiente array:
sampleArray = numpy.array([[3,6, 9, 12], [15,18, 21, 24],
[27,30, 33, 36], [39,42, 45, 48], [51,54, 57, 60]])
'''

print('-----Ejercicio 4-----')
sampleArray = np.array([[3, 6, 9, 12],
                        [15, 18, 21, 24],
                        [27, 30, 33, 36],
                        [39, 42, 45, 48],
                        [51, 54, 57, 60]])
array4 = sampleArray[1::2, ::2]
print(array4)

'''
5_Crea una matriz de resultados sumando las
siguientes dos matrices de NumPy. A
continuación, modifica la matriz de resultados
calculando el cuadrado de cada elemento.
arrayone = numpy.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4,7, 1]])
'''

print('-----Ejercicio 5-----')
arrayone = np.array([[5, 6, 9],
                     [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24],
                     [4, 7, 1]])
resultado = arrayone + arrayTwo
print('Suma de las dos matrices:')
print(resultado)
resultado = np.square(resultado)
print('El cuadrado de cada elemento:')
print(resultado)


'''
6_Divide la matriz en cuatro submatrices de igual
tamaño. Nota: Crea una matriz de enteros 8x3
de un rango entre 10 y 34 de tal manera que la
diferencia entre cada elemento sea 1 y luego
divide la matriz en cuatro submatrices de igual
tamaño
'''

print('-----Ejercicio 6-----')
array6 = np.linspace(10, 34, 24)
array6 = array6.reshape((8, 3))
print(array6)
print('Dividido en 4 sub matrices de 2X3:')
sub_arrays = np.split(array6, 4)  # matrices de 2X3
print(sub_arrays)


'''
7_Ordena el siguiente array de NumPy:
Caso 1: Ordenar el array por la segunda fila
Caso 2: Ordenar el array por la segunda columna
sampleArray = numpy.array([[34,43,73], [82,22,12], [53,94,66]])
'''

print('-----Ejercicio 7-----')
sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])
print(sampleArray)
caso1 = np.argsort(sampleArray[1, :])
caso1 = sampleArray[:, caso1]
print('Caso 1:')
print(caso1)

caso2 = np.argsort(sampleArray[:, 1])
caso2 = sampleArray[caso2, :]
print('Caso 2:')
print(caso2)


'''
8_Imprime el máximo del eje 0 y el mínimo del eje 1
de la siguiente matriz bidimensional:
sampleArray = numpy.array([[34,43,73],[82,22,12], [53,94,66]])
'''

print('-----Ejercicio 8-----')
sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])
maximo = sampleArray.max(axis=0)
print('Máximo del eje 0:')
print(maximo)

minimo = sampleArray.min(axis=1)
print('Mínimo del eje 1:')
print(minimo)


'''
9_Elimina la segunda columna de una matriz dada e
inserta la siguiente columna nueva en su lugar.
sampleArray = numpy.array([[34,43,73], [82,22,12],[53,94,66]])
newColumn = numpy.array([[10,10,10]])
'''

print('-----Ejercicio 9-----')
sampleArray = np.array([[34, 43, 73],
                        [82, 22, 12],
                        [53, 94, 66]])
newColumn = np.array([[10, 10, 10]])

print(sampleArray)
sampleArray = np.delete(sampleArray, 1, axis=1)
sampleArray = np.insert(sampleArray, 1, newColumn, axis=1)
print('Array con la columna nueva insertada:')
print(sampleArray)
