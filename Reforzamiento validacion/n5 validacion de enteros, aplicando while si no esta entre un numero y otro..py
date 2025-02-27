def validacion(n1):
    while True:
        try:
            num = int(input(n1))
            while not (1<=num <=10):
                num = int(input("Ingrese nuevamente: "))
            return num
        except ValueError:
            print("Ingrese valores enteros")

def val(n2):
    while True:
        try:
            num = int(input(n2))
            if num>=11 and num<=20:
                return num
            else:
                continue
        except ValueError:
            print("Ingrese valores enteros")

n1 = validacion("Ingresa un numero entre 1 y 10: ")
print("El numero ingresado es: " +str(n1))

n2 = val("Ingrese un numero entre 11 y 20: ")
print("El numero ingresado es: " +str(n2))
