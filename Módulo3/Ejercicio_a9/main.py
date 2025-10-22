'''
9_Añade un atributo de clase llamado escuela a la
clase Estudiante y dale un valor predeterminado.
A continuación, añade un método de clase que
dado el nombre de otra escuela actualice el valor
de ese atributo. Llama a tu método en el
programa principal y asegúrate de que funciona.
'''
from Estudiante import Estudiante

if __name__ == '__main__':
    # Ejercicio 8
    notas = {"Matemática": 0, "Historia": 0, "Idioma": 0, "Química": 0, "Física": 0}
    estudiante = Estudiante("Gustavo", 41, 0, notas)


    def llenadoNotas(estudiante):
        for asignatura in estudiante.notas:
            nota = int(input(f"Ingrese la nota de {asignatura}: "))
            notas[asignatura] = nota

        return notas
    # estudiante.notas = llenadoNotas(estudiante)
    # estudiante.notasInferior(estudiante.notas)

    # Ejercicio 9
    print(f"Nombre anterior de escuela: {estudiante.escula}")
    escuela = input("Ingrese el nombre de la escuela: ")
    estudiante.nombreEsculea(escuela)
    print(f"Nuevo nombre de escuela: {estudiante.escula}")
