'''
8_Añade a la clase anterior, un método estático
que dada una lista de notas y sus asignaturas
asociadas como diccionario, imprima aquellas
asignaturas que han recibido una nota inferior 5.
'''
from Estudiante import Estudiante

if __name__ == '__main__':
    # Ejercicio 8
    asignaturas = ["Matemática", "Historia", "Idioma", "Química", "Física"]
    notas = []
    estudiante = Estudiante("Gustavo", 41, 0)


    def llenadoNotas(asignaturas: list):
        for i in range(0, len(asignaturas)):
            nota = int(input(f"Ingrese la nota de {asignaturas[i]}: "))
            notas.append(nota)

        return notas


    notas = llenadoNotas(asignaturas)
    estudiante.notasInferior(asignaturas, notas)
