'''
4. Haz un programa que, dados dos intervalos, calcule el intervalo correspondiente a la
intersección o indique que esta es vacía.
'''
if __name__ == '__main__':
    i1min = int(input('Introduce el minimo del 1° intervalo: '))
    i1max = int(input('Introduce el máximo del 1° intervalo: '))
    i2min = int(input('Introduce el minimo del 2° intervalo: '))
    i2max = int(input('Introduce el máximo del 2° intervalo: '))
    aux = i1max

    #odena los intervalos
    if i1max < i1min:
        i1max = i1min
        i1min = aux

    aux = i2max
    if i2max < i2min:
        i2max = i2min
        i2min = aux

    #determina el minimo y máximo de la intersección
    minimo = i1min
    if i1min < i2min:
        minimo = i2min
    maximo = i2max
    if i2max > i1max:
        maximo = i1max

    if minimo >= maximo:
        print('[{} , {}]'.format(minimo, maximo))
    else:
        print('[]')

