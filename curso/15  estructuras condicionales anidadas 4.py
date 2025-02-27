#Programa que permita cargar un numero entero positivo de hasta 3 cifras y
#muestre un mensaje indicando si tiene 1, 2 o 3 cifras.
#Mostrar un mensaje de error si el numero de cifras es mayor

while True:
    numero = int(input("Ingresa: "))

    if numero > 0:
        if numero <10:
            print("Tiene 1 cifra")
        else:
            if numero <= 99:
                print("Tiene 2 cifras")
            else:
                if numero <= 999:
                    print("Tiene 3 cifras")
                else:
                    print("Error")
    else:
        print("Es negativo")
    
