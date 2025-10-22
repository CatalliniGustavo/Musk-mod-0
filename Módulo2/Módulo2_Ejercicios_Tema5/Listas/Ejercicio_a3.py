'''
3. Haz un programa que lea secuencias de enteros acabada en -1,
y que escriba cada una invirtiendo la orden de sus elementos.
Input: 3 -4 -5 6 -1
Output: [6, -5, -4, 3]
'''
if __name__ == '__main__':
    lista = []
    num = int(input('Ingresa un número a la lista: '))

    while True:  # para que la lista no esté vacía
        if num != -1:
            break
        else:
            num = int(input('Ingresa un número a la lista: '))

    while num != -1:
        lista.append(num)
        num = int(input('Ingresa un número a la lista: '))

    lista.reverse()
    print(lista)