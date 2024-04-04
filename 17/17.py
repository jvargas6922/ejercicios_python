#Listas o arreglos de datos.

#Listas de numeros
numeros = [1,2,3,4,5,6,7,8,9,10]

#Listas de cadenas
nombres = ["Juan","Pedro","Maria","Ana","Luis"]

#Lista mixta
mixta = [1,2,3,"Juan","Pedro"]

print(numeros)
print(nombres)
print(mixta)

#Acceder a un elemento de la lista
print(nombres[0])
print(nombres[1])
print(nombres[2])

# para agregar elementos a la lista se usa el metodo (append)
nombres.append("Carlos");
print(nombres)

# para eliminar elementos de la lista se usa el metodo (del)
del nombres[2]
print(nombres)

for i in nombres:
    print(i)

# metodo suma de una lista sum()
suna = sum(numeros);
print(suna)
    
