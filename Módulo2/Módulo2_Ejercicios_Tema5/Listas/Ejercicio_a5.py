'''
5. Haz un programa que lea una secuencia de números mientras sean positivos y que escriba la media.
Input: 4 10 5 12 -1
Output: 7.75
'''
import statistics

if __name__ == '__main__':
    num = int(input('Ingresa un numero: '))
    while True:
        if num >= 0:
            break
        else:
            num = int(input('Ingresa un numero: '))
    lista = []
    while num >= 0:
        lista.append(num)
        num = int(input('Ingresa un numero: '))

    promedio = statistics.mean(lista)
    print('El promedio de la lista es: {}'.format(promedio))