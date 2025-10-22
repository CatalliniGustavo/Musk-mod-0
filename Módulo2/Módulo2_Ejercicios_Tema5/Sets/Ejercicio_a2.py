'''
2. Haz un programa que devuelva un nuevo conjunto de elementos idénticos de dos conjuntos.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output: {40, 50, 30}
'''
if __name__ == '__main__':
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    union = set1.intersection(set2)
    print(union)
