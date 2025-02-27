def nombredef():
    while True:
        nombre = input("Ingrese un nombre: ")
        if nombre.isnumeric() or any (i in ["@","!","#","-"] for i in nombre):
            continue
        return nombre.capitalize().strip()
def vocaldef(nombre):
    if nombre[0] in ["A","E","I","O","U"]:
        nombre = nombre.replace("A","R").replace("E","2").replace("I","3").replace("O","4").replace("U","5")
        return nombre

while True:
    nombre = nombredef()
    if vocaldef(nombre):
        print("Empieza con una vocal")
        cambiado = vocaldef(nombre)
        print(cambiado)
        
