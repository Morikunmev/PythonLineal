def validacion1(n1):
    return 1<= n1 <=12
def validacion2(n2):
    return 13<= n2 <=17

n1 = int(input("Ingresa un numero entre 1 y 12: "))
n2 = int(input("Ingresa un numero entre 13 y 17: "))

while True:
    if validacion1(n1) and validacion2(n2):
        print("Valido")
        break
    else:
        print("Intentelo nuevamente")
        n1 = int(input("Ingresa un numero entre 1 y 12: "))
        n2 = int(input("Ingresa un numero entre 13 y 17: "))
