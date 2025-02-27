#Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el numero es positivo.
#Negativo o nulo (es decir cero)

while True:
    numero = int(input("Ingresa: "))
    if numero == 0:
        print("Nulo")
    else:
        if numero>0:
            print("Positivo")
        else:
            print("Negativo")

    
