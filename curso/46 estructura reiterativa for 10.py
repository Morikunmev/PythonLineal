def validar(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num<= 0 and num == float(num):
                continue
            else:
                return num
        except ValueError:
            continue
def equilaterodef(lado1,lado2,lado3):
    return lado1 == lado2 and lado1 == lado3
def isocelesdef(lado1, lado2, lado3):
    return lado1 == lado2 or lado1 == lado3 or lado2 == lado3
def escalenodef(lado1, lado2, lado3):
    return lado1 != lado2 and lado1 != lado3 and lado2 != lado3
def validartring():
    while True:
        try:
            lado1 = int(input("Ingresa el primer lado: "))
            lado2 = int(input("Ingresa el segundo lado: "))
            lado3 = int(input("Ingresa el tercer lado: "))
            if lado1<=0 or lado2<=0 or lado3<=0:
                continue
            else:
                return lado1, lado2, lado3
        except ValueError:
            continue
equilatero = 0
isoceles = 0
escaleno = 0
n = validar("Ingrese la cantidad de triangulos a evaluar: ")
for i in range(n):
    print(f"Triangulo nro {i+1}/{n}")
    lado1, lado2, lado3 = validartring()
    if equilaterodef(lado1,lado2,lado3):
        print("Triangulo equilatero")
        equilatero += 1
    elif isocelesdef(lado1, lado2, lado3):
        print("Triangulo isoceles")
        isoceles += 1
    elif escalenodef(lado1, lado2, lado3):
        print("Triangulo escaleno")
        escaleno += 1
print(f"{equilatero} triangulos equilateros")
print(f"{isoceles} triangulos isoceles")
print(f"{escaleno} triangulos escalenos")
