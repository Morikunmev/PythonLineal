def validar(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num >0 and num == 10:
                return num
        except ValueError:
            continue
        
def mayor(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num == float(num) and num<=0:
                continue
            else:
                return num
        except ValueError:
            continue
        
def multiplo3(valor):
    return valor % 3 == 0
def multiplo5(valor):
    return valor %5 == 0

def primo(valor):
    if valor <2:
        return False
    for i in range(2, valor):
        if valor % i == 0:
            return False
    return True

        
numeros = validar("Ingrese 10 numeros: ")
mult3 = 0
mult5 = 0
primos = 0
for i in range(numeros):
    valor = mayor(f"Ingrese un valor {i+1}/{numeros}")
    if multiplo3(valor):
        mult3+= 1
    elif multiplo5(valor):
        mult5 +=1
    if primo(valor):
        primos +=1
        
print(f"{mult3} numeros multiplos de 3")
print(f"{mult5} numeros multiplos de 5")
print(f"{primos} numeros primos")


        
    
    
    
