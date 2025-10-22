'''
1. Haz un programa que añada una lista de elementos a un conjunto.
Input:
{"Yellow", "Orange", "Black"}
["Blue", "Green", "Red"]
Output: {'Black', 'Blue', 'Yellow', 'Green', 'Red', 'Orange'}
'''
if __name__ == '__main__':
    s = {"Yellow", "Orange", "Black"}
    lista = ["Blue", "Green", "Red"]

    print(s)
    s.update(lista)
    print(s)

    # for elemento in lista: #los agrega al final del set
    #   s.add(elemento)

    # print(s)
