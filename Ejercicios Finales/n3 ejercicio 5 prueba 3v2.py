def salir(bucle, registro):
    if registro == 3:
        return False
    return bucle

def strings():
    while bucle:
        nombre = input("Ingresa el nombre: ")
        while nombre.isnumeric() or any(i.isnumeric() for i in nombre) or nombre.count(" ")>=1 or not nombre.isalpha():
            nombre = input("Ingresa el nombre: ")
        apellido = input("Ingresa el apellido: ")
        while apellido.isnumeric() or any (i.isnumeric() for i in apellido) or apellido.count(" ")>=1 or not apellido.isalpha():
            apellido = input("Ingresa el apellido: ")
        return nombre.capitalize(), apellido.capitalize()
def notadef():
    suma = 0
    promedio = 0
    
    while bucle:
        try:
            for i in range(3):
                nota = float(input(f"Ingresa la nota nro {i+1} / 3: "))
                while not 1.0<=nota<=7.0:
                    nota = float(input(f"Ingresa la nota nro {i+1} / 3:"))
            suma+= nota
            promedio = suma / 3
            promedio = promedio * 0.1

            trabajo = float(input("Ingrese la nota del trabajo: "))
            while not 1.0<=trabajo<=7.0:
                trabajo = float(input("Ingrese la nota del trabajo: "))
            trabajo*= 0.2

            teorica = float(input("Ingrese la nota de la teorica: "))
            while not 1.0<=teorica<=7.0:
                teorica = float(input("Ingrese la nota de la teorica: "))
            teorica*= 0.3

            desarrollo = float(input("Ingrese la nota del desarrollo: "))
            while not 1.0<=desarrollo<=7.0:
                desarrollo = float(input("Ingrese la nota del desarrollo: "))
            desarrollo*= 0.4

            ponderado = promedio + trabajo + teorica + desarrollo
            return round(promedio,2), round(trabajo,2), round(teorica,2), round(desarrollo,2), round(ponderado,2)
        except ValueError:
            continue
def mayordef(ponderado,mayor):
    if mayor > ponderado:
        return mayor
    else:
        return ponderado
def menordef(ponderado, menor):
    if menor < ponderado:
        return menor
    else:
        return ponderado
def promediodef(ponderado):
    return ponderado
    


mayor = 0
menor = 7.0
registro = 0
bucle = True
promedioG = 0

nombres = ""
apellidos = ""

notas = ""
trabajos = ""
teoricas = ""
desarrollos = ""
ponderados = ""

mayor_nombre = ""
menor_nombre = ""

while salir(bucle, registro):
    registro +=1
    print(f"registro nro {registro}")
    nombre, apellido = strings()
    nombres+=nombre + ","
    apellidos+=apellido + ","
    
    nombres = nombres.replace(","," ")
    apellidos = apellidos.replace(","," ")
    
    listanombres = nombres.split()
    listaapellidos = apellidos.split()
    print(listanombres), print(listaapellidos)

    nota, trabajo, teorica, desarrollo, ponderado = notadef()

    mayor = mayordef(ponderado,mayor)
    if mayor == ponderado:
        mayor_nombre = nombre
    menor = menordef(ponderado, menor)
    if menor == ponderado:
        menor_nombre = nombre
        
    promedioG+=promediodef(ponderado)
    print(promedioG)
    
    nota = str(nota)
    trabajo = str(trabajo)
    teorica = str(teorica)
    desarrollo = str(desarrollo)
    ponderado = str(ponderado)
    
    notas+=nota + ","
    trabajos+=trabajo+ ","
    teoricas+= teorica+ ","
    desarrollos+=desarrollo + ","
    ponderados+= ponderado+ ","

    notas = notas.replace(","," ")
    trabajos = trabajos.replace(","," ")
    teoricas = teoricas.replace(","," ")
    desarrollos = desarrollos.replace(","," ")
    ponderados = ponderados.replace(","," ")

    listanotas = notas.split()
    listatrabajos = trabajos.split()
    listateoricas = teoricas.split()
    listadesarrollos = desarrollos.split()
    listaponderados = ponderados.split()
    
    for i in range(len(listanotas)):
        listanotas[i] = float(listanotas[i])
        for j in range(len(listatrabajos)):
            listatrabajos[j] = float(listatrabajos[j])
            for x in range(len(listateoricas)):
                listateoricas[x] = float(listateoricas[x])
                for y in range(len(listadesarrollos)):
                    listadesarrollos[y] = float(listadesarrollos[y])
                    for g in range(len(listaponderados)):
                        listaponderados[g] = float(listaponderados[g])
    print(listanotas), print(listatrabajos), print(listateoricas), print(listadesarrollos), print(listaponderados)

print(f"El promdio general es: {round(promedioG,2)}")
print(f"El ponderado mayor pertenece a {mayor_nombre}: {mayor}")
print(f"El ponderado menor pertenece a {menor_nombre}: {menor}")

    
