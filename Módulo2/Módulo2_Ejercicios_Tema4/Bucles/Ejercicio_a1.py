'''
1. Haz un programa que lea dos números a y b, y que escriba todos los números enteros a y b.
Debe cumplirse que a < b. En caso que a > b, escribe los número de manera descendente.
'''
if __name__ == '__main__':
    num1 = int(input('Ingresa el 1° numero: '))
    num2 = int(input('Ingresa el 2° numero: '))

    if num1 < num2:
        for num in range(num1, num2 + 1):
            print('[{}] '.format(num),end="")
    else:
        for num in range(num1, num2 - 1, -1):
            print('[{}] '.format(num),end="")
