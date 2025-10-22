'''
4. Haz un programa que inicialice el diccionario con valores por defecto.
Input:
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
Output: {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
'''
if __name__ == '__main__':
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    d = dict.fromkeys(employees, defaults)
    print(d)
