##def validacion(bucle):
##    while bucle:
##        nombre = input("Ingresa un caracter: ")
##        return nombre
##def contador(nombre):
##    return nombre.count(" ")
##
##bucle = True
##
##while bucle:
##    nombre = validacion(bucle)
##    contar = contador(nombre):
##    print(f"Se ingresaron {contar} espacios en blanco")
##    

bucle = True
while bucle:
    acumulador = 0
    caracter = input("Ingresa: ")
    for i in range(len(caracter)):
        if caracter[i] == " ":
            acumulador+= 1

    print(acumulador)
