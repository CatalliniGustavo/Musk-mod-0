'''
1_Escribe un script en Python para mostrar los
distintos formatos de fecha y hora.
a) Fecha y hora actuales
b) Año actual
c) Mes del año
d) Número de la semana del año
e) Día de la semana
f) Día del año
g) Día del mes
h) Día de la semana
'''
from datetime import date, timedelta
import datetime

print('-----Ejercicio 1-----')
# a) Fecha y hora actuales
date1 = datetime.datetime.today()
print(f'Fecha y hora actuales: {date1}')
# b) Año actual
print(f'Año actual: {date1.year}')
# c) Mes del año
print(f'Mes del año: {date1.month}')
# Número de la semana del año
semana = date1.isocalendar().week
print(f'Número de la semana del año: {semana}')
# e) Día de la semana
diaSemana = date1.isocalendar().weekday
print(f'Día de la semana: {diaSemana}')
# f) Día del año
diaAño = date1.strftime('%j')
print(f'Día del año: {diaAño}')
# g) Día del mes
diaMes = date1.day
print(f'Día del mes: {diaMes}')
# h) Día de la semana
diastr = date1.strftime('%A')
print(f'Día de la semana: {diastr}')

'''
2_Escribe un programa en Python para convertir
una cadena a datetime.
INPUT: Jan 1 2014 2:43PM
OUTPUT: 2014-07-01 14:43:00
'''
print('-----Ejercicio 2-----')
fechastr = 'Jul 1 2014 2:43PM'
formato = '%b %d %Y %I:%M%p'
fechaConvertida = datetime.datetime.strptime(fechastr, formato)
print(f'Fecha String: {fechastr}')
print(f'Fecha Convertida: {fechaConvertida}')


'''
3_Escribe un programa en Python para obtener la
hora actual.
'''
print('-----Ejercicio 3-----')
fecha = datetime.datetime.now()
print(f'La hora actual: {fecha.hour}')

'''
4_Escribe un programa en Python para restar cinco
días a la fecha actual.
'''
print('-----Ejercicio 4-----')
fecha = datetime.datetime.now()
deltaT = datetime.timedelta(days=5)
fechaN = fecha - deltaT
print(f'Fecha actual: {fecha}')
print(f'5 dias anteriores: {fechaN}')

'''
5_Escribe un programa en Python para convertir
una cadena de marcas de tiempo unix en una
fecha legible.
INPUT Unix timestamp string: 1284105682
OUTPUT: 2010-09-10 13:31:22
'''
print('-----Ejercicio 5-----')
unixT = 1284105682
fecha = datetime.datetime.fromtimestamp(unixT)
print(fecha)

'''
6_Escribe un programa en Python para sumar 5
segundos con la hora actual
'''
print('-----Ejercicio 6-----')
fecha = datetime.datetime.now()
deltaT = datetime.timedelta(seconds=5)
fechaN = fecha + deltaT
print(fecha)
print(fechaN)

'''
7_Escribe un programa en Python para obtener el
número de la semana.
'''

print('-----Ejercicio 7-----')
date1 = datetime.datetime.today()
semana = date1.isocalendar().week
print(f'Número de la semana: {semana}')

'''
8_Escribe un programa en Python para seleccionar
todos los domingos de un año determinado.
'''
print('-----Ejercicio 8-----')

año = 2025  # Año que se va a evalur
domingos = []

fecha1 = date(año, 1, 1)  # Se comienza el 1 de enero

while fecha1.year == año:

    if fecha1.strftime('%A') == 'Sunday':
        domingos.append(fecha1)

    fecha1 += timedelta(days=1)


for domingo in domingos:
    print(f'Domingo {domingo}')

print(f'Hay {len(domingos)} domingos en el año {año}')

'''
9_Escribe un programa en Python para contar el
número de lunes del primer día del mes desde
2015 hasta 2016.
'''
print('-----Ejercicio 9-----')
año = 2025
lunes = []

fecha1 = date(año, 1, 1)  # Se comienza el 1 de enero

while fecha1.year == año:

    # Se busca los lunes que coincidan con el 1° del mes
    if fecha1.strftime('%A') == 'Monday' and fecha1.day == 1:
        lunes.append(fecha1)

    fecha1 += timedelta(days=1)


for lun in lunes:
    print(f'Lunes {lun}')

print(f'Hay {len(lunes)} Lunes primero del mes en el año {año}')


'''
10_Escribe un programa en Python para crear 12
fechas fijas a partir de una fecha especificada en
un periodo determinado. La diferencia entre dos
fechas será de 20.
'''

print('-----Ejercicio 10-----')
while True:
    try:
        fecha1 = input('Ingrese la fecha de inicio (dd-mm-aaaa): ')
        formato = '%d-%m-%Y'
        fechaConvertida = datetime.datetime.strptime(fecha1, formato)
        break
    except (ValueError):
        print('Error en el Formato dd-mm-aaaa')

# Toma solo la fecha y no la hora
fecha2 = datetime.date(fechaConvertida.year,
                       fechaConvertida.month, fechaConvertida.day)
fechas = [fecha2]

for i in range(11):
    # la fecha inicial más 11, con 20 dias de diferencia 
    fecha2 += datetime.timedelta(days=20)
    fechas.append(fecha2)

for f in fechas:
    print(f'{f.day}/{f.month}/{f.year}')
