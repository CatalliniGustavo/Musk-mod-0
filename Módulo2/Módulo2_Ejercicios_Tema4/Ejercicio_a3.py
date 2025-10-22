'''
3. Haz un programa que lea un entero que representa una temperatura en grados Celsius,
y que diga si hace calor, si hace frío, o si se está bien. Suponed que hace calor si
la temperatura es más alta que 30 grados, que hace frío si es más baja que 10 grados,
y que se está bien en otro caso.
Input: 25
Output: 'Se está bien'
'''
if __name__ == '__main__':
    celsius = int(input('Ingresa la temperatura: '))
    if celsius > 30:
        print('Hace calor')
    elif celsius < 10:
        print('Hace frio')
    else:
        print('Está bien')