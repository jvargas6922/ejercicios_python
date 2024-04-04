# SENTENCIA MATCH EN PYTHON
# hace la misma funcion que el switch en otros lenguajes.
# case _ es como el default en otros lenguajes.

numero = 5
match numero:
    case 1:
        print("El numero es 1")
    case 2:
        print("El numero es 2")
    case 3:
        print("El numero es 3")
    case _:
        print("El numero desconocido")


# 1) EJERCICIO VERFICAR SI EL NUMERO INGRESADO ES PAR O IMPAR
numero1 = int(input("Ingrese un numero: "))
match numero1 % 2:
    case 0:
        print("El numero es par")
    case _:
        print("El numero es impar")