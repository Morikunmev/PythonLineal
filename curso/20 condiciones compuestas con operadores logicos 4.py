#Se ingresan por teclado 3 numeros, si todos los valores ingresados son menores a 10.
#imprimir en pantalla: "Todos los numeros son menores a diez"


def validar(n1,n2,n3):
    return n1 < 10 and n2 <10 and n3<10

n1, n2, n3 = int(input("Ingresa: ")), int(input("Ingresa: ")), int(input("Ingresa: "))
if validar(n1,n2,n3):
    print("Todos los valores son menores a 10")

