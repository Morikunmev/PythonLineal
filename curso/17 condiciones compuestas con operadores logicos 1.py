#tres numeros enteros distintos y nos muestre el mayor

n1 = int(input("Ingrese: "))
n2 = int(input("Ingrese: "))
n3 = int(input("Ingrese: "))

if n1 > n2 and n1 > n3:
    print("El mayor es: " +str(n1))
else:
    if n2 > n1 and n2 > n3:
        print("El mayor es: " +str(n2))

    else:
        print("El mayor es: " +str(n3))
