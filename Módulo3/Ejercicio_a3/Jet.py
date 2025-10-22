'''
Añade otro atributo llamado "cantidad" a la clase.
El usuario le dará valor pasando un nuevo
parámetro por el constructor. A continuación,
crear 2 instancias para: F14 y Mirage2000 con
las cantidades 87 у 35.
'''
class Jet:
    def __init__(self, name, country, cantidad ):
        self.name = name
        self.origin = country
        self.cantidad = cantidad
