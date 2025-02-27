def validar(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num <= 0:
                continue
            else:
                return num
        except ValueError:
            continue
def mayordef(suma1,suma2):
    return suma1>suma2
def menordef(suma1, suma2):
    return suma1<suma2
def repetir(suma1, suma2):
    return suma1 == suma2

i = 1
y = 1
suma1 = 0
suma2 = 0
print("Carga de la primera lista")
while i <=2:
    numero = validar("Ingresa un numero: ")
    suma1 += numero
    i+=1
print("Carga de la segunda lista")
while y <= 2:
    numero1 = validar("Ingresa un numero: ")
    suma2 += numero1
    y+= 1

if mayordef(suma1,suma2):
    print("La primera lista tiene valor mayor")
elif menordef(suma1, suma2):
    print("La segunda lista tiene mayor valor")
elif repetir(suma1,suma2):
    print("Las dos listas son iguales")

    

    
