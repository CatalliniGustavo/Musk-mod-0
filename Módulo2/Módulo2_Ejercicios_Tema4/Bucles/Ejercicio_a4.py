'''
4. Haz un programa que lea un número n y que escriba la “tabla de multiplicar” de n.
'''
if __name__ == '__main__':
    num = int(input('Ingrese un número: '))
    for i in range(11):
        print('{} x {} = {}'.format(num, i, num * i))