'''
9. Haz un programa que cuente el número de apariciones del elemento 50 de una tupla.
Input: (50, 10, 60, 70, 50)
Output: 2
'''
if __name__ == '__main__':
    t1 = (50, 10, 60, 70, 50)
    conteo = t1.count(50)

    print('El 50 aparece {} veces en la tupla'.format(conteo))
