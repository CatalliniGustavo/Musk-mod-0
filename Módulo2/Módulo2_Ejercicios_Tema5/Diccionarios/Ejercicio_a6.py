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
if __name__ == '__main__':
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