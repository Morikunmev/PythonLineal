#Realizar la carga del precio de un producto y la cantidad a llevar.
#Mostrar cuanto se debe pagar ( se ingresa un valor entero en el precio del producto y la cantidad

precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad a pagar: "))

importe = precio * cantidad

print("Debe pagar: " + str(importe))
