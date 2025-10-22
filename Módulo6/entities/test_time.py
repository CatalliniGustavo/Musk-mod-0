'''2_Escribe un programa en Python para convertir
una cadena a datetime.
INPUT: Jan 1 2014 2:43PM
OUTPUT: 2014-07-01 14:43:00
'''
import datetime


print('-----Ejercicio 2-----')
fechastr = 'Jul 1 2014 2:43PM'
formato = '%b %d %Y %I:%M%p'
fechaConvertida = datetime.datetime.strptime(fechastr, formato)
print(f'Fecha String: {fechastr}')
print(f'Fecha Convertida: {fechaConvertida}')