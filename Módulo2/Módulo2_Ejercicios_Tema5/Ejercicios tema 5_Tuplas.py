'''
1. Haz una programa que invierta una tupla.
'''
print('-----Ejercicio 1-----')
tupla = (10, 20, 30, 40, 50)
print(tupla)
tupla = tupla[::-1]
print(tupla)


'''
2. Haz un programa que acceda al valor 15 de la tupla.
Input: ("Naranja", [10, 20, 30], (5, 15, 25))
Output: 15
'''
print('-----Ejercicio 2-----')
tupla = ("Naranja", [10, 20, 30], (5, 15, 25))
print(tupla[2][1])


'''
3. Haz un programa que declare una tupla con un solo elemento 10.
'''
print('-----Ejercicio 3-----')
tupla = (10)
print(tupla)


'''
4. Haz un programa que descomponga la tupla en 4 variables.
Input:  (10, 20, 30, 40)
Output:
10
20
30
40
'''

print('-----Ejercicio 4-----')
tupla = (10, 20, 30, 40)

a, b, c, d = tupla

print(a)
print(b)
print(c)
print(d)

'''
5. Haz un programa que intercambie dos tuplas en Python.
Input: 
t1 = (1, 2)
t2 = (3, 4)
Output:
t1 = (3, 4)
t2 = (1, 2)
'''
print('-----Ejercicio 5-----')
tupla1 = (1, 2)
tupla2 = (3, 4)
print('Tupla 1 {} tupla 2 {}'.format(tupla1, tupla2))
tupla1, tupla2 = tupla2, tupla1
print('Tupla 1 {} tupla 2 {}'.format(tupla1, tupla2))

'''
6. Haz un programa que copie elementos específicos de una tupla a una nueva tupla.
Input: t1 = (11, 22, 33, 44, 55, 66)
Output: t2: (44, 55)
'''
print('-----Ejercicio 6-----')
t1 = (11, 22, 33, 44, 55, 66)

t2 = t1[3:5]
print(t2)


'''
7. Haz un programa que modifique una tupla.
Input: t1 = (11, [22, 33], 44, 55)
Output: t1: (11, [222, 33], 44, 55)
'''
print('-----Ejercicio 7-----')
t1 = (11, [22, 33], 44, 55)

t1[1][0] = 222
print(t1)

'''
8. Ordena una tupla de tuplas por el 2º elemento.
Input: t1 = (('a', 23),('b', 37),('c', 11), ('d',29))
Output: t1 =(('c', 11), ('a', 23), ('d', 29), ('b', 37))
'''
print('-----Ejercicio 8-----')
t1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
t2 = sorted(t1, key=lambda x: x[1])

print(t1)
print(t2)


'''
9. Haz un programa que cuente el número de apariciones del elemento 50 de una tupla.
Input: (50, 10, 60, 70, 50)
Output: 2
'''
print('-----Ejercicio 9-----')
t1 = (50, 10, 60, 70, 50)
conteo = t1.count(50)

print('El 50 aparece {} veces en la tupla'.format(conteo))


'''
10. Haz un programa que compruebe si todos los elementos de la tupla son iguales.
Input: (45, 45, 45, 45)
Output: 'Son todos los elementos iguales'
'''
print('-----Ejercicio 10-----')
t1 = (45, 45, 45, 45)
elemento = t1[0]
for i in range(0, len(t1)):
    if elemento == t1[i]:
        igual = True
    else:
        igual = False

if igual:
    print('Todo los elementos son iguales')
else:
    print('No todo los elementos son iguales')
