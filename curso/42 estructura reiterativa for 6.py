def validar(n):
    while True:
        try:
            num = int(input(n))
            if num<=0 and num == float(num):
                continue
            else:
                return num
        except ValueError:
            continue

def medidas(base, altura):
    while True:
        try:
            base = int(input(f"Ingrese base {i+1}/{n}: "))
            altura = int(input(f"Ingrese la altura {i+1}/{n}: "))
            if base<=0 and altura<=0:
                continue
            else:
                return base,altura
        except ValueError:
            continue

def mayor(superficie):
    return superficie>12

n = validar("Ingrese cantidad a evaluar: ")
base = 0
altura = 0
cantidad = 0
for i in range(n):
    base, altura = medidas(base, altura)
    superficie = (base * altura) / 2
    print(f"calculo {superficie}")
    if mayor(superficie):
        cantidad +=1
print(f"Cantidad de triangulos con superficie mayor a 12 es: {cantidad}")
    
    
