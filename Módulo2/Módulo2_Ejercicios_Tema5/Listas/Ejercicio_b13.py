'''
13. Haz un programa que elimine todas las apariciones
de un elemento específico introducido por el usuario
de la lista [10, 50, 40, 20, 60, 30].
'''
if __name__ == '__main__':
    lista = [10, 50, 40, 20, 60, 30]
    num = int(input('Ingresa un numero que quiera eliminar de la lista: '))
    if num in lista:
        while num in lista:
            lista.remove(num)
        print(lista)
    else:
        print('Elemento no está presente en la lista')

