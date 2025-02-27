def nombredef():
    while True:
        nombre = input("Ingrese su nombre: ")
        for i in nombre:
            if i.isnumeric() or i in ["@","!","#","-"] or nombre.count(" ") >=1 or any(i.isnumeric() for i in nombre):
                continue
            else:
                return nombre.capitalize()
            
def repetido(nombre):
    if nombre in nombres:
        return True
    else:
        return False
    
def salir(opcion, registro):
    if registro >=5:
        string = input(opcion)
        if string.lower().strip() == "si":
            return False
        else:
            return True
    return True
    
    

nombres = " "
registro = 0
opcion = True

while salir("quieres finalizar el bucle?: ", registro):
    nombre = nombredef()
    while repetido(nombre):
        print("Nombre repetido")
        nombre = nombredef()
    nombres+= nombre + " "
    convertido = nombres.split()
    print(convertido)
    registro+= 1
    
for i in range(registro):
    print(f"registro nro: {i+1}, nombre: {convertido[i]}")
    
