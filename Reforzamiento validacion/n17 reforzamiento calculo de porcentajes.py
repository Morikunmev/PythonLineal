descuento1 = "0.04"
descuento1 = descuento1.split()
descuento1 = [float(i) for i in descuento1]
print(descuento1)


suma = "940.000"
suma = suma.replace(".","").split()
suma = [int(i) for i in suma]

final = suma[0] * (1- descuento1[0])
print(final)



