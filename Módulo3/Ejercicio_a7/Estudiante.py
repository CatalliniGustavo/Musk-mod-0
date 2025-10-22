'''
Añade un método público en la clase Estudiante
que calcule la media de una lista de notas y
actualice el valor del atributo grade. A
continuación llama a la función en tu programa
principal e imprime el valor de grade.
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

