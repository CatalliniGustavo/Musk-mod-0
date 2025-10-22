'''
17. Haz un programa que lea varias descripciones de rectángulos y de círculos,
y que para cada una escriba el área correspondiente. La entrada empieza con un
número n, seguido de n descripciones. Si es de un rectángulo, se tiene la
palabra “rectángulo” seguida de dos reales estrictamente positivos que indican
la longitud y la anchura. Si es de un círculo, se tiene la palabra “círculo”
seguida de un real estrictamente positivo que indica el radio.
Input:
Introduce la longitud de la secuencia: 2
Introduce el nombre del polígono: rectangulo
Introduce la longitud del rectángulo: 10
Introduce la anchura del rectángulo: 5
El rectangulo tiene area 50.0
Introduce el nombre del polígono: circulo
Introduce el radio del círculo: 4
El circulo tiene area 50.26548245743669
'''
import math

if __name__ == '__main__':
    num = int(input('Introduce la longitud de la secuencia: '))
    '''
 for i in range(num):
     opc = input('Introduce el nombre del polígono: ')
     match opc:
         case 'rectangulo':
             longrec = int(input('Introduce la longitud del rectángulo: '))
             anchrec = int(input('Introduce la anchura del rectángulo: '))
             print('El rectángulo tiene un area de {}'.format(longrec * anchrec))
         case 'circulo':
             radio = float(input('Introduce el radio del círculo: '))
             print('El círculo tiene un area de {}'.format(math.pi * pow(radio, 2)))
         case _:
             i -= 1
             print('La opción no existe {}'.format(i))
    '''  # opción usando la función match

    for i in range(0, num):
        opc = input('Introduce el nombre del polígono: ')
        if opc.lower() == 'rectangulo':
            longrec = int(input('Introduce la longitud del rectángulo: '))
            anchrec = int(input('Introduce la anchura del rectángulo: '))
            print('El rectángulo tiene un area de {}'.format(longrec * anchrec))
        elif opc.lower() == 'circulo':
            radio = float(input('Introduce el radio del círculo: '))
            print('El círculo tiene un area de {}'.format(math.pi * pow(radio, 2)))
        else:
            i -= 1  # Descuenta una opción fallida
            print('La opción no existe')
