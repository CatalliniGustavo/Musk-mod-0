'''
6. Haz un programa que añada un segundo en una hora del día, dadas sus horas, minutos y segundos.
'''
if __name__ == '__main__':
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    #para que los datos ingresados estén dentro de los parámetros
    while 0 > horas or horas > 24:
        horas = int(input("Horas: "))
    while 0 > minutos or minutos > 59:
        minutos = int(input("Minutos: "))
    while 0 > segundos or segundos > 59:
        segundos = int(input("Segundos: "))

    segundos += 1
    if segundos > 59:
        segundos = 0
        minutos += 1
        if minutos > 59:
            minutos = 0
            horas += 1
            if horas >= 24:
                horas = 0
    print('Horas: {} , Minutos: {} , Segundos: {}'.format(horas, minutos, segundos))