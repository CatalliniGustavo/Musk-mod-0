'''
9. Haz un programa que reciba una secuencia de naturales de tamaño n
y nos devuelva cuál es el primer natural que tiene un valor inferior al primer natural leído.
'''
if __name__ == '__main__':
    largo = int(input('Ingrese el largo de la lista de números: '))
    lista = [] * largo
    nreferencia = 0
    # llenado de la lista y toma el número de referencia
    for i in range(largo):
        if i == 0:
            nreferencia = int(input('Ingrese el {}° número: '.format(i + 1)))
            lista.insert(i, nreferencia)
        else:
            lista.insert(i, int(input('Ingrese el {}° número: '.format(i + 1))))

    # Busca el menor si hay
    haymenor = False
    nmenor = nreferencia
    for i in lista:
        if i < nreferencia:
            nmenor = i
            haymenor = True
            break

    for i in lista:
        print(i, end=' ')

    print('')

    if haymenor:
        print('El primer meno a "{}" es el "{}"'.format(nreferencia, nmenor))
    else:
        print('No se ha encontrado ningún valor menor.')
