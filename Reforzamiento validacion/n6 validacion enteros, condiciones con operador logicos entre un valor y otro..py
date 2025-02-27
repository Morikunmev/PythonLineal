def validar(n):
    while True:
        try:
            num = int(input(n))
            if num>0 and num ==10:
                return num
            else:
                continue
        except ValueError:
            continue
def entero(n):
    while True:
        try:
            enter = int(input(n))
            if enter >0:
                return enter
            else:
                continue
        except ValueError:
            continue

n = validar("Ingrese 10 valores: ")
suma = 0
for i in range(n):
    valor = entero(f"Ingrese valor: {i+1}/{n}")
    suma += valor
promedio = suma / n
print(f"La suma de los {n} valores es: {suma}")
print(f"el promedio de los {n} valores es: {promedio}")


    
