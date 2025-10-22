'''
6. Haz un programa que devuelva un conjunto de elementos presentes en el conjunto A o B, pero no en ambos.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output: {20, 70, 10, 60}
'''
if __name__ == '__main__':
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.symmetric_difference_update(set2)
    print(set1)