"""
Escribe un programa en Python que realice operaciones matemáticas simples (suma, resta, multiplicación y división) utilizando una función. El programa debe permitir al usuario ingresar dos números y seleccionar una operación para realizar.
"""

def calculadora(a, b, operacion):
    if(operacion == '+'):
        return suma(a, b)
    if(operacion == '-'):
        return resta(a, b)
    if(operacion == '*'):
        return  multiplicacion(a, b)
    if(operacion == '/'):
        return division(a, b)
            
def suma(a, b):
    result = a + b
    return result

def resta(a, b):
    result = a - b
    return result

def multiplicacion(a, b):
    result = a * b
    return result

def division(a, b):
    result = a / b
    return result

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
operacion = input("Ingrese la operacion que desea realizar (+, -, *, /): ")
print(f"El resultado de la operacion ({operacion}) es: {calculadora(num1, num2, operacion)}")