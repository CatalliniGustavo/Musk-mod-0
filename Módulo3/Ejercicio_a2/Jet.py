'''
Usando la clase Jet, crea nuevas instancias con
los siguientes nombres y orígenes:
SU33: Russia
AJS37: Sweden
Mirage2000: France
F14: USA
Mig29: USSR
A10: USA
'''

class Jet:
    def __init__(self, name, country):
        self.name = name
        self.origin = country

