'''
6. Haz un programa que copie elementos específicos de una tupla a una nueva tupla.
Input: t1 = (11, 22, 33, 44, 55, 66)
Output: t2: (44, 55)
'''
if __name__ == '__main__':
    t1 = (11, 22, 33, 44, 55, 66)
    
    t2 = t1[3:5]
    print(t2)    