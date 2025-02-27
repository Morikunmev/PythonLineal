def validar():
    while True:
        try:
            num = int(input("Ingresa valores enteros: "))
            return num
        except ValueError:
            continue
def infinito():
    valor = 0
    suma = 0
    while valor !=-1:
        valor = validar()
        print("valor ingresado: {}".format(valor))
        suma += valor
    print(f"la suma es: {suma}")

infinito()
