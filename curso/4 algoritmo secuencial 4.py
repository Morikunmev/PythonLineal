#Escribir un programa en el cual se ingresen cuatro numeros,
#calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))
num4 = int(input("Ingresa el cuarto numero: "))

suma = num1 + num2
producto = num3 * num4

print("La suma de " +str(num1) + " y " + str(num2) + " es " + str(suma))
print("El prodcuto de " +str(num3) + " y " + str(num4) + " es " +str(producto))

