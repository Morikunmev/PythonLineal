def validar():
    while True:
        try:
            num = int(input("Ingresa un valor: "))
            return num
        except ValueError:
            continue
def afirmaciondef(opcion):
    while True:
        opcion = input("Desea cargar otro valor?: ").strip().lower()
        if opcion in ["si","s"]:
            return opcion
        else:
            break

suma = 0
opcion = ""
while True:
    valor = validar()
    suma += valor
    if afirmaciondef(opcion):
        continue
    else:
        break

print(f"La suma total es: {suma}")
