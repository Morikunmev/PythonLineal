def nombredef():
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.isnumeric() or any(i in ["@","#","-","!"] for i in nombre):
            continue
        else:
            return nombre.capitalize().strip()

nombre = nombredef()
print(f"Nombre ingresado: {nombre}")
