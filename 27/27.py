# Clases en python
# Crear una clase llamada Persona que tenga los siguientes atributos: nombre, edad y lugar de residencia.
# Definir una función que muestre por pantalla los datos de la persona.
# Crear una clase llamada Empleado que herede de la clase Persona y añada un atributo sueldo y una función que muestre el sueldo.
# Crear un objeto de la clase Empleado, mostrar los datos de la persona y el sueldo por pantalla.
# atributo self definicion de la clase

class Persona:
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}, tengo {self.edad} años y vivo en {self.residencia}')

persona = Persona('Juan', 28, 'Bogotá')
persona.saludar()

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
residencia = input('Ingrese su residencia: ')

persona2 = Persona(nombre, edad, residencia);
persona2.saludar()
