'''
8. Haz un programa que dada una secuencia de años acabada en 0 nos diga cuántos hay del siglo 20.
Input: 1950 1900 2000 1910 1800 0
Output: Existen 3 años que pertenecen al siglo XX
'''
if __name__ == '__main__':
    anio = int(input('Ingresa un año terminados en cero: '))

    contador = 0
    while anio != 0:
        anioaux = anio
        anio = anio // 100
        if anio + 1 == 20:
            contador += 1
            print(anioaux , ' Pertenece al siglo xx')
        anio = int(input('Ingresa un año terminados en cero: '))

    print('Existe {} años que pertenecen al siglo xx'.format(contador))
