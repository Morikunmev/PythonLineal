def validar():
    while True:
        nombre = input("Ingrese nombre: ")
        if nombre.isnumeric() or any(i in ["@","!","#","-"] for i in nombre):
            continue
        else:
            return nombre.capitalize().strip()
def correodef():
    while True:
        correo = input("Ingrese su correo: ")
        if "@" in correo and correo.count("@") == 1 and not any(i.isnumeric() for i in correo):
            return correo
        elif correo == "salir":
            return correo
        else:
            continue
def reemplazo(correo):
    if "@" in correo:
        nombre, dominio = correo.split("@")
        convertido = nombre + "@inacap.cl"
        return convertido
        

while True:
    nombre = validar()
    if nombre.capitalize() == "Salir":
        break
    print(nombre)
    correo = correodef()
    if correo == "salir":
        break
    if correo:
        print("Ahora eres de inacap!")
        convertido = reemplazo(correo)
        print(convertido)


