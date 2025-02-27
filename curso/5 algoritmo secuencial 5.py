#Realizar un programa que lea cuatro valores numeros e informar su suma y promedio

n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa otro numero: "))
n3 = int(input("Ingresa otro numero: "))
n4 = int(input("Ingresa otro numero: "))

sumatotal = n1 + n2 + n3 + n4
promedio = sumatotal / 4

print("La suma total de los cuatro numeros ingresados es: {}".format(sumatotal))
print("El promedio de los cuatro numeros es: {}".format(promedio))
