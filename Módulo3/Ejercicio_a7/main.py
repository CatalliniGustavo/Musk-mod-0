'''
Añade un método público en la clase Estudiante
que calcule la media de una lista de notas y
actualice el valor del atributo grade. A
continuación Ilama a la función en tu programa
principal e imprime el valor de grade.
'''
from Estudiante import Estudiante

if __name__ == '__main__':
    estudiante = Estudiante("Gustavo", 41, 0)
    listaNotas = []


    def llenadoLista(listaNotas):
        for i in range(0, 5):
            nota = int(input("Ingrese la nota: "))
            listaNotas.append(nota)

        return listaNotas


    listaNotas = llenadoLista(listaNotas)
    estudiante.calcularMedia(listaNotas)
    print(estudiante.grade)

