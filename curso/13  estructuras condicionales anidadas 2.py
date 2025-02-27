#Se cargan por teclado 3 numeros distintos. Mostrar por pantalla el mayor de ellos

n1 = int(input("Ingrese: "))
n2 = int(input("Ingrese: "))
n3 = int(input("Ingrese: "))
print("El valor mayor de los 3 valores ingresados es: ")
if n1 > n2:
    if n1 > n3:
        print(n1)
    else:
        print(n3)
else:
    if n2 >n3:
        print(n2)
    else:
        print(n3)
