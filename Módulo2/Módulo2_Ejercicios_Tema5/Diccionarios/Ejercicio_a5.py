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
if __name__ == '__main__':
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