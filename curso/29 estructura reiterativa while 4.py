x = 1
cantidad = 0
n = int(input("Ingrese cuantas piezas va a procesar: "))
while x<=n:
    largo = float(input("Ingrese la medida de la pieza: "))
    if largo>= 1.20 and largo<=1.30:
        cantidad = cantidad +1
    x+=1

print("Cantidad de piezas aptas")
print(cantidad)
