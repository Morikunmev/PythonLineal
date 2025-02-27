#Ingresar el sueldo de una perona, si supera los 3000 dolares mostrar un mensaje
#en pantalla indicando que debe abonar impuestos

sueldo = int(input("Ingrese el sueldo: "))

if sueldo > 3000:
    print("Esta persona debe pagar impuestos: ")
else:
    print("No debe pagar impuestos")
