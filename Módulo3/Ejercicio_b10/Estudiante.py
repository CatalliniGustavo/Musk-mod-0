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
import statistics


class Estudiante:
    escula = "Escuela Musk"

    def __init__(self, nombre, edad, grade, notas, asistencias):
        self.nombre = nombre
        self.edad = edad
        self.grade = grade
        self.notas = notas
        self.asistencias = asistencias

    # Ejercicio 7
    def calcularMedia(self, listaNotas: list):
        media = statistics.median(listaNotas)
        self.grade = media

    # Ejercicio 8
    @staticmethod
    def notasInferior(diccionario: dict):
        for asignatura, nota in diccionario.items():
            if nota < 5:
                print(f"asignatura: {asignatura}, nota: {nota}")

    # Ejercicio 9
    @classmethod
    def nombreEsculea(cls, nombre):
        cls.escula = nombre

    # Ejercicio 10
    '''
    devuelva 1 si algún mes tiene una
    asistencia < 4, devuelva 2 si algún mes tiene
    alguna asistencia entre [4, 8) o bien devuelva 3
    en caso contrario.
    '''
    def __asistencia(self, asistencias: dict):
        if min(asistencias.values()) < 4:
            return 1
        elif min(asistencias.values()) >= 4 and min(asistencias.values()) < 8:
            return 2
        else:
            return 3

    def asistenciasInferior(self, diccionario: dict):
        return self.__asistencia(diccionario)
