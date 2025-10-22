'''
3. Haz un programa que obtenga sólo elementos únicos de dos conjuntos.
Input:
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Output: {70, 40, 10, 50, 20, 60, 30}
'''
if __name__ == '__main__':
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    union = set1.union(set2)
    print(union)
