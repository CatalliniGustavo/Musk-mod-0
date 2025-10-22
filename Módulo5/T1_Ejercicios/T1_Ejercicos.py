'''
1_Escribe una función en python para leer el
contenido de un archivo de texto "poema.txt"
línea por línea y mostrar el mismo en pantalla.
'''

from datetime import datetime  # ejercicio 8
import os
from collections import Counter
import string


print('-----Ejercicio 1-----')


def leer_contenido(archivo):
    with open(f"T1_Ejercicios\\{archivo}.txt", encoding='utf-8') as f:
        for linea in f:
            # strip() para eliminar los salto de lineas
            print(linea.strip())


archivo = 'poema'
leer_contenido(archivo)


'''
2_Escribe una función para contar el número de
líneas de un archivo de texto "historia.txt":
Ejemplo: Si el archivo "story.txt" contiene las
siguientes líneas
Un niño está jugando allí.
Hay un parque infantil.
Un avión está en el cielo.
El cielo es rosa.
La contraseña puede contener letras y números.
El resultado debe ser 5.
'''

print('-----Ejercicio 2-----')


def contar_Lineas(archivo):
    with open(f"T1_Ejercicios\\{archivo}.txt", encoding='utf-8') as f:
        lineas = f.readlines()  # separa el texto en lineas
        contador = len(lineas)
        return contador


archivo = 'historia'
cantidad_Lineas = contar_Lineas(archivo)
print(f'En el archivo {archivo}.txt hay {cantidad_Lineas} lineas')


'''
3_Escribe una función en Python para contar y
mostrar el número total de palabras en un
archivo de texto.
'''

print('-----Ejercicio 3-----')


def contar_palabras(archivo):
    with open(f"T1_Ejercicios\\{archivo}.txt", encoding='utf-8') as f:
        contenido = f.read()
        palabras = contenido.split()
        n_palabras = len(palabras)
        return n_palabras


archivo = 'poema'
print(f'Hay {contar_palabras(archivo)} palabras en el archivo {archivo}.txt')


'''
4_Escriba una función en Python para leer líneas
de un archivo de texto "notas.txt". Su función
debe encontrar y mostrar la aparición de la
palabra "el".
'''

print('-----Ejercicio 4-----')


def contar_El():
    with open('T1_Ejercicios\\notas.txt', encoding='utf-8')as f:

        contenido = f.read()
        palabras = contenido.split()
        # marca donde se encuentra la palabra 'el'
        nuevo = contenido.replace(' el ', ' [EL] ')
        nuevo = nuevo.replace('El ', ' [EL] ')  # si empieza con mayúscula
        print(nuevo)
        el = palabras.count('el')
        el += palabras.count('El')
        return el


print(f'La palabra "el" se menciona {contar_El()} veces en el archivo')

'''
5_Escriba una función display_words() en python
para leer las lineas de un archivo de texto
"story.txt", y mostrar aquellas palabras que
tengan menos de 4 caracteres.
'''

print('-----Ejercicio 5-----')


def display_words():
    with open('T1_Ejercicios\\story.txt', encoding='utf-8') as f:
        contenido = f.read()
        palabras = contenido.split()
        lista_p = []
        for p in palabras:
            if len(p) < 4:
                lista_p.append(p)
    return lista_p


lista_p = display_words()
print(lista_p)


'''
6_Un archivo de texto llamado "materia.txt"
contiene algún texto, que necesita ser mostrado
de manera que cada carácter siguiente esté
separado por un símbolo "#". Escriba una
definición de función para hash_display() en
Python que muestre todo el contenido del
archivo matter.txt en el formato deseado.
Ejemplo : Si el archivo materia.txt tiene el
siguiente contenido almacenado :
EL MUNDO ES REDONDO
La función hash_display() debería mostrar el
siguiente contenido :
T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#
'''

print('-----Ejercicio 6-----')


def hash_display():
    with open('T1_Ejercicios\\materia.txt', encoding='utf-8') as f:
        contenido = f.read()
        resultado = '#'.join(contenido) + '#'
        print(resultado)


hash_display()


'''
7_Escribe un programa en Python para generar 26
archivos de texto llamados A.txt, B.txt, y así
sucesivamente hasta Z.txt.
'''

print('-----Ejercicio 7-----')
for l in string.ascii_uppercase:
    with open(f'T1_Ejercicios\\{l}.txt', 'w', encoding='utf-8') as f:
        f.write(f'Archivo {l}.txt')

'''
8_Escribe un programa en python para añadir
texto a un archivo y mostrar el texto en
python.txt
'''
print('-----Ejercicio 8-----')
with open('T1_Ejercicios\\python.txt', 'a', encoding='utf-8') as f:
    tiempo = datetime.now()
    # se agrega la fecha y hora para referencia
    f.write(f'// Texto agregado {tiempo}')
with open('T1_Ejercicios\\python.txt', encoding='utf-8') as f:
    contenido = f.read().strip()
    print(contenido)

'''
9_Escribe un programa en python para calcular la
frecuencia de todas las palabras de un archivo
txt.
'''

print('-----Ejercicio 9-----')

with open('T1_Ejercicios\\poema.txt', encoding='utf-8') as f:
    contenido = f.read().lower()  # carga el contenido con todas las palabras en minuscula
    palabras = contenido.split()  # se separa el contenido en palabras
    list_frecuencias = Counter(palabras)  # Cuenta las palabras
    print(list_frecuencias)


'''
10_Escribe un programa en python para comprobar
si un archivo especificado existe.
'''
print('-----Ejercicio 10-----')
nombre_archivo = input('Ingrfese el nombre del archivo con su extensión: ')
# se busca el archivo en esta carpeta
ruta = f'T1_ejercicios\\{nombre_archivo}'

if os.path.exists(ruta):
    print(f'El archivo "{nombre_archivo}" existe.')
else:
    print(f'El archivo "{nombre_archivo}" NO existe.')
