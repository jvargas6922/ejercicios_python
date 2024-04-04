# SENTENCIA BUCLE FOR
# for variable in elemento a recorrer:
# USO DEL FOR TENEMOS QUE TENER UNA LISTA DE ELEMENTOS EN EL CUAL EL FOR NOS PERMITE ITERAR CADA UNOS DE LOS ELEMENTOS DE LA LISTA.
#  break se utiliza para detener el bucle.
frutas = ["manzana", "pera", "mango"]
contador = 0

for fruta in frutas:
    contador += 1
    print(f"fruta # {contador}: {fruta}")
    if fruta == "pera":
        break

# 1) ejercicio 1
numeros  = [1,2,3,20,4,5]
for numero in numeros:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")

# 2) ejercicio 2

# Requerimientos del ejercicio
#Crea una lista llamada numeros que contenga al menos cinco números enteros.
#Inicializa una variable llamada suma en 0.
#Utiliza un ciclo for para iterar a través de la lista numeros y suma cada número a la variable suma.
#Después del ciclo for, divide la variable suma entre la cantidad de números en la lista (que puedes obtener usando la función len(numeros)).
#Imprime el resultado como el promedio de los números en la lista.
notas = [10, 8, 9, 7, 10]
suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)
print(f"El promedio de las notas es {promedio}")


    