'''
3. Haz un programa que dada una lista de naturales de tamaño n, indique la posición del primer número par.
'''
if __name__ == '__main__':

    largo = int(input('Ingrese la longitud de la lista: '))
    lista = list(range(largo))

    for i in range(largo):
        lista.insert(i, int(input('Ingrese el {}° número: '.format(i + 1))))
        if lista[i] % 2 == 0:
            print(lista[i], ' en la posición: {}'.format(i))
            break #finaliza cuando se ingresa el primer valor par de la lista