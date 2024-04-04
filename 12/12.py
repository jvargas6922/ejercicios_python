# poder saber la longitud de una cadena de texto
# se utiliza la funcion len()
nombre = "Joffred"
apellido = "Vargas"
frase = "En la lucha por la locha"

logitud = len(nombre)
print(logitud)
print(len(apellido))
print(len(frase))

# poder extraer un caracter de una cadena de texto
# se utiliza la notacion de corchetes []
print(nombre[0])
print(apellido[0])
print(frase[0])

# para separar la cadena de texto
#se utiliza split()
palabra = frase.split()
print(palabra)

#para poder cambiar el texto a mayusculas
#se utiliza la funcion upper()
print(nombre.upper())
print(apellido.upper())
print(frase.upper())

#para poder cambiar el texto a minusculas
#se utiliza la funcion lower()
print(nombre.lower())
print(apellido.lower())
print(frase.lower())

# para poder remplazar una palabra por otra
# se utiliza la funcion replace()
print(frase.replace('lucha', 'plata'))
print(frase.replace('la', 'la plata'))


