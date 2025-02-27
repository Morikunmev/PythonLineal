def salir(opcion, registro):
    if registro>=3:
        string = input(opcion)
        if string.lower().strip() in ["si", "s"]:
            return False
        elif registro == 6:
            return False
        else:
            return True
    return True

def nombredef():
    while True:
        nombre = input("Ingrese su nombre: ")
        for i in nombre:
            if i in ["@","!","#","-"] or i.isnumeric() or any(i.isnumeric() for i in nombre) or nombre.count(" ")>=1:
                continue
            else:
                return nombre.capitalize()
def apellidodef():
    while True:
        apellido = input("Ingrese su apellido: ")
        for i in apellido:
            if i in ["@","!","#","-"] or i.isnumeric() or any(i.isnumeric() for i in apellido) or apellido.count(" ")>=1:
                continue
            else:
                return apellido.capitalize()

def repetido2(apellido):
    if apellido in apellidos:
        return True
    else:
        return False
    
def repetido(nombre):
    if nombre in nombres:
        return True
    else:
        return False

def notadef():
    while True:
        try:
            nota = float(input(f"Ingrese nota nro {i+1} /3: "))
            if 1.0<= nota<=7.0:
                return nota
            else:
                continue
        except ValueError:
            continue
        
def mayordef(promedio,mayor):
    if promedio > mayor:
        return promedio
    else:
        return mayor
    
def menordef(promedio,menor):
    if promedio<menor:
        return promedio
    else:
        return menor

registro = 0
nombres = " "
apellidos = " "
opcion = True
promedios = ""
mayor = 0
menor = 7.0

nombre_mayor = " "
nombre_menor = " "


while salir("Quieres finalizar el bucle?: ", registro):
    registro +=1
    print(f"registro nro {registro}")
    nombre = nombredef()
    while repetido(nombre):
        print("Nombre repetido, intentar nuevamente")
        nombre = nombredef()
    nombres+=nombre + " "
    convertido1 = nombres.split()
    print(convertido1)

    apellido = apellidodef()
    while repetido2(apellido):
        print("Apellido repetido, intentar nuevamente")
        apellido = apellidodef()
    apellidos+= apellido + " "
    convertido2 = apellidos.split()
    print(convertido2)

    suma = 0
    for i in range(3):
        nota = notadef()
        suma += nota
    promedio = suma / 3

    mayor = mayordef(promedio, mayor)
    if mayor == promedio:
        nombre_mayor = nombre
        
    menor = menordef(promedio,menor)
    if menor == promedio:
        nombre_menor = nombre
    
    promedio = str(round(promedio,1))
    promedios+=promedio+" "
    convertido3 = promedios.split()
    print(convertido3)
        

    
print(f"El promedio mayor fue: {round(mayor,1)} que pertenece a: {nombre_mayor}")
print(f"El promedio menor fue: {round(menor,1)} que pertenece a: {nombre_menor}")
for i in range(registro):
    print(f"Registro nro: {i+1}, nombre: {convertido1[i]}, apellido: {convertido2[i]}, promedio: {convertido3[i]})")
