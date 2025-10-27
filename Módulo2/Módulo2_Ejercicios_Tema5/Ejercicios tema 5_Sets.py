'''
1. Haz un programa que añada una lista de elementos a un conjunto.
Input:
{"Yellow", "Orange", "Black"}
["Blue", "Green", "Red"]
Output: {'Black', 'Blue', 'Yellow', 'Green', 'Red', 'Orange'}
'''
print('-----Ejercicio 1-----')

s = {"Yellow", "Orange", "Black"}
lista = ["Blue", "Green", "Red"]

print(s)
s.update(lista)
print(s)

# for elemento in lista: #los agrega al final del set
#   s.add(elemento)

# print(s)


'''
2. Haz un programa que devuelva un nuevo conjunto de elementos idénticos de dos conjuntos.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output: {40, 50, 30}
'''
print('-----Ejercicio 2-----')

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
union = set1.intersection(set2)
print(union)

'''
3. Haz un programa que obtenga sólo elementos únicos de dos conjuntos.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output: {70, 40, 10, 50, 20, 60, 30}
'''
print('-----Ejercicio 3-----')

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
union = set1.union(set2)
print(union)


'''
4. Haz un programa que actualice el primer conjunto con elementos que no existen en el segundo conjunto.
Input:
set1 = {10, 20, 30}
set2 = {20, 40, 50}
Output: set1 {10, 30}
'''
print('-----Ejercicio 4-----')

set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)


'''
5. Haz un programa que elimine elementos del conjunto a la vez.
Input: set1 = {10, 20, 30, 40, 50}
Output: {40, 50}
'''
print('-----Ejercicio 5-----')

set1 = {10, 20, 30, 40, 50}
set1.remove(10)
set1.remove(20)
set1.remove(30)
# set1.difference_update({10, 20, 30}) # solución alternativa
print(set1)


'''
6. Haz un programa que devuelva un conjunto de elementos presentes en el conjunto A o B, pero no en ambos.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output: {20, 70, 10, 60}
'''
print('-----Ejercicio 6-----')

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)


'''
7. Haz un programa que compruebe si dos conjuntos tienen algún elemento en común.
En caso afirmativo, mostrar los elementos comunes.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
Output: Tienen en común {10}
'''

print('-----Ejercicio 7-----')

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
    print("No tiene elementos comunes")
else:
    print("Elementos comunes {}".format(set1.intersection(set2)))


'''
8. Haz un programa que actualice el conjunto1 añadiendo
elementos del conjunto2, excepto los elementos comunes.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output: {70, 10, 20, 60}
'''
print('-----Ejercicio 8-----')

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)


'''
9. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2,
excepto los elementos comunes.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output: {40, 50, 30}
'''
print('-----Ejercicio 9-----')

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)