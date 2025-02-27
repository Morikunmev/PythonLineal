def primo(valor):
    if valor <2:
        return False
    for i in range(2, valor):
        if valor % i == 0:
            return False
    return True

n = int(input("Ingresa un numero: "))
for i in range(n):
    valor = int(input(f"Ingresa un valor {i+1}/{n}: "))
    if primo(valor):
        print("Es primo")
