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
if __name__ == '__main__':
    d = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }
    print(d)
    
    d['emp3']['salary'] = 8500
    
    print(d)