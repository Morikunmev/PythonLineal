#Se ingresa por teclado un numero positivo de uno o dos digitos (1..99)
#Mostrar un mensaje indicando si el numero tiene uno o dos digitos

while True:
    valor = int(input("Ingrese un valor comprendido entre 1 y 99: "))
    if valor>= 10 and valor <= 99:
        print("Tiene 2 digitos")
    elif valor <10:
        print("Tiene 1 digito")
    else:
        print("Tiene mas de dos digitos")
