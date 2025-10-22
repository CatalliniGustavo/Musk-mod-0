'''
9. Haz un programa que almacene en una lista los números del 1 al 10
y los muestre por pantalla en orden inverso separados por comas.
'''
if __name__ == '__main__':
    lista = list(range(1, 11))

    for i in range(len(lista), 0, -1):
        if i == 1:
            print('{}'.format(lista[0]))
        else:
            print('{}, '.format(lista[i-1]), end='')