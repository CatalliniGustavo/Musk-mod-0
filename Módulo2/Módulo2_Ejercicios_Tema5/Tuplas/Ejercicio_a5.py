'''
5. Haz un programa que intercambie dos tuplas en Python.
Input: 
t1 = (1, 2)
t2 = (3, 4)
Output:
t1 = (3, 4)
t2 = (1, 2)
'''
if __name__ == '__main__':
    tupla1 = (1, 2)
    tupla2 = (3, 4)
    print('Tupla 1 {} tupla 2 {}'.format(tupla1, tupla2))
    tupla1, tupla2 = tupla2, tupla1
    print('Tupla 1 {} tupla 2 {}'.format(tupla1, tupla2))
    
    