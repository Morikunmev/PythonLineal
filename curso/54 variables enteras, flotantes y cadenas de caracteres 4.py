def nombredef():
    while True:
        nombre = input("Ingresa el nombre: ")
        if nombre.isnumeric() or any (i in ["@","!","#","-"] for i in nombre):
            continue
        else:
            return nombre.capitalize().strip()
def igual(nombre):
    if nombre in listado:
        return True
    else:
        return False
    
def mayordef(mayor, nombre):
    if mayor is None or nombre>mayor:
        return nombre
    else:
        return mayor
    
def menordef(menor, nombre):
    if menor is None or nombre<menor:
        return nombre
    else:
        return menor
    
def validar():
    while True:
        try:
            num = int(input("Ingrese la cantidad a evaluar: "))
            if num<= 0:
                continue
            else:
                return num
        except ValueError:
            continue
    
listado = ""
mayor = None
menor = None
cantidad = validar()
for i in range(cantidad):
    nombre = nombredef()
    while igual(nombre):
        print("Nombre repetido, ingrese nuevamente")
        nombre = nombredef()
    listado+=nombre + ", "
    print(listado)
    mayor = mayordef(mayor, nombre)
    menor = menordef(menor, nombre)
print(listado)
print("El mayor alfabeticamente es: {}".format(mayor))
print("El menor alfabeticamente es: {}".format(menor))

