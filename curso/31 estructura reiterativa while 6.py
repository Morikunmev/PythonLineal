def validar():
    while True:
        try:
            num = float(input("Ingrese la altura: "))
            return num
        except ValueError:
            continue

def validar1(n):
    while True:
        try:
            num = int(input(n))
            if num <= 0:
                print("No puede ingresar valores menores o iguales a 0")
            else:
                return num
        except ValueError:
            continue
        
n = validar1("Ingrese personas a evaluar: ")
x = 1
suma = 0
while x <= n:
    altura = validar()
    suma += altura
    promedio = suma / n
    x+=1

print(f"el promedio de {n} personas es {promedio}")
