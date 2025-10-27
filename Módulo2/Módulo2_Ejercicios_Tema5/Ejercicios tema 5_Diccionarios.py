'''
1. Haz un programa que convierta dos listas en un diccionario.
['a', 'b', 'c']
[1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}
'''
print('-----Ejercicio 1-----')
lista1 = ['a', 'b', 'c']
lista2 = [1, 2, 3]
diccionario = dict(zip(lista1, lista2))
print(diccionario)
    
''' Solución alternativa:
d = {}
for i in range(0, len(l1)):
    d[l1[i]] = l2[i]
print(d)
    '''
    
'''
2. Haz un programa que fusione dos diccionarios de Python en uno solo.
Input:
dict1 = {'diez': 10, 'veinte': 20, 'treinta': 30}
dict2 = {'treinta': 30, 'cuarenta': 40, 'cincuenta': 50}
Output: {'diez': 10, 'veinte': 20, 'treinta': 30, 'cuarenta': 40, 'cincuenta': 50}
'''
print('-----Ejercicio 2-----')
dict1 = {'diez': 10, 'veinte': 20, 'treinta': 30}
dict2 = {'treinta': 30, 'cuarenta': 40, 'cincuenta': 50}
dict1.update(dict2)
print(dict1)

'''
# Alternativa
dict3 = {**dict1, **dict2}
print(dict3)
'''

'''
3. Haz un programa que imprima el valor de la clave 'history' del siguiente diccionario.
{
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}    
Output: 80
'''
print('-----Ejercicio 3-----')
d = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(d["class"]["student"]["marks"]["history"])


'''
4. Haz un programa que inicialice el diccionario con valores por defecto.
Input:
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Output: {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
'''
print('-----Ejercicio 4-----')
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
d = dict.fromkeys(employees, defaults)
print(d)


'''
5. Haz un programa que cree un diccionario extrayendo las claves de un diccionario dado.
Input:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
Output: {'name': 'Kelly', 'salary': 8000}
'''
print('-----Ejercicio 5-----')
d = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]
    
d2 = dict()
    
for k in keys:
    d2.update({k : d[k]})
print(d2)


'''
6. Haz un programa que elimine una lista de claves de un diccionario.
Input:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
# Keys a eliminar
keys = ["name", "salary"]
Output: {'age': 25, 'city': 'New york'}
'''
print('-----Ejercicio 6-----')
d = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]
    
for k in keys:
    d.pop(k)
print(d)


'''
7. Haz un programa que compruebe si un valor existe en un diccionario.
Input:
{'a': 100, 'b': 200, 'c': 300}
200
Output: 200 presente en el diccionario
'''
print('-----Ejercicio 7-----')
d = {'a': 100, 'b': 200, 'c': 300}
valor = 200
    
if valor in d.values():
    print('200 presente en el diccionario')
else:
    print('200 no está presente en el diccionario')
        

'''
8. Haz un programa que cambie el nombre de la clave de un diccionario.
Input:
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Output: {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
'''
print('-----Ejercicio 8-----')
d = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
print(d) 
    
d["location"] = d.pop("city")
print(d) 

'''
9. Haz un programa que obtenga la clave de un valor mínimo del siguiente diccionario.
Input:
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
Output: Math 
'''
print('-----Ejercicio 9-----')
d = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
mini = min(d.values())
    
print('El valor minimo es: {}'.format(mini))
    
print(min(d, key=d.get))


'''
10. Haz un programa que cambie el valor de una clave en un diccionario anidado.
Input:
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
Output:
{
   'emp1': {'name': 'Jhon', 'salary': 7500},
   'emp2': {'name': 'Emma', 'salary': 8000},
   'emp3': {'name': 'Brad', 'salary': 8500}
}
'''
print('-----Ejercicio 10-----')
d = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
print(d)
    
d['emp3']['salary'] = 8500
    
print(d)