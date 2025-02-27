def validar(n):
    while True:
        try:
            num = int(input(n))
            if num<=0:
                continue
            elif num != 10:
                continue
            else:
                return num
        except ValueError:
            continue
        
def entero():
    while True:
        try:
            enter = int(input(f"Ingrese un valor de {i+1}: "))
            if enter <= 0:
                continue
            else:
                return enter
        except ValueError:
            continue


n = validar("Ingrese 10 valores: ")
suma = 0
for i in range(n):
    valor = entero()
    suma += valor

promedio = suma / n

print(f"La suma de los {n} valores es: {suma}")
print(f"el promedio de los {n} valores es: {promedio}")


    
    
