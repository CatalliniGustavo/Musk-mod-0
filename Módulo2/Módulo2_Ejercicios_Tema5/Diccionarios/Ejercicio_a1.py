'''
1. Haz un programa que convierta dos listas en un diccionario.
['a', 'b', 'c']
[1, 2, 3]
Output: {'a': 1, 'b': 2, 'c': 3}
'''
if __name__ == '__main__':
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