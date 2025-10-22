'''
4. Haz un programa que actualice el primer conjunto con elementos que no existen en el segundo conjunto.
Input:
set1 = {10, 20, 30}
set2 = {20, 40, 50}
Output: set1 {10, 30}
'''
if __name__ == '__main__':
    set1 = {10, 20, 30}
    set2 = {20, 40, 50}
    set1.difference_update(set2)
    print(set1)
