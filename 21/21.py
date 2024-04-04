"""
1- Crea un diccionario llamado datos_personales con las siguientes claves: "nombre", "edad", "direccion" y "telefono". Inicializa todos los valores a None.
2- Solicita al usuario que ingrese su nombre, edad, dirección y número de teléfono y almacena cada valor en el diccionario datos_personales.
3- Muestra en pantalla los datos ingresados por el usuario utilizando las claves del diccionario.
"""

datos_personales = {
    "nombre": None,
    "edad": None,
    "direccion": None,
    "telefono": None
}

datos_personales["nombre"] = input("Ingrese su nombre: ")
datos_personales["edad"] = int(input("Ingrese su edad: "))
datos_personales["direccion"] = input("Ingrese su dirección: ")
datos_personales["telefono"] = input("Ingrese su número de teléfono: ")

print(datos_personales)
print("Datos personales:")
print(f"Nombre: {datos_personales['nombre']}")
print(f"Edad: {datos_personales['edad']}")
print(f"Dirección: {datos_personales['direccion']}")
print(f"Teléfono: {datos_personales['telefono']}")