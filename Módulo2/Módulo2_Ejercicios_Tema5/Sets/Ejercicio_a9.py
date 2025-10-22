'''
9. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2,
excepto los elementos comunes.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output: {40, 50, 30}
'''
if __name__ == '__main__':
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.intersection_update(set2)
    print(set1)