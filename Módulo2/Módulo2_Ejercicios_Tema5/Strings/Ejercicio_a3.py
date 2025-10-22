'''
3. Haz un programa que invierta una cadena dada.
Input: hola y adios
Output: soida y aloh
'''
if __name__ == '__main__':
    frase = input('Ingresa una frase: ')
    # con un bucle
    for i in range(len(frase)-1, -1 , -1):
        print(frase[i],end='')
    print('')
    # otras opciones
    reversa = frase[::-1]
    print(reversa)
    reversa = ''
    reversa = ''.join(reversed(reversa))
    print(frase[::-1])