'''
2. Haz un programa que lea una secuencia no vacía de enteros acabada en -1,
y que escriba cuántos son iguales al último.
Input: 3 4 -2 3 -7 3 -1
Output: Existen 2 elementos iguales al último elemento
'''
if __name__ == '__main__':
    lista = []
    num = int(input('Ingresa un número a la lista: '))

    while True:# para que la lista no esté vacía
        if num != -1:
            break
        else:
            num = int(input('Ingresa un número a la lista: '))

    while num != -1:
        lista.append(num)
        num = int(input('Ingresa un número a la lista: '))

    print(lista)
    contador = -1
    for num in lista:
        if num == lista[len(lista)-1]:
            contador += 1
    if contador >= 1:
        print('{} se repite {} veces'.format(lista[len(lista)-1], contador))