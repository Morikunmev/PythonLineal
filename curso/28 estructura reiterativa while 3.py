#Permita la carga de 10 valores por teclado y nos muestre la suma
#de los valores ingresados y su promedio
def validar():
    while True:
        try:
            valor = int(input("Ingrese un valor: "))
            return valor
        except ValueError:
            print("Ingrese un valor numerico valido.")
            
i = 1
suma = 0
while i <=10:
    print(f"{i}/10")
    valor = validar()
    suma = suma + valor
    i +=1

promedio = suma // 10
print("La suma de los 10 valores es: "+str(suma))
print("El promedio es: "+str(promedio))
