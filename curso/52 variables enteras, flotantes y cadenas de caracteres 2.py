def nombredef():
    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre.isnumeric() or any(i in ["@","!","#","-"] for i in nombre):
            continue
        else:
            return nombre.capitalize().strip()

def mayordef(nombremayor, nombre):
    if nombremayor is None or nombre > nombremayor:
        return nombre
    else:
        return nombremayor
    
def menordef(nombremenor, nombre):
    if nombremenor is None or nombre < nombremenor:
        return nombre
    else:
        return nombremenor
nombremayor = None
nombremenor = None

for i in range(2):
    nombre = nombredef()
    print("Nombre ingresado: {}".format(nombre))
    nombremayor = mayordef (nombremayor,nombre)
    nombremenor = menordef (nombremenor,nombre)
print(f"El nombre mayor alfabeticamente es: {nombremayor}")
print(f"El nombre menor alfabeticamente es: {nombremenor}")
