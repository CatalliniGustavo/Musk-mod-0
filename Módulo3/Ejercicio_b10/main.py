'''
10_Añade un método privado en la clase anterior,
que dado un diccionario mes-número de
asistencias, devuelva 1 si algún mes tiene una
asistencia < 4, devuelva 2 si algún mes tiene
alguna asistencia entre [4, 8) o bien devuelva 3
en caso contrario. Para probar el método
privado, encapsúlalo con una función pública
que devuelva su resultado.
'''
from Estudiante import Estudiante

if __name__ == '__main__':
    # Ejercicio 8
    notas = {"Matemática": 0, "Historia": 0, "Idioma": 0, "Química": 0, "Física": 0}
    # Ejercicio 10
    asistencias = {"Enero": 0, "Febrero": 0, "Marzo": 0, "Abril": 0,
                  "Mayo": 0, "Junio": 0, "Julio": 0,"Agosto":0,
                  "Septiembre": 0, "Octubre": 0, "Noviembre": 0,"Diciembre": 0}
    estudiante = Estudiante("Gustavo", 41, 0, notas, asistencias)


    def llenadoNotas(estudiante):
        for asignatura in estudiante.notas:
            nota = int(input(f"Ingrese la nota de {asignatura}: "))
            notas[asignatura] = nota

        return notas

    # Ejercicio 10
    def llenadoAsistencia(estudiante):
        for mes in estudiante.asistencias:
            asist = int(input(f"Ingrese la asistencia del mes de {mes}: "))
            asistencias[mes] = asist
        return asistencias
    # estudiante.notas = llenadoNotas(estudiante)
    # estudiante.notasInferior(estudiante.notas)

    # Ejercicio 9
    # print(f"Nombre anterior de escuela: {estudiante.escula}")
    # escuela = input("Ingrese el nombre de la escuela: ")
    # estudiante.nombreEsculea(escuela)
    # print(f"Nuevo nombre de escuela: {estudiante.escula}")

    # Ejercicio 10
    estudiante.asistencias = llenadoAsistencia(estudiante)
    asis = estudiante.asistenciasInferior(estudiante.asistencias)
    print(asis)
    if asis == 1:
        print("Hay almenos un mes con menos de 4 asistencias")
    elif asis == 2:
        print("Hay almenos un mes entre 4 y menos de 8 asistencias")
    else:
        print("En todo los meses hay más de 8 asistencias")