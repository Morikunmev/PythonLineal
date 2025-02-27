def repetidos(numero):
    suma = numero.count("a") + numero.count("e")
    return suma



while True:
    numero = input("Ingresa la clave: ")
    print(repetidos(numero))


