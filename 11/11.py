# Sentencia While
# contador = 1
# while contador <= 10:
#     print(contador)
#     contador += 1
#     if contador == 5:
#         break

# Ejercicio 1
# crear una programa que haga un conteo y luego diga feliz año nuevo.
# contador = 10
# while contador >= 1:
#     print(contador)
#     contador -= 1

# print("Feliz año nuevo")

# Ejercicio 2
# suma = 0
# numero = int(input("Ingrese un número positivo (o un numero negativo para salir): "))
# while numero >= 0:
#     suma += numero
#     numero = int(input("Ingrese un número positivo (o un numero negativo para salir): "))

# print("La suma de los números ingresados es: ", suma)

# Ejercicio 3
#Solicita al usuario que ingrese un número entero positivo como límite para el conteo.
#Inicializa una variable llamada contador en 1.
#Utiliza un bucle while para realizar el conteo desde 1 hasta el número límite ingresado por el usuario.
#En cada iteración del bucle, muestra el valor actual de contador en la pantalla.
#Después de imprimir el número actual, incrementa el valor de contador en 1 para pasar al siguiente número.
#Cuando el valor de contador alcance o supere el número límite ingresado por el usuario, el bucle while debe detenerse.
#Imprime "Conteo completado" para indicar que el conteo ha terminado.

numeroUsuario = int(input("Ingrese un número entero positivo: "))
contador = 1
while contador <= numeroUsuario:
    print(contador)
    contador += 1
print("Conteo completado")