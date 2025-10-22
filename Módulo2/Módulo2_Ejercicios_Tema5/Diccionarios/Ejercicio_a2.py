'''
2. Haz un programa que fusione dos diccionarios de Python en uno solo.
Input:
dict1 = {'diez': 10, 'veinte': 20, 'treinta': 30}
dict2 = {'treinta': 30, 'cuarenta': 40, 'cincuenta': 50}
Output: {'diez': 10, 'veinte': 20, 'treinta': 30, 'cuarenta': 40, 'cincuenta': 50}
'''
if __name__ == '__main__':
    dict1 = {'diez': 10, 'veinte': 20, 'treinta': 30}
    dict2 = {'treinta': 30, 'cuarenta': 40, 'cincuenta': 50}
    dict1.update(dict2)
    print(dict1)

'''
# Alternativa

dict3 = {**dict1, **dict2}
print(dict3)
'''