'''
5. Haz un programa que elimine elementos del conjunto a la vez.
Input: set1 = {10, 20, 30, 40, 50}
Output: {40, 50}
'''
if __name__ == '__main__':
    set1 = {10, 20, 30, 40, 50}
    set1.remove(10)
    set1.remove(20)
    set1.remove(30)
    # set1.difference_update({10, 20, 30}) # solución alternativa
    print(set1)
