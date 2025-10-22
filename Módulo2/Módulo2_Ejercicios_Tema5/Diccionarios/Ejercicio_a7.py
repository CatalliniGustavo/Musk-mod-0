'''
7. Haz un programa que compruebe si un valor existe en un diccionario.
Input:
{'a': 100, 'b': 200, 'c': 300}
200
Output: 200 presente en el diccionario
'''
if __name__ == '__main__':
    d = {'a': 100, 'b': 200, 'c': 300}
    valor = 200
    
    if valor in d.values():
        print('200 presente en el diccionario')
    else:
        print('200 no está presente en el diccionario')
        
