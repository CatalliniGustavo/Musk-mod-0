'''
10. Haz un programa que compruebe si todos los elementos de la tupla son iguales.
Input: (45, 45, 45, 45)
Output: 'Son todos los elementos iguales'
'''
if __name__ == '__main__':
    t1 = (45, 45, 45, 45)
    elemento = t1[0]
    for i in range(0, len(t1)):
        if elemento == t1[i]:
            igual = True
        else:
            igual = False
            
    if igual:
        print('Todo los elementos son iguales')
    else:
        print('No todo los elementos son iguales')
        