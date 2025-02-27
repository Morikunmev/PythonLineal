def validar(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num<=0 and num == float(num):
                continue
            elif 1<=num<=20:
                return num
        except ValueError:
            continue
def entero():
    while True:
        try:
            num = int(input(f"Ingresa un valor {i+1}/{n}"))
            if num == float(num) and num<=0:
                continue
            else:
                return num
        except ValueError:
            continue
        
def mayor100(valor):
    return valor>=1000

def primo(valor):
    if valor <2:
        return False
    for i in range(2,valor):
        if valor % i == 0:
            return False
    return True 

n = validar("Ingrese entre 1 y 20: ")
mayores1000 = 0
primoss = 0

for i in range(n):
    valor = entero()
    if mayor100(valor):
        mayores1000+=1
    if primo(valor):
        primoss+=1

print(f"{mayores1000} valores mayores a 1000")
print(f"{primoss} numeros primos")
        
        
    
