'''
12. Haz un programa que añada un nuevo elemento 60
a la lista [10, 50, 40, 20, 30] después de un
elemento especificado por el usuario. Si el elemento
introducido no está presente en la lista debe mostrar el mensaje:
'Elemento no presente en la lista'.
'''
if __name__ == '__main__':
    lista = [10, 50, 40, 20, 30]
    num = int(input('Ingresa un numero: '))

    lista2 = []
    if num in lista:
        for i in range(0,5):
            if lista[i] == num:
                lista2.append(lista[i])
                lista2.append(60)
            else:
                lista2.append(lista[i])
        print(lista2)
    else:
        print('Elemento no está presente en la lista')

