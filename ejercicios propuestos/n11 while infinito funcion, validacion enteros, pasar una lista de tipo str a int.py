def salirdef(registro):
    if registro == 5:
        return False
    return True

def enteros():
    while True:
        try:
            numeros = int(input(f"Ingrese un numero {registro}/ 5: "))
            if numeros <= 0 or not 1<=numeros<=100:
                continue
            return numeros
        except ValueError:
            continue

registro = 0
numeros = " "
while salirdef(registro):
    registro+=1

    numero = enteros()
    numero = str(numero)
    numeros+=numero+" "
    listado1 = numeros.split()

listado1 = [int(i) for i in listado1]
print(listado1)
suma = 0
for i in listado1:
    suma+=i
print(suma)

