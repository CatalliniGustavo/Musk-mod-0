'''
9_Añade un atributo de clase llamado escuela a la
clase Estudiante y dale un valor predeterminado.
A continuación, añade un método de clase que
dado el nombre de otra escuela actualice el valor
de ese atributo. Llama a tu método en el
programa principal y asegúrate de que funciona.
'''
import statistics


class Estudiante:
    escula = "Escuela Musk"

    def __init__(self, nombre, edad, grade, notas):
        self.nombre = nombre
        self.edad = edad
        self.grade = grade
        self.notas = notas

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