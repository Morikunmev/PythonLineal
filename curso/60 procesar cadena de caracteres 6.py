def validacion(bucle):
    while bucle:
        nombre = input("Ingrese su clave: ")
        if len(nombre)>=10 and len(nombre) <=20:
            return nombre
        else:
            print("Tiene que tener entre 10 y 20 caracteres")
bucle = True

def contador(clave):
    clave = len(clave)
    return clave

while bucle:
    clave = validacion(bucle)
    if clave:
        print("exitoso")
        print(f"Se han ingresado {contador(clave)} caracteres")
