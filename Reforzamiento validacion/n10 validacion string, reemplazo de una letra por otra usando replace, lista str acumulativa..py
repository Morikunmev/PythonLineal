def string():
    while True:
        string = input("Ingrese un texto: ").strip().lower()
        if string.isnumeric() or any(i in ["@","!","#","-"] for i in string):
            continue
        else:
            return string
def opciondef(opcion):
    while True:
        string = input(opcion).strip().lower()
        if string in ["si","s"]:
            return string
        else:
            return string

cadena = ""

while True:
    nombre = string()
    nombre = nombre.replace("r", "1").replace("s","2")
    #le puse las comillas porque quiero separarlo
    cadena += nombre + " "
    print(cadena)
    opcion = opciondef("Quieres descifrar lo escrito?: ")
    if opcion in ["si","s"]:
        cadena = cadena.replace("1", "r").replace("2","s")
        print(cadena)
        cadena = " "
    else:
        continue
    
    
