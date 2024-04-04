# EJEMPLO DE CONDICIONALES ANIDADAS
# Programa que evalua la nota de un alumno
nota = float(raw_input("Ingresa tu nota en una escala del 1 al 100:"))

if nota >= 90:
    print("Felicidades has aprobado con una calificacion sobresaliente")
elif nota >= 70:
    print("Has aprobado satifactoriamente")
elif nota >= 60 and nota < 70:
    print("Has aprobado, pero necesitas mejorar")
else:
    print("Lo siento, has supendido. Debes esforzarte mas en la proxima evaluacion")