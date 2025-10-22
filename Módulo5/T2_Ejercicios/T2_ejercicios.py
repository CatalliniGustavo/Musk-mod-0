'''
1_Para realizar los ejercicios usar el archivo
csvAutomobile_data.csv.
A partir del conjunto de datos dado, imprime las
cinco primeras y últimas filas.
'''

import pandas as pd

print('-----Ejercicio 1-----')
df = pd.read_csv('T2_Ejercicios\\Modulo5_Automobile_data-221102-123259.csv')
print(df.head())
print(df.tail())

'''
Limpia el conjunto de datos y actualiza el archivo
CSV. Reemplaza todos los valores de las
columnas que contengan ?, n.a, o NaN.
'''
print('-----Ejercicio 2-----')
df = pd.DataFrame(df)
pd.set_option('display.max_rows', None)
# Elimina las filas duplicadas
print('-----Filas Duplicadas-----')
filas_duplicadas = df.duplicated()
print(df[filas_duplicadas])
# Reemplaza '?' y 'n.a' por NaN
df.replace(['?', 'n.a'], pd.NA, inplace=True)
df.drop_duplicates(inplace=True)
# Rellena los valores NaN
df.fillna(11111.0, inplace=True)
# Data limpia sin datos NaN o duplicados
print(df)
df.to_csv('T2_Ejercicios\\Modulo5_Automobile_data_limpio.csv', index=False)


'''
3_Encuentra el nombre de la empresa del coche
más caro. Imprime el nombre de la empresa del
coche más caro y su precio.
'''
print('-----Ejercicio 3-----')
precio = df.loc[df['price'] == df['price'].max()]
print(
    f'Empresa: {precio['company'].values[0]} Precio: {precio['price'].values[0]}')


'''
4_Imprime todos los datos de los coches Toyota.
'''
print('-----Ejercicio 4-----')
toyota = df.loc[df['company'] == 'toyota']
print(toyota)

'''
5_Cuenta el total de coches por empresa.
'''
print('-----Ejercicio 5-----')
modelos = df['company'].value_counts()
print(modelos)

'''
6_Encuentra el coche con el precio más alto de
precio de cada empresa.
'''
print('-----Ejercicio 6-----')
valores_maximos = df.loc[df.groupby('company')['price'].idxmax()]
print(valores_maximos)

'''
7_Encuentra el kilometraje medio de cada empresa
fabricante de automóviles.
'''
print('-----Ejercicio 7-----')
promedio = df.groupby('company')['average-mileage'].mean()
print(promedio)

'''
8_Ordena todos los coches por la columna Precio.
'''

print('-----Ejercicio 8-----')
print(df.sort_values(by=['price'], ascending=False))

'''
9_Concatena dos dataframes utilizando las
siguientes condiciones:
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}
'''
print('-----Ejercicio 9-----')
germanCars = {'Company': ['Ford', 'Mercedes', 'BMV',
                          'Audi'], 'Price': [23845, 171995, 135925, 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan',
                            'Mitsubishi'], 'Price': [29995, 23600, 61500, 58900]}
df1 = pd.DataFrame(germanCars)
df2 = pd.DataFrame(japaneseCars)
df_concatenados = pd.concat([df1, df2], axis=0)  # vertical
print(df_concatenados)

'''
10_Combina dos dataframe utilizando la siguiente
condición. Crea dos dataframe utilizando los
siguientes dos Dicts, fusiónalos y añade el
segundo dataframe como una nueva columna al
primer dataframe.
car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_Horsepower = {*Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}
'''
print('-----Ejercicio 10-----')
car_Price = {'Company': ['Toyota', 'Honda', 'BMV',
                         'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda',
                              'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}

df3 = pd.DataFrame(car_Price)
df4 = pd.DataFrame(car_Horsepower)
df_union = df3.merge(df4, on='Company', how='inner')
print(df_union)

