'''
Dadas las siguientes clases con el output de sus
respectivos métodos, crea una interfaz formal
que las implemente.
Módulo 5
svm = SVM()
svm.preprocess data(data=None, y=None)
svm.fit()
svm.predict()
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()
output:
Preprocessing data at SVM
Training at SVM
Evaluating at SVM
Preprocessing data at DecisionTree
Training at DecisionTree
Evaluating at DecisionTree
'''


from abc import ABCMeta
from abc import abstractmethod

print('-----Ejercicio 1-----')


class SVM:
    @abstractmethod
    def preprocess_data(self, data, y):
        print('Preprocessing data at SMV')

    @abstractmethod
    def fit(self):
        print('Training at SMV')

    @abstractmethod
    def predict(self):
        print('Evaluating at SVM')


class DecisionTree(SVM):

    def preprocess_data(self, data, y):
        print('Preprocessing data at DecisionTree')

    def fit(self):
        print('Training at DecisionTree')

    def predict(self):
        print('Evaluating at DecisionTree')


svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()

'''
2_Repite el ejercicio anterior esta vez creando una
interfaz informal.
'''


class SVM:

    def preprocess_data(self, data, y):
        print('Preprocessing data at SMV')

    def fit(self):
        print('Training at SMV')

    def predict(self):
        print('Evaluating at SVM')


class DecisionTree(SVM):

    def preprocess_data(self, data, y):
        print('Preprocessing data at DecisionTree')

    def fit(self):
        print('Training at DecisionTree')

    def predict(self):
        print('Evaluating at DecisionTree')


print('-----Ejercicio 2-----')

svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()

'''
3_Crea una clase virtual llamada Algoritmo con los
atributos nombre, tarea y aprendizaje que sea
superclase de la clase BaseClassifier del
problema anterior. Comprueba con el método
issubclass que Algoritmo es padre de
BaseClassifier.
'''


class Algoritmo(metaclass=ABCMeta):

    def __init__(self, nombre, tarea, aprendizaje):
        self.nombre = nombre
        self.tarea = tarea
        self.aprendizaje = aprendizaje


class BaseClassifier(object):

    def __init__(self):
        pass


print('-----Ejercicio 3-----')
Algoritmo.register(BaseClassifier)
print(issubclass(BaseClassifier, Algoritmo))
