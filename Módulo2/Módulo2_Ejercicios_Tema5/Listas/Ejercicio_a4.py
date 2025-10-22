'''
4. Haz un programa que lea n palabras, y que escriba
cada una invirtiendo la orden de sus caracteres.
Input:
hola
adios
hasta pronto
hasta luego
Output: ['aloh', 'soida', 'otnorp atsah', 'ogeul atsah']
'''
if __name__ == '__main__':
    lista = []
    n = int(input('Ingrese el largo de la lista: '))

    for i in range(n):
        lista.append(input('ingresa la frase: '))
    print(lista)

    cont = 0
    for x in lista:
        m = ''.join(reversed(x))
        lista[cont] = m
        cont += 1

    print(lista)
