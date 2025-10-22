'''
4. Haz un programa que cree una función con un argumento por defecto.
Crea una función show_employee() usando las siguientes condiciones.
-Debe aceptar el nombre y el salario del empleado y mostrar ambos.
-Si falta el salario en la llamada de función, asigne el valor predeterminado 9000 al salario.
Input:
showEmployee("Ben", 12000)
showEmployee("Jessa")
Output:
Name: Ben salary: 12000
Name: Jessa salary: 9000
'''


def show_employee(employee, salary=9000):
    print(f'{employee}: {salary}')


if __name__ == '__main__':
    show_employee("Ben", 12000)
    show_employee("Jessa")
