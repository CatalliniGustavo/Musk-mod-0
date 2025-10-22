'''
8. Haz un programa que lea dos naturales a y b, con b > 0, y que escriba la división entera d y el residuo r de a 
entre b. Recordad que, por definición, d y r tienen que ser los únicos enteros tales que 0 ≤ r < b y d · b + r = a. 
Ejemplo: a=32, b=5, d=6, r=2 ya que 32 = 5 * 6 + 2
Input: 32 5
Output: dividendo: 32, divisor: 5, residuo: 2, cociente: 6
'''
if __name__ == '__main__':
    a = 32
    b = 5
    d = a // b
    r = a % b
    print("Dividendo: {}\nDivisor: {}\nResiduo: {}\nCociente: {}".format(a, b, r, d))
