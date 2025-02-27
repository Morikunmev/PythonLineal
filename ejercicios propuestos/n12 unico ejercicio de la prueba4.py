def salirdef(registro):
    if registro == 5:
        return False
    return True

def nombredef(infinito):
    while infinito:
        nombre = input(f"Ingresa un nombre {registro}/5: ")
        if nombre.isnumeric() or any(i.isnumeric() for i in nombre) or not nombre.isalpha() or nombre.count(" ")>=1:
            continue
        return nombre.capitalize()
    
def sueldodef(infinito):
    while infinito:
        try:
            sueldo = float(input(f"Ingresa el sueldo del trabajador {nombre}: "))
            if sueldo <=0:
                continue
            return sueldo
        except ValueError:
            continue

def gratificaciondef(sueldo):
    sueldo = float(sueldo)
    calculo = round(sueldo * (1+0.25),1)
    return calculo

def afpdef(gratificacion):
    gratificacion = float(gratificacion)
    calculo = round(gratificacion * 0.1225,3)
    return calculo

def saluddef(gratificacion):
    gratificacion = float(gratificacion)
    calculo = round(gratificacion * 0.07, 3)
    return calculo

def finaldef(gratificacion, afp, salud):
    gratificacion, afp, salud = float(gratificacion), float(afp), float(salud)
    calculo = round(gratificacion - afp - salud,2)
    return calculo
    
infinito = True
registro = 0

nombres = ""
sueldos = ""

grat = ""
afps = ""
saluds = ""
sueldofinal = ""


while salirdef(registro):
    registro+=1
    print()
    #pedir el nombre
    nombre = nombredef(infinito)
    nombres+=nombre + " "
    #conversion
    listanombres = nombres.split()
    print(listanombres)

    #pedir el sueldo
    sueldo = sueldodef(infinito)
    sueldo = str(sueldo)
    sueldos+= "$" + sueldo + " "
    print()
    #conversion
    listasueldos = sueldos.split()
    print("Lista de sueldos")
    print(listasueldos)

    #calculo de gratificacion
    gratificacion = gratificaciondef(sueldo)
    gratificacion = str(gratificacion)
    grat+= "$" + gratificacion + " "
    #conversion
    print("Lista de gratificacion del 25% en total: ")
    listagratificacion = grat.split()
    print(listagratificacion)

    #calculo de afp
    afp = afpdef(gratificacion)
    afp = str(afp)
    afps+= "$" + afp + " "
    #conversion
    listadoafp = afps.split()
    print("Lista de descuento de afp del 12.25%: ")
    print(listadoafp)

    #calculo de descuento salud
    salud = saluddef(gratificacion)
    salud = str(salud)
    saluds+= "$" + salud + ""
    #conversion
    listasalud = saluds.split()
    print("Lista descuento salud del 7%: ")
    print(listasalud)

    #calculo de sueldo final
    final = finaldef(gratificacion, afp, salud)
    final = str(final)
    sueldofinal+= "$" + final + " "
    #conversion
    listadofinal = sueldofinal.split()
    print("Lista de sueldo final: ")
    print(listadofinal)

for i in range(registro):
    print(f"registro nro {i+1}: {listanombres[i]}, {listadofinal[i]}")

for x in range(len(listadofinal)):
    listadofinal[x] = listadofinal[x].replace("$","")
print(listadofinal)

listadofinal = [float(i) for i in listadofinal]
print(listadofinal)
