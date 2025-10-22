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
if __name__ == '__main__':
    d = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    print(d) 
    
    d["location"] = d.pop("city")
    print(d) 