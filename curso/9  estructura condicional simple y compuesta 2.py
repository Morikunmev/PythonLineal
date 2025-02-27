#Solicitar dos numeros, si el primero es mayor al segundo informar su suma y diferencia.
#Caso contrario informar el producto y la division del primero respecto al segundo

num1 = int(input("Ingresa: "))
num2 = int(input("Ingresa: "))
print("El mayor es: ")
if num1 > num2:
    print(num1)
    suma = num1 + num2
    diferencia = num1 - num2
    print("La suma es: {}".format(suma))
    print("La diferencia es: {}".format(diferencia))
else:
    print(num2)
    producto = num1 * num2
    division = num1 / num2
    print("El producto es: {}".format(producto))
    print("La division es: {}".format(round(division,2)))

