'''
7. Haz un programa que lea un real x≥0 y que escriba
⌊x⌋ (la parte entera inferior de x),
⌈x⌉ (la parte entera superior de x),
y el redondeo de x.
'''
if __name__ == '__main__':
    real = float(input('Ingrese un número real: '))
    inferior = int(real)
    superior = int(real) + 1
    redondeo = int(real + 0.5)
    print('Parte inferior: [{}]\nParte superior: [{}]\nRedondeo: [{}]'.format(inferior, superior, redondeo) )
