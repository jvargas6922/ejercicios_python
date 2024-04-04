#Crear una tupla llamada palabras que contenga varias palabras, por ejemplo, "manzana", "banana" y "cereza".
#Solicitar al usuario que ingrese una palabra mediante la función input(). La palabra ingresada será almacenada en la variable palabra_buscar.
#Utilizar una estructura condicional (un if y un else) para verificar si palabra_buscar está presente en la tupla palabras.
#Si la palabra está en la tupla, imprimir "La palabra está en la tupla."
#Si la palabra no está en la tupla, imprimir "La palabra no está en la tupla."

palabras = ("manzana", "banana", "cereza")
palabra_buscar = input("Ingrese una palabra: ")
if palabra_buscar in palabras:
    print("La palabra está en la tupla.")
else:
    print("La palabra no está en la tupla.")
