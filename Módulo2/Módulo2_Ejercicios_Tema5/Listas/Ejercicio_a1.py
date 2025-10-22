'''
1. Haz un programa que lea una lista dado su tamaño e imprima el segundo elemento (si existe).
'''
if __name__ == '__main__':
    num = int(input('Ingresa el tamaño de la lista: '))
    lista = []

    for i in range(num):
        elemento = input('Ingresa un elemento a la lista: ')
        lista.append(elemento)

    print(lista)
    if len(lista) > 1:
        print('el segundo elemento de la lista es {}'.format(lista[1]))
    else:
        print('no existe segundo elemento de la lista')