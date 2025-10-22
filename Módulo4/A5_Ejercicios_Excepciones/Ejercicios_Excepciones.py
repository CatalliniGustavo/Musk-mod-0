'''
1_Crea una función que genere una excepción e
imprima su tipo, los argumentos de la excepción
y su mensaje de error.
'''

print('-----Ejercicio 1-----')


def metodo_Error():
    try:
        raise ValueError("Error")

    except Exception as e:
        print(f'Tipo: {type(e)}')
        print(f'Argumento: {e.args}')
        print(f'Mensaje: {str(e)}')


metodo_Error()

'''
2_Crea una función que compute la diferencia
entre dos enteros. En caso de que la diferencia
sea negativa genera una excepción inventada
por ti que informe sobre ello. Por ejemplo. la
excepción podría llamarse
NegativeDifferenceException.
'''
print('-----Ejercicio 2-----')


class NegativeDifferenceException(Exception):
    pass


def diferencia(num1, num2):
    try:
        print(f'La diferencia entre {num1} y {num2}')
        if num1 < num2:
            raise NegativeDifferenceException(
                'La diferencia da un número negativo como resultado')
        print(f'La diferencia es: {num1-num2}')
    except Exception as e:
        print(f'Tipo: {type(e)}')
        print(f'{e.args}')


diferencia(5, 3)
diferencia(5, 7)

'''
3_Crea una función que calcule la división entre
dos números. Debe imprimir el mensaje 'Los
parámetros deben ser número enteros' cuando
se genera una excepción de tipo y 'El divisor no
puede ser 0' cuando se genera un
zerodivisionerror.
'''
print('-----Ejercicio 3-----')


def division(num1, num2):
    try:
        print(f'La división entre {num1} y {num2}')
        if type(num1) != int or type(num2) != int:
            raise ValueError
        resultado = int(num1) / int(num2)
        print(f'El resultado: {resultado}')
    except ValueError:
        print('Los parámetros deben ser número enteros')
    except ZeroDivisionError:
        print('No se pude realizar la división por cero')
    finally:
        print('-----Ejercicio 4-----')
        print('Mensaje final')


division(10, 5)
division(10, 'b')
division(10, 3.5)
division(10, 0)

'''
4_Añade a la función anterior, un mensaje que se
imprima al final de la ejecución de la función
independientemente de si se ha generado
excepción o no.

'''