# ejercicio para poder utilizar el modulo de math.

# logica se le pide al usuario ingresar un numero entero y poder hacer la siguientes comparaciones: Rango1 = numero negativo(0), Rango2 numeros entre 0 hasta 10 , Rango3 = numeros mayores a 10

numero = int(input("Ingrese un numero: "))
match numero:
    case numero if numero < 0: 
        print(f"El numero {numero} esta en el rango 1")
    case numero if numero <= 0 and numero < 10:
        print(f"El numero {numero} esta en el rango 2")
    case numero if numero >= 10: 
        print(f"El numero {numero} esta en el rango 3")
    case _:
        print(f"El numero {numero} no esta en ningun rango")