def validacion(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero in ["@", "#"]:
                print("No puede ingresar esos caracteres")
            elif numero < 3 or numero >3000:
                print("El numero debe estar entre 3 y 3000.")
            else:
                return numero
        except ValueError:
            print("Tiene que ingresar valores enteros")


while True:
    n = validacion("Ingrese un numero entre 3 y 3000: ")
    print("El numero ingresado es: " +str(n))
