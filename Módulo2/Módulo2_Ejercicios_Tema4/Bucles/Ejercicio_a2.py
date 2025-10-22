'''
2. Haz un programa que lea una secuencia de 10 números y que escriba la media.
'''
if __name__ == '__main__':
    lista = []

    for i in range(10):
        lista.insert(i, int(input('Ingrese el {}° número: '.format(i + 1))))


    suma = sum(lista)/10
    print('El promedio es: {}'.format(suma))