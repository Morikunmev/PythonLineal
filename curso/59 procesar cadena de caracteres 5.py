def validar(bucle):
    while bucle:
        string = input("Ingresa: ").strip()
        return string
def cantidad(string):
    string = string.lower()
    acumulador = string.count("a") + string.count("e") + string.count("i") + string.count("o") + string.count("u")
    return acumulador

bucle = True
while bucle:
    acumulador = 0
    string = validar(bucle)
    cantidad1 =  cantidad(string)
    print(f"hay {cantidad1} vocales")


