# Diccionario anidados.(objetos anidados)
# primero se debe acceder al diccionario principal y luego al diccionario secundario.
# para acceder a un valor de un diccionario anidado se debe hacer de la siguiente manera:
# diccionario_principal["llave1"]["llave2"]
# ejemplo:
personas = {
    "persona1": {
        "nombre": "Juan",
        "apellido": "Perez",
        "edad": 25,
        "estatura": 1.75
    },
    "persona2": {
        "nombre": "Maria",
        "apellido": "Gomez",
        "edad": 30,
        "estatura": 1.60
    },
    "persona3": {
        "nombre": "Luis",
        "apellido": "Lopez",
        "edad": 20,
        "estatura": 1.80
    }
}

datos = personas["persona1"]
print(datos)
print(datos["nombre"])
datos2 = personas["persona2"]
print(datos2)
print(datos2["nombre"])

# tambien se pude declarar un diccionario vacio para que el usuario lo llene con los datos que desee.
# ejemplo:
persona = {
    "nombre": None,
    "apellido": None,
    "edad": None,
    "estatura": None
}

# solicitar al usuario que llene el diccionario
persona["nombre"] = input("Ingrese su nombre: ")
persona["apellido"] = input("Ingrese su apellido: ")
persona["edad"] = int(input("Ingrese su edad: "))
persona["estatura"] = float(input("Ingrese su estatura: "))
print(persona)
print("Mi nombre es " + persona["nombre"], + " mi apellido es " + persona["apellido"], + " tengo " + str(persona["edad"]) + " años y mido " + str(persona["estatura"]) + " metros.");