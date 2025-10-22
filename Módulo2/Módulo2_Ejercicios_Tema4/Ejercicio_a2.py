'''
2. Haz un programa que lea una letra y que indique por pantalla si es una mayúscula, si es una minúscula,
si es una vocal, y si es una consonante.
'''
if __name__ == '__main__':
    letra = input('Ingrese una letra: ')
    l = letra[0]

    if l.islower():
        print('{} es minúscula'.format(l))
    else:
        print('{} es mayúscula'.format(l))
    if l.lower() in ['a', 'e', 'i', 'o', 'u']:
        print('{} es vocal'.format(l))
    else:
        print('{} es consonante'.format(l))