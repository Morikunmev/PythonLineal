def salir(bucle,general):
    general = len(general)
    if general == 4:
        return False
    return bucle
def string():
    while bucle:
        nombre = input("Ingresa el nombre: ")
        while nombre.isnumeric() or any(i.isnumeric() for i in nombre) or nombre.count(" ")>=1 or not nombre.isalpha():
            nombre = input("Ingresa el nombre: ")
        apellido = input("Ingresa el apellido: ")
        while apellido.isnumeric() or any(i.isnumeric() for i in apellido) or apellido.count(" ")>=1 or not apellido.isalpha():
            apellido = input("Ingresa el apellido: ")

        return nombre.capitalize(), apellido.capitalize()
def notadef():
    suma = 0
    promedio = 0

    n1 = "El promedio que pertenece al 10% corresponde a: "
    n2 = "La nota del trabajo que pertenece al 20% corresponde a: "
    n3 = "la nota de la teorica que pertenece al 30% corresponde a: "
    n4 = "La nota del desarrollo que pertenece al 40% corresponde a: "
    n5 = "El ponderado total del alumno es: "

    while bucle:
        try:
            for i in range(3):
                nota = float(input(f"Ingresa la nota nro: {i+1} / 3: "))
                while not 1.0<=nota<=7.0:
                    nota = float(input(f"Ingresa la nota nro: {i+1} / 3"))
            suma+= nota
            promedio = suma / 3
            promedio*=0.1

            trabajo = float(input("Ingrese la nota del trabajo: "))
            while not 1.0<=trabajo<=7.0:
                trabajo = float(input("Ingrese la nota del trabajo: "))
            trabajo*= 0.2

            teorica = float(input("Ingrese la nota de la teorica: "))
            while not 1.0 <=teorica<= 7.0:
                teorica = float(input("Ingrese la nota de la teorica: "))
            teorica*=0.3

            desarrollo = float(input("Ingrese la nota del desarrollo: "))
            while not 1.0 <=desarrollo<=7.0:
                desarrollo = float(input("Ingrese la nota del desarrollo: "))
            desarrollo*= 0.4

            ponderado = promedio + trabajo + teorica + desarrollo

            return n1, round(promedio,2), n2, round(trabajo,2), n3, round(teorica,2), n4, round(desarrollo, 2), n5, round(ponderado,2)
        except ValueError:
            continue
    
def mayordef(mayor, ponderado):
    if mayor > ponderado:
        return mayor
    else:
        return ponderado
def menordef(menor, ponderado):
    if menor < ponderado:
        return menor
    else:
        return ponderado
def juicio():
    n1 = "Nivel mediocre"
    n2 = "Nivel bien"
    if promedioG <=3.9:
        return promedioG, n1
    else:
        return promedioG, n2
        

bucle = True

general = ""
general1 = ""

nombres = ""
apellidos = ""

promedios = ""
trabajos = ""
teoricas = ""
desarrollos = ""
ponderados = ""

mayor_nombre = ""
menor_nombre = ""

promedioG = 0

mayor = 0
menor = 7.0

while salir(bucle,general):
    
    general+= "1" + " "
    listageneral = general.split()
    listageneral = len(listageneral)
    listageneral = str(listageneral)
    
    general1+= listageneral + " "
    listageneral1 = general1.split()
    for i in range(len(listageneral1)):
        listageneral1[i] = int(listageneral1[i])

    print(f"LISTADO GENERAL: {listageneral1}")
    print(f"Registro nro: {listageneral}")
    print()
    
    
    nombre, apellido = string()
    
    nombres+=nombre + " "
    listanombre = nombres.split()

    apellidos+=apellido + " "
    listaapellido = apellidos.split()
    
    n1, promedio, n2, trabajo, n3, teorica, n4, desarrollo, n5, ponderado = notadef()
    print(n1,promedio)
    print(n2,trabajo)
    print(n3,teorica)
    print(n4,desarrollo)
    print(n5,ponderado)

    mayor = mayordef(mayor, ponderado)
    if mayor == ponderado:
        mayor_nombre = nombre
    menor = menordef(menor, ponderado)
    if menor == ponderado:
        menor_nombre = nombre

    promedioG+=ponderado
    print(f"suma total del promedio: {promedioG}")

    promedio = str(promedio)
    promedios+= promedio + " "
    listap = promedios.split()
    print(f"listado promedios {listap}")

    trabajo = str(trabajo)
    trabajos+= trabajo + " "
    listat = trabajos.split()
    print(f"Listado trabajos {listat}")

    teorica = str(teorica)
    teoricas+= teorica + " "
    listatt = teoricas.split()
    print(f"Listado teoricas {listatt}")

    desarrollo = str(desarrollo)
    desarrollos+=desarrollo + " "
    listad = desarrollos.split()
    print(f"Listado desarrollos {listad}")

    ponderado = str(ponderado)
    ponderados+= ponderado + " "
    listapo = ponderados.split()
    print(f"Listado ponderados {listapo}")
    print()
for i in range(len(listap)):
    listap[i] = float(listap[i])
for i in range(len(listat)):
    listat[i] = float(listat[i])
for i in range(len(listatt)):
    listatt[i] = float(listatt[i])
for i in range(len(listad)):
    listad[i] = float(listad[i])
for i in range(len(listapo)):
    listapo[i] = float(listapo[i])

print(listap),print(listat),print(listatt),print(listad),print(listapo),print()
promedioG = promedioG / 2
print(f"El promedio general de los {listageneral} alumnos: {round(promedioG,2)}")
print(f"El mayor ponderado perteneciente al nombre {mayor_nombre} es: {mayor}")
print(f"El menor ponderado perteneciente al nombre {menor_nombre} es: {menor}")

juicio, n1 = juicio()
print(f"El lvl del promedio es: {juicio} que corresponde a: {n1}")
    

    
    
