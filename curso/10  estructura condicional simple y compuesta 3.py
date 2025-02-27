#Se ingresan 3 notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"

nota1 = int(input("Ingresa la nota 1: "))
nota2 = int(input("Ingresa la nota 2: "))
nota3 = int(input("Ingresa la nota 3: "))
promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 7:
    print("Promocionado")
else:
    print("No promocionado")

