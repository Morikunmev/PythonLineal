##nota1 = int(input("Ingrese la nota 1: "))
##nota2 = int(input("Ingrese la nota 2: "))
##nota3 = int(input("Ingrese la nota 3: "))
##
##promedio = (nota1 + nota2 + nota3) / 3
##
##if promedio >= 7:
##    print("Promocionado")
##elif promedio >= 4 and promedio <7:
##    print("Regular")
##else:
##    print("Reprobado")
##


#OTRA FORMA DE HACER EL EJERCICIO

nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
nota3 = int(input("Ingrese la nota 3: "))

promedio = (nota1 + nota2 + nota3) /3
if promedio >= 7:
    print("Promocionado")
else:
    if promedio >=4:
        print("Regular")

    else:
        print("Reprobado")
