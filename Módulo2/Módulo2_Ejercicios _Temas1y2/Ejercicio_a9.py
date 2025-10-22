'''
9. Haz un programa que, dada una cantidad de segundos, diga cuántas horas, minutos y segundos representa.
Input: 3600
Output: 3600 segundos son 60.0 minutos y 1.0 horas
'''
if __name__ == '__main__':
    segundos = 3600
    minutos = segundos / 60
    horas = segundos / 3600
    print('{} segundos son {} minutos y {} horas'.format(segundos, minutos, horas))
