def validacion():
    while True:
        try:
            n = int(input("Ingrese numeros entre 1 y 10: "))
            if n == 10 or n != float(n):
                return n
            else:
                continue
        except ValueError:
            continue

def enteros(valor):
    while True:
        try:
            num = int(input(valor))
            if num<= 0 and num == float(num):
                continue
            else:
                return num
        except ValueError:
            continue
        
cant = validacion()
suma = 0
for i in range(cant):
    valor = enteros(f"Ingrese un valor {i+1}/{cant}: ")
    if i >4:
        suma += valor
print(f"La suma de los 5 ultimos numeros es {suma}")
    
        
        
