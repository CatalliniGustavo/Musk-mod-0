'''
7. Haz un programa que diga si un natural n es capicua o no.
'''
if __name__ == '__main__':
    num = input('Ingrese un número: ')
    numpost = ''
    for i in range(len(num) -1 , -1, -1):
        numpost = numpost + num[i]

    print('{} {} '.format(num, numpost))
    if num == numpost:
        print('Es capicua!!!')
    else:
        print('No es capicua!!!')
