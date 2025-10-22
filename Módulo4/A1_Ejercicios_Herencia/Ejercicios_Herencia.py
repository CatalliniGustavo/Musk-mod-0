'''
1_Crea una clase Staff con los atributos role, depty
salary. Crea una clase Profesor que herede de la
clase anterior y que además tenga como
atributos nombre y edad. Haz que sea posible
instanciar un profesor dándole valor a todos los
atributos.
'''


class Staff:
    def __init__(self, role, depty, salary):
        self.role = role
        self.depty = depty
        self.salary = salary

    def __str__(self):
        return f"Role: {self.role}, Depty: {self.depty}, Salary: ${self.salary}, "

# Crea una clase Profesor que herede de la
# clase anterior y que además tenga como
# atributos nombre y edad.


class Profesor(Staff):
    def __init__(self, role, depty, salary, nombre, edad):
        super().__init__(role, depty, salary)
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return super().__str__() + f"Nombre: {self.nombre}, Edad: {self.edad} años"


# Haz que sea posible
# instanciar un profesor dándole valor a todos los
# atributos.
print('-----Ejercicio 1-----')
profesor = Profesor("Enseñar", "Profesores", 3000, "Jorge", 35)
print(profesor)


'''
2_Representa el siguiente diagrama con sus clases,
atributos y métodos correspondientes.
Cada método display debe imprimir el nombre de
la clase, atributos y valores de la instancia en ese
momento. Ejemplo: IndisplaymethodofParent1x=10
'''


class Parent1:
    def __init__(self, x):
        self.x = x

    def display(self):
        print(f"In display metho do Parent1 x= {self.x}")


class Parent2:
    def __init__(self, y):
        self.y = y

    def display(self):
        print(f"In display metho do Parent2 y= {self.y}")


class Child(Parent1, Parent2):
    def __init__(self, x, y, z):
        Parent1.__init__(self, x)
        Parent2.__init__(self, y)
        self.z = z

    def display(self):
        print(f"In Display metho do child z= {self.z}")


# Cada método display debe imprimir el nombre de
# la clase, atributos y valores de la instancia en ese
# momento. Ejemplo: IndisplaymethodofParent1x=10

print('-----Ejercicio 2-----')
x = Parent1(10)
y = Parent2(15)
z = Child(10, 20, 30)
x.display()
y.display()
z.display()


'''
3_Crea una clase Car que herede de Vehicle y que
sobreescriba los métodos max_speed() y
change_gear(). Instancia dos objetos de cada
clase y compruebaque la salida de cada método
es distinta
'''


class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details: ', self.name, self.color, self.price)

    def max_speed(self):
        print(f'{self.name} max speed is 150')

    def change_gear(self):
        print(f'{self.name} change 6 gear')

# Crea una clase Car que herede de Vehicle


class Car(Vehicle):
    def __init__(self, name, color, price):
        super().__init__(name, color, price)

    def max_speed(self):
        print(f'{self.name} max speed is 200')

    def change_gear(self):
        print(f'{self.name} change 5 gear')

print('-----Ejercicio 3-----')
# Instancia dos objetos de cada
# clase y comprueba que la salida de cada método
# es distinta
vehicle1 = Vehicle('Ford', 'Blanco', 10000)
vehicle2 = Vehicle('Renault', 'Rojo', 20000)
car1 = Car('Toyota', 'Azul', 30000)
car2 = Car('Honda', 'Negro', 30000)
vehicle1.max_speed()
vehicle1.change_gear()
vehicle2.max_speed()
vehicle2.change_gear()
car1.max_speed()
car1.change_gear()
car2.max_speed()
car2.change_gear()
