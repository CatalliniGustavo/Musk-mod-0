'''
3_Añade otro atributo llamado "cantidad" a la clase.
El usuario le dará valor pasando un nuevo
parámetro por el constructor. A continuación,
crear 2 instancias para: F14 y Mirage2000 con
las cantidades 87 у 35.
'''
from Jet import Jet

if __name__ == '__main__':
    jet1 = Jet("F16", "USA", 0)
    cantidad = int(input(f"Ingrese cantidad de '{jet1.name}': "))
    jet1.cantidad = cantidad

    jet2 = Jet("F14", "USA", 87)
    jet3 = Jet("Mirage2000", "France", 35)
