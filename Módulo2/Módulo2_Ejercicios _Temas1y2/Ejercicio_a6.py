'''
6. Hacer un programa que dado un valor calcule su cuadrado y el cubo.
Input: 10
Output: 100 1000
'''
if __name__ == '__main__':
    num1 = 10
    cuadrado = pow(num1, 2)
    cubo = pow(num1, 3)
    print("El cuadrado es: {} \nEl cubo es: {}".format(cuadrado, cubo))
