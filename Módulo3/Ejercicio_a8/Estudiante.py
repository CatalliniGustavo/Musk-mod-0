'''
Añade a la clase anterior, un método estático
que dada una lista de notas y sus asignaturas
asociadas como diccionario, imprima aquellas
asignaturas que han recibido una nota inferior 5.
'''
import statistics


class Estudiante:
    def __init__(self, nombre, edad, grade):
        self.nombre = nombre
        self.edad = edad
        self.grade = grade

    def calcularMedia(self, listaNotas: list):
        media = statistics.median(listaNotas)
        self.grade = media

    # Ejercicio 8: método estático
    # que dada una lista de notas y sus asignaturas
    # asociadas como diccionario, imprima aquellas
    # asignaturas que han recibido una nota inferior 5.
    @staticmethod
    def notasInferior(listaAsignaturas: list, listaNotas: list):
        diccionario = dict(zip(listaAsignaturas, listaNotas))
        for asignatura, nota in (diccionario.items()):
            if nota < 5:
                print(f"asignatura: {asignatura}, nota: {nota}")
