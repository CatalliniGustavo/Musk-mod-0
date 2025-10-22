'''
1_Para resolver estos ejercicios debes usar el
fichero csvcompany_sales_data.csv.
Lee el beneficio total de todos los meses y
muéstralo mediante un gráfico de líneas. Se
proporcionan los datos del beneficio total de
cada mes. El gráfico de líneas generado debe
incluir las siguientes propiedades:
Nombre de la etiqueta X = Número de mes
Nombre de la etiqueta Y = Beneficio total 
'''

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

print('-----Ejercicio 1-----')
df = pd.read_csv('T4_Ejercicios\Modulo5_company_sales_data-221102-123259.csv')
x = np.array(df['month_number'])
y = np.array(df['total_profit'])

fig1 = plt.figure().canvas.manager.set_window_title('Ejercicio 1')
plt.plot(x, y)
plt.title("Beneficios por mes")
plt.xlabel("Número de mes")
plt.ylabel("Beneficio total")
plt.show()


'''
2_Obtenga el beneficio total de todos los meses y
muestre un gráfico de líneas con las siguientes
propiedades de estilo:
•Estilo de línea punteada y el color de la línea
debe ser rojo
•Mostrar la leyenda en la parte inferior derecha.
•Nombre de la etiqueta X = Número de mes
•Nombre de la etiqueta Y = Número de
•unidades vendidas
•Añadir un marcador de círculo.
•El ancho de la línea debe ser 3
'''

print('-----Ejercicio 2-----')
fig2 = plt.figure().canvas.manager.set_window_title('Ejercicio 2')
plt.plot(x, y, color='red', linestyle='--',
         linewidth=3, marker='o', mec='r', markerfacecolor='black', markersize=8)
plt.title("Beneficios por mes")
plt.xlabel("Número de mes")
plt.ylabel("Número de unidades vendidas")
plt.legend(['Profit data of last year'], loc='lower right')
plt.show()


'''
3_Lee todos los datos de ventas de productos y
mostrarlos mediante un gráfico multilínea.
Muestra el número de unidades vendidas por
mes para cada producto utilizando gráficos
multilínea. (es decir, una línea de trazado
separada para cada producto).
'''
print('-----Ejercicio 3-----')
fig3 = plt.figure().canvas.manager.set_window_title('Ejercicio 3')
x = np.array(df['month_number'])
facecream = df['facecream']
facewash = df['facewash']
toothpaste = df['toothpaste']
bathingsoap = df['bathingsoap']
shampoo = df['shampoo']
moisturizer = df['moisturizer']
plt.plot(x, facecream, color='blue', marker='o')
plt.plot(x, facewash, color='orange', marker='o')
plt.plot(x, toothpaste, color='green', marker='o')
plt.plot(x, bathingsoap, color='red', marker='o')
plt.plot(x, shampoo, color='purple', marker='o')
plt.plot(x, moisturizer, color='brown', marker='o')
plt.legend(['facecream', 'facewash', 'toothpaste', 'bathingsoap',
           'shampoo', 'moisturizer'], loc='upper left')
plt.title("Ventas")
plt.xlabel("Número de mes")
plt.ylabel("Unidades de ventas en número")
plt.show()


'''
4_Lee los datos de las ventas de pasta de dientes
de cada mes y muéstralos mediante un gráfico
de dispersión (scatter). Además, añade una
cuadrícula en el gráfico. El estilo de la cuadrícula
debe ser "-".
'''
print('-----Ejercicio 4-----')
fig4 = plt.figure().canvas.manager.set_window_title('Ejercicio 4')
plt.plot(x, toothpaste, 'o')
plt.grid(linestyle='-')
plt.legend(['Venta de pastas de dientes'], loc='upper left')
plt.title("Ventas pasta de dientes")
plt.xlabel('Número del mes')
plt.ylabel('Número de unidades vendidas')
plt.show()

'''
5_Lee los datos de ventas de los productos crema
facial y lavado de cara y muéstralos mediante el
gráfico barras. El gráfico de barras debe mostrar
el número de unidades vendidas por mes para
cada producto. Añade de una barra distinta para
cada producto en el mismo gráfico. 
'''

print('-----Ejercicio 5-----')
fig5 = plt.figure().canvas.manager.set_window_title('Ejercicio 5')
plt.bar(x - 0.1, facecream, width=0.2)
plt.bar(x + 0.1, facewash, color='orange', width=0.2)
plt.grid(linestyle='--')
plt.legend(['Ventas crema facial', 'Ventas lavado de cara'], loc='upper left')
plt.title('Facewash and facecream sale data')
plt.xlabel('Número del mes')
plt.ylabel('Unidades de ventas en número')
plt.show()


'''
6_Lee los datos de ventas de jabón de baño de
todos los meses y muéstralos mediante un
gráfico de barras.Guarda este gráfico en tu disco
duro.
'''

print('-----Ejercicio 6-----')
fig6 = plt.figure().canvas.manager.set_window_title('Ejercicio 6')
plt.bar(x, bathingsoap, width=0.9)
plt.grid(linestyle='--')
plt.title('Ventas jabon de baño')
plt.xlabel('Número del mes')
plt.ylabel('Unidades de ventas en número')
plt.savefig('T4_Ejercicios\Ejercicio_6.png')
plt.show()


'''
7_Lee el beneficio total de cada mes y muéstralo
utilizando el histograma para ver los rangos de
beneficio más comunes.
'''

print('-----Ejercicio 7-----')
fig7 = plt.figure().canvas.manager.set_window_title('Ejercicio 7')
y = np.array(df['total_profit'])
rangos = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
# 'y' ya es un array creado en el ejercicio 1 linea 21
plt.hist(y, bins=rangos)
plt.title('Profit')
plt.xlabel('profit en dolares')
plt.ylabel('Actual Profit en dolares')
plt.legend(['Profit'], loc='upper left')
plt.show()


'''
8_Calcula los datos de ventas totales del último
año para cada producto y muéstralos mediante
un gráfico circular.Nota: En el gráfico circular
muestra el número de unidades vendidas por año
para cada producto en porcentaje.
'''

print('-----Ejercicio 8-----')
# total de la suma de cada columna por producto
facecream = df['facecream'].sum()
facewash = df['facewash'].sum()
toothpaste = df['toothpaste'].sum()
bathingsoap = df['bathingsoap'].sum()
shampoo = df['shampoo'].sum()
moisturizer = df['moisturizer'].sum()
totales = np.array([facecream, facewash, toothpaste,
                   bathingsoap, shampoo, moisturizer])
mylabels = ['Crema facial', 'Lavado de cara', 'Pasta de dientes',
            'Gel de baño', 'Shampoo', 'Moisturizer']
fig8 = plt.figure().canvas.manager.set_window_title('Ejercicio 8')
plt.pie(totales, labels=mylabels, autopct='%.1f%%')
plt.legend(mylabels, loc='lower right')
plt.title('Sales data')
plt.show()


'''
9_Lee el jabón de baño de todos los meses y
visualízalo utilizando el Subplot.
'''

print('-----Ejercicio 9-----')
facewash = np.array(df['facewash'])
bathingsoap = np.array(df['bathingsoap'])
fig9 = plt.figure().canvas.manager.set_window_title('Ejercicio 9')
# Primer subplot
plt.subplot(2, 1, 1)
plt.plot(bathingsoap, color='black', marker='o')
plt.title('Ventas gel de baño')
# Segundo subplot
plt.subplot(2, 1, 2)
plt.plot(facewash, color='red', marker='o')
plt.title('Ventas gel de baño')
plt.xlabel('Número del mes')
plt.ylabel('Unidades de ventas en número')

plt.show()


'''
10_Lee todos los datos de las ventas de productos y
muéstrelos mediante el diagrama de pila.
'''

print('-----Ejercicio 10-----')

# Redefino los array
facecream = df['facecream']
facewash = df['facewash']
toothpaste = df['toothpaste']
bathingsoap = df['bathingsoap']
shampoo = df['shampoo']
moisturizer = df['moisturizer']

fig10 = plt.figure().canvas.manager.set_window_title('Ejercicio 10')
# colores según el gráfico de ejemplo
colores = ['purple', 'cyan', 'red', 'black', 'green', 'olive']
plt.stackplot(x, facecream, facewash, toothpaste,
              bathingsoap, shampoo, moisturizer, colors=colores)
plt.title('Todas las ventas de productos en un stack plot')
plt.xlabel('Número del mes')
plt.ylabel('Unidades de ventas en número')
# 'mylabels' del ejercicio 8
plt.legend(mylabels, loc='upper left')

plt.show()
