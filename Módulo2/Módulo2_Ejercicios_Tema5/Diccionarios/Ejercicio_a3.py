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
if __name__ == '__main__':
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
