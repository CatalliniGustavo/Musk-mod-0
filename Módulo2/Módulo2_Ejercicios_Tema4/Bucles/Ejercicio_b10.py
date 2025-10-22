'''
10. Haz un programa que cuente cuántos valores hay en una secuencia de enteros acabada en 0.
'''
if __name__ == '__main__':
    contador = 0
    numero = int(input('Ingresa un numero: '))
    # simula un do_while por si no se ingresa ningún valor
    while True:
        if numero == 0:
            break
        else:
            numero = int(input('Ingresa un numero: '))
            contador += 1

    print('La lista tiene {} valores'.format(contador))