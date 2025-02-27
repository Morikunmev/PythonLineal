def salirdef(bucle,contador):
    contador = len(contador)
    if contador == 4:
        return False
    return bucle

def strings():
    while bucle:
        nombre = input("Ingrese el nombre del trabajador: ")
        while nombre.isnumeric() or any(i.isnumeric() for i in nombre) or not nombre.isalpha() or nombre.count(" ")>=1:
            nombre = input("Ingrese el nombre del trabajador: ")
        apellido = input("Ingrese el apellido del trabajador: ")
        while apellido.isnumeric() or any(i.isnumeric() for i in apellido) or not apellido.isalpha() or apellido.count(" ")>=1:
            apellido = input("Ingrese el apellido del trabajador: ")
        empresa = input("Ingrese la empresa en la que esta trabajado: ")
        while empresa.isnumeric() or any(i.isnumeric() for i in empresa) or not empresa.isalpha() or empresa.count(" ") >3:
            empresa = input("Ingrese la empresa en la que esta trabajando: ")

        pub = input("Ingrese si es publica o privada: ")
        while not pub.lower() in ["publica","privada"]:
            pub = input("Ingrese si es publica o privada: ")
        return nombre.capitalize(), apellido.capitalize(), empresa.capitalize(), pub.capitalize()

def calculo(grat=0.25,afp=0.1225,salud=0.07):
    n1 = f"el sueldo del trabajador {nombre} {apellido}:"
    n2 = "la gratificacion del 25% es:"
    n3 = "la afp del 12.25% es:"
    n4 = "la salud del 7% es:"
    n5 = "los descuentos totales son:"
    while bucle:
        try:
            sueldo = float(input(f"Ingrese el sueldo del trabajador {nombre} {apellido}: "))
            while sueldo<=0:
                sueldo = float(input(f"Ingrese el sueldo del trabajador {nombre} {apellido}: "))
            gratificacion = sueldo * (1+grat)
            gratificacion = round(gratificacion,2)

            afps = round(gratificacion * afp,2)
            saluds = round(gratificacion *salud,2)
            final = round(gratificacion - afps - saluds,2)

            return n1,sueldo, n2, gratificacion,n3,afps,n4,saluds,n5,final

        except ValueError:
            continue
def mayordef():
    if sueldo > mayor:
        return sueldo
    else:
        return mayor
def menordef():
    if sueldo < menor:
        return sueldo
    else:
        return menor
def publicadef():
    if pub.lower() == "publica":
        return True
def privadadef():
    if pub.lower() == "privada":
        return True
bucle = True

contador = ""
registro = ""

publicas = ""
privadas = ""

nombres = ""
apellidos = ""
empresas = ""

mayor = 0
menor = 999999

sueldo_mayor = ""
sueldo_menor = ""

sueldos = ""
gratificaciones = ""
afpss = ""
saludss = ""
finales= ""

lista3 = "0"
lista4 = "0"

while salirdef(bucle,contador):
    contador+="1" + " "
    lista = contador.split()
    lista = len(lista)
    lista = str(lista)

    registro+=lista + " "
    lista1 = registro.split()
    for i in range(len(lista1)):
        lista1[i] = int(lista1[i])
    print(f"Registro nro: {lista}")
    print(f"Lista de registros: {lista1}")

    nombre, apellido, empresa,pub = strings()
    if publicadef():
        publicas+=pub + " "
        lista3 = publicas.split()
        lista3 = len(lista3)
    elif privadadef():
        privadas+= pub+ " "
        lista4 = privadas.split()
        lista4 = len(lista4)

        

    nombres+=nombre + " "
    apellidos+= apellido + " "
    empresas+= empresa + " "

    listanombres = nombres.split()
    listaapellidos = apellidos.split()
    listaempresas = empresas.split()

    n1,sueldo, n2, gratificacion,n3,afps,n4,saluds,n5,final = calculo(grat=0.25,afp=0.1225,salud=0.07)
    print()
    print(n1,sueldo)
    print(n2,gratificacion)
    print(n3,afps)
    print(n4,saluds)
    print(n5,final)

    mayor = mayordef()
    if mayor == sueldo:
        sueldo_mayor = nombre
    menor = menordef()
    if menor == sueldo:
        sueldo_menor = nombre

    gratificacion = str(gratificacion)
    gratificaciones+= "$" + gratificacion + " "
    listagrat = gratificaciones.split()

    afps = str(afps)
    afpss+"-" + afps + " "
    listaafp = afpss.split()

    saluds = str(saluds)
    saludss+= "-" + saluds + " "
    listasalud = saludss.split()

    final = str(final)
    finales+="$" +final + " "
    listafinal = finales.split()

print(f"El trabajador con mayor sueldo es: {sueldo_mayor}, que es: {mayor}")
print(f"El trabajador con menor sueldo es: {sueldo_menor}, que es: {menor}")

for i in range(len(lista1)):
    print(f"registro nro {lista1[i]}, nombre: {listanombres[i]}, empresa: {listaempresas[i]}")
print(f"empresas publicas: {lista3}")
print(f"empresas privadas: {lista4}")
    
        
    
    
    
    
