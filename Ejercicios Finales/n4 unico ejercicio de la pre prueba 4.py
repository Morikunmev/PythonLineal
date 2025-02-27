def salirdef(bucle,regsitro):
    if registro == 3:
        return False
    return bucle
def strings():
    while bucle:
        nombre = input("Ingrese su nombre: ")
        if nombre.isnumeric() or any (i.isnumeric() for i in nombre) or nombre.count(" ")>=1 or not nombre.isalpha():
            continue
        apellido = input("Ingrese su apellido: ")
        if apellido.isnumeric() or any (i.isnumeric() for i in apellido) or apellido.count(" ")>=1 or not apellido.isalpha():
            continue
        return nombre.capitalize(), apellido.capitalize()
    
def calculos(grat = 0.25, afp = 0.1225, salud = 0.07):
    while bucle:
        try:
            sueldo = float(input(f"Ingrese el sueldo del trabajador {nombre} {apellido}: "))
            if sueldo<=0:
                continue
            gratificacion = sueldo * (1+grat)
            gratificacion = round(gratificacion,2)

            afps = gratificacion * afp
            afps = round(afps,2)

            saluds = gratificacion * salud
            saluds = round(saluds,2)

            final = round(gratificacion - afps - saluds, 2)

            return sueldo, gratificacion, afps, saluds, final   
        except ValueError:
            continue

def mayordef(sueldo, mayor):
    if sueldo >mayor:
        return sueldo
    else:
        return mayor
def menordef(sueldo, menor):
    if sueldo <menor:
        return sueldo
    else:
        return menor

mayor = 0
menor = 99999999
bucle = True
registro = 0

nombres = ""
apellidos = ""

nombre_mayor= ""
apellido_mayor =""

nombre_menor = ""
apellido_menor = ""

sueldos = ""
gratificaciones = ""
afps = ""
saluds = ""
finals = ""

while salirdef(bucle,registro):
    registro+=1
    nombre, apellido = strings()
    nombres+=nombre + " "
    apellidos+=apellido + " "
    
    listanombre = nombres.split()
    listaapellido = apellidos.split()
    print(listanombre), print(listaapellido)

    sueldo, gratificacion, afp, salud, final = calculos(grat = 0.25, afp = 0.1225, salud = 0.07)
    print("El sueldo del trabajados {} {} es: {}".format(nombre,apellido,sueldo))
    print("La gratificacion del 25% del trabador {} {} es: {}".format(nombre,apellido,gratificacion))
    print("La afp del 12.25 % del trabajador {} {} es: {}".format(nombre, apellido, afp))
    print("La salud del 7% del trabajador {} {} es: {}".format(nombre,apellido, salud))
    print("los descuentos totales son: {}".format(final))
    
    mayor = mayordef(sueldo, mayor)
    if mayor == sueldo:
        nombre_mayor = nombre
        apellido_mayor = apellido
        
    menor = menordef(sueldo, menor)
    if menor == sueldo:
        nombre_menor = nombre
        apellido_menor = apellido

    sueldo = str(sueldo)
    sueldos+= "$" + sueldo +" "
    listasueldo = sueldos.split()
    print(listasueldo)

    gratificacion = str(gratificacion)
    gratificaciones+= "$" + gratificacion + " "
    listagrat = gratificaciones.split()
    print(listagrat)

    afp = str(afp)
    afps+= "-" + afp + " "
    listaafp = afps.split()
    print(listaafp)

    salud = str(salud)
    saluds+= "-" + salud + " "
    listasalud = saluds.split()
    print(listasalud)

    final = str(final)
    finals+= "$" + final + " "
    listafinal = finals.split()
    print(listafinal)
    
print(f"El trabajador con mayor sueldo es: {nombre_mayor} {apellido_mayor}, que es: {mayor}")
print(f"El trabajador con menor sueldo es: {nombre_menor} {apellido_menor}, que es: {menor}")

for i in range(len(listasueldo)):
    listasueldo[i] = listasueldo[i].replace("$","")
print(listasueldo)


    
