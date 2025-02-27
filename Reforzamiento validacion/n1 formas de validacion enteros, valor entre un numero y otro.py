def primera_forma():
    n1 = int(input("Ingresa valores entre 4 y 3000"))
    while True:
        if n1 >= 4 and n1 <=3000:
            print("Valido")
            break
        else:
            n = int(input("Incorrecto, Volver a intentar"))

def segunda_forma():
    n1 = int(input("Ingrese un numero entre 4 y 3000"))
    while not(4<= n1 <=3000):
        n1 = int(input("Ingrese nuevamente"))
    print("Perfecto")

def tercera_forma():
    n1 = int(input("Ingrese un numero entre 4 y 3000"))
    while 4 >= n1 or n1 >=3000:
        n1 = int(input("Ingrese nuevamente"))

    print("Perfecto")


