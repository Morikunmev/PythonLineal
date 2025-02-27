#Escribir un programa que solicite por teclado 10 notas de alumnos
#y nos informe cuantos tienen notas mayores a 5 o iguales a 7
#y cuantos menores a 5
def validar(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num >0 and num==10:
                return num
            else:
                continue
        except ValueError:
            continue
        
def flotante(mensaje):
    while True:
        try:
            flot = float(input(mensaje))
            if 0.0<=flot<=7.0:
                return flot
            else:
                continue
        except ValueError:
            continue
def mayor(nota):
    if nota == 7.0 and nota >=5.0:
        return nota

al = validar("Ingrese nro 10: ")
contador = 0
contador1 = 0

for i in range(al):
    nota = flotante(f"Ingrese la nota {i+1}/{al}")
    if mayor(nota):
        contador +=1
    else:
        contador1 += 1

print(f"alumnos con notas mayores a 5 o iguales a 7 son: {contador} alumnos")
print(f"alumnos con nota menor a 5 son {contador1} alumnos")

    
