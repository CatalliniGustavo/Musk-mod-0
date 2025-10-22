'''
7. Haz un programa que compruebe si dos conjuntos tienen algún elemento en común.
En caso afirmativo, mostrar los elementos comunes.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
Output: Tienen en común {10}
'''

if __name__ == '__main__':
    set1 = {10, 20, 30, 40, 50}
    set2 = {60, 70, 80, 90, 10}
    if set1.isdisjoint(set2):
        print("No tiene elementos comunes")
    else:
        print("Elementos comunes {}".format(set1.intersection(set2)))
