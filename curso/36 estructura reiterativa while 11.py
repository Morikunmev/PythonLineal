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
def paresdef(valor):
    return valor %2 == 0

n = validar("Ingresa numeros enteros: ")
i = 1
pares = 0
impares = 0

while i <= n:
    valor = validar("Ingrese el valor: ")
    if paresdef(valor):
        pares += 1
    else:
        impares +=1
    i+=1

print("La cantidad de valores pares es: "+str(pares))
print("La cantidad de valores impares es: "+str(impares))
