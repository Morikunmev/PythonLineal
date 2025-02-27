def validar(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num == 10:
                return num
        except ValueError:
            continue
def enteros():
    while True:
        try:
            valor = int(input(f"Ingrese un valor {i+1}/{cant}: "))
            return valor
        except ValueError:
            continue
        
def multiplo15(valor):
    if valor % 15 == 0:
        return valor
def par(valor):
    if valor %2 == 0:
        return valor
def positiv(valor):
    return valor>0
def negativ(valor):
    return valor<0

cant = validar("Ingrese 10: ")
positivos = 0
negativos = 0
mult15 = 0
pares = 0
for i in range(cant):
    valor = enteros()
    if positiv(valor):
        positivos += 1
    elif negativ(valor):
        negativos += 1
    if multiplo15(valor):
        mult15 += 1
    if par(valor):
        pares += 1

print(f"valores positivos: {positivos}")
print(f"valores negativos: {negativos}")
print(f"valores multiplos de 15: {mult15}")
print(f"Valores partes: {pares}")
        
    
