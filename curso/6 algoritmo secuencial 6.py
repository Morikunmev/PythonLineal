#Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora


horas_trabajadas = int(input("Ingrese horas trabajadas semanales: "))
valor_hora = int(input("Ingrese cuanto se le paga por hora: "))
sueldo = horas_trabajadas * valor_hora
print("El sueldo a pagar es: " + str(sueldo))
