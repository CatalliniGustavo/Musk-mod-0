'''
8. Ordena una tupla de tuplas por el 2º elemento.
Input: t1 = (('a', 23),('b', 37),('c', 11), ('d',29))
Output: t1 =(('c', 11), ('a', 23), ('d', 29), ('b', 37))
'''
if __name__ == '__main__':
    t1 = (('a', 23),('b', 37),('c', 11), ('d',29))
    t2 = sorted(t1, key=lambda x: x[1])
    
    print(t1)
    print(t2)
    