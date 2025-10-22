'''
10. Haz un programa que dada una temperatura en grados Celsius la muestre en grados Fahrenheit y en grados Kelvin. 
(F= 1.8C + 32 y  ºK =°C + 273ºK).
Input: 40
Output:    
    "Temperatura en Celsius: 40",
    "Temperatura en Fahrenheit: 104.0",
    "Temperatura en Kelvin: 313",
'''
if __name__ == '__main__':
    c = 40
    f = 1.8 * c + 32
    k = c + 273
    print('Temperatura en Celcius: {}\nTemperatura en Fahrenheit: {}\nTemperatura en Kelvin: {}'.format(c, f, k))
