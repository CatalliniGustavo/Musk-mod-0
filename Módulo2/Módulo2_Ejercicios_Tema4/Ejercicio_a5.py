'''
5. Haz un programa que indique si un año es bisiesto o no. Un año bisiesto tiene 366 días.
Después de la reforma gregoriana, los años bisiestos son los múltiplos de cuatro que no
acaban en dos ceros, y también los acabados en dos ceros tales que el número que queda
después de sacar los dos ceros finales es divisible por cuatro. Así, 1800 y 1900, a pesar
de ser múltiples de cuatro, no fueran bisiestos; en cambio, 2000 lo fue.
'''
if __name__ == '__main__':
    fecha = int(input("Ingresa un año: "))
    if fecha % 4 == 0:
        if fecha % 100 != 0 and fecha % 400 != 0:
            print("Bisiesto")
        else:
            print("no bisiesto")
    else:
        print("no bisiesto")
