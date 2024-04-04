#Ejemplo de funciones en python
#  funciona sumar dos numeros
# def suma(a, b):
#     result = a + b
#     return result

# dato = suma(2, 3)
# print(dato)

# value1 = int(input("Ingrese el primer valor: "))
# value2 = int(input("Ingrese el segundo valor: "))
# dato = suma(value1, value2)
# print(dato)

# Funcion para saber si un numero es par o impar
# def numero_par_impar(numero):
#     if numero % 2 == 0:
#         return "El numero es par"
#     else:
#         return "El numero es impar"
    
# dato1 = int(input("Ingrese un numero: "))
# print(numero_par_impar(dato1))

# funcion para saber el numero maximo en una lista de numeros
def max_number(numbers):
    max = 0
    for number in numbers:
        if number > max:
            max = number
    return max

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_number(numbers))
