#Realizar un programa que pida cargar una fecha, verificar si dicha fecha corresponde a Navidad

def validacion(dia):
    return 1 <= dia <=31
def validacion1(mes):
    return 1 <= mes <= 12

while True:
    dia = int(input("Ingrese un dia entre 1 y 31: "))
    mes = int(input("Ingrese un mes entre 1 y 12: "))

    if validacion(dia) and validacion1(mes):
        break
    else:
        print("Fecha invalida. Intente nuevamente.")

año = int(input("Ingrese año: "))

print("Fecha Ingresada: {}-{}-{}".format(dia, mes, año))


