'''
7. Haz un programa que modifique una tupla.
Input: t1 = (11, [22, 33], 44, 55)
Output: t1: (11, [222, 33], 44, 55)
'''
if __name__ == '__main__':
    t1 = (11, [22, 33], 44, 55)
    
    t1[1][0] = 222
    print(t1)