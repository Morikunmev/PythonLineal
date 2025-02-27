def validar():
    while True:
        nombre = input("Ingrese nombre: ")
        for i in nombre:
            if i in ["@","!","#","-"] or i.isnumeric():
                continue
            else:
                return nombre

while True:
    nombre = validar()
    print(nombre)
