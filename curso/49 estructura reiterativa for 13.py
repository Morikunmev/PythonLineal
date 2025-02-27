def validar():
    while True:
        try:
            num = int(input("Ingrese 5 estudiantes del turno mañana: "))
            if num !=5:
                continue
            else:
                return num
        except ValueError:
            continue
def validar1():
    while True:
        try:
            num = int(input("Ingrese 6 estudiantes del turno tarde: "))
            if num !=6:
                continue
            else:
                return num
        except ValueError:
            continue
def validar2():
    while True:
        try:
            num = int(input("Ingrese 11 estudiantes del turno noche: "))
            if num != 11:
                continue
            else:
                return num
        except ValueError:
            continue
def edadf(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if 4<= num<=25:
                return num
        except ValueError:
            continue
def mayorf(promedio1, promedio2, promedio3):
    if promedio1 > promedio2 and promedio1 > promedio3:
        return "turno mañana"
    elif promedio2 > promedio1 and promedio2 > promedio3:
        return "turno tarde"
    else:
        return "turno noche"


mañana = validar()
tarde = validar1()
noche = validar2()
suma1 = 0
suma2 = 0
suma3 = 0

print("TURNO MAÑANA")
for i in range(mañana):
    edad = edadf(f"Ingrese la edad del estudiante {i+1}/ {mañana}: ")
    suma1 += edad
    promedio1 = suma1 / mañana
print("TURNO TARDE")
for j in range(tarde):
    edad = edadf(f"Ingrese la edad del estudiante {j+1}/ {tarde}: ")
    suma2 += edad
    promedio2 = suma2 / tarde
print("TURNO NOCHE")
for x in range(noche):
    edad = edadf(f"Ingrese la edad del estudiante {x+1}/ {noche}: ")
    suma3 += edad
    promedio3 = suma3 / noche

print(f"El promedio del turno mañana es: {round(promedio1,2)}")
print(f"El promedio del turno tarde es: {round(promedio2,2)}")
print(f"El promedio del turno noche es: {round(promedio3,2)}")
mayor = mayorf(promedio1, promedio2, promedio3)
print(f"El promedio mayor es el: {mayor}")
        
