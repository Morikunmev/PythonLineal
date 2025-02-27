def validacion(bucle, registro):
    if registro == 3:
        return False
    return bucle
    
def nombredef(nombre, apellido):
    while bucle:
        nombre1 = input(nombre)
        while nombre1.isnumeric() or any(i.isnumeric() for i in nombre1) or not nombre1.isalpha() or nombre1.count(" ")>=1:
            nombre1 = input(nombre)
            
        apellido1 = input(apellido)
        while apellido1.isnumeric() or any(i.isnumeric() for i in apellido1) or not apellido1.isalpha() or apellido1.count(" ") >=1:
            apellido1 = input(apellido)
            
        return nombre1.capitalize(), apellido1.capitalize()

def limitedef(bucle):
    while bucle:
        try:
            edad = int(input(f"Ingrese su edad {registro}/3: "))
            while not 15<=edad<=100:
                edad = int(input(f"Ingrese su edad {registro}/3: "))
                
            altura = float(input(f"Ingrese su altura {registro}/3: "))
            while not 1.00<=altura<=3.00:
                altura = float(input(f"Ingrese su altura {registro}/3: "))
            return edad, altura
        except ValueError:
            continue
        
def notasdef(bucle):
    while bucle:
        try:
            nota = float(input(f"Ingresa la nota nro {i+1} / 3:"))
            if 1.0<=nota<=7.0:
                return nota
        except ValueError:
            continue
def controldef(suma):
    promedio = (suma / 3) * 0.1
    return round(promedio,2)
def calculo():
    while bucle:
        try:
            trabajo = float(input("Ingrese la nota del trabajo: "))
            while not 1.0<=trabajo<=7.0:
                trabajo = float(input("Ingrese la nota del trabajo: "))           
            teorica = float(input("Ingrese la nota de la teorica: "))
            while not 1.0<=teorica<=7.0:
                teorica = float(input("Ingrese la nota de la teorica: "))
            desarrollo = float(input("Ingrese la nota del desarrollo: "))
            while not 1.0<=desarrollo<=7.0:
                desarrollo = float(input("Ingrese la nota del desarrollo: "))
            return trabajo, teorica, desarrollo
        except ValueError:
            continue
def calculo1(trabajo, teorica, desarrollo):
    trabajo1 = round(trabajo * 0.2, 2)
    teorica1 = round(teorica * 0.3, 2)
    desarrollo1 = round(desarrollo * 0.4, 2)
    return trabajo1, teorica1, desarrollo1

def ponderadodef(promedio, trabajo, teorica, desarrollo):
    return promedio + trabajo + teorica + desarrollo

def mayordef(mayor, ponderado):
    if ponderado > mayor:
        return ponderado
    else:
        return mayor

def menordef(menor, ponderado):
    if ponderado < menor:
        return ponderado
    else:
        return menor

registro = 0
bucle = True

nombres = ""
apellidos = ""

edades = ""
alturas = ""

ponderados = ""
suma1 = 0
mayor = 0
menor = 7.0


while validacion(bucle, registro):
    registro+= 1
    nombre, apellido = nombredef(f"Ingrese su nombre: {registro}/3: ", f"Ingrese su apellido: {registro}/3: ")

    nombres+= nombre + ", "
    nombres = nombres.replace(",","")
    listanombres = nombres.split()
    print(listanombres)
    
    apellidos+=apellido + ", "
    apellidos = apellidos.replace(",","")
    listaapellidos = apellidos.split()
    print(listaapellidos)

    edad, altura = limitedef(bucle)
    edad, altura = str(edad), str(round(altura,2))
    
    edades += edad + " "
    listaedades = edades.split()
    listaedades = [int(i) for i in listaedades]

    alturas+=altura + " "
    listaalturas = [float(i) for i in alturas.split()]
    print(listaalturas)

    suma = 0
    for i in range(3):
        nota = notasdef(bucle)
        suma+= nota
    promedio = controldef(suma)
    print(f"El promedio del 10% ponderado del alumno {nombre} {apellido} es {promedio}")

    trabajo, teorica, desarrollo = calculo()
    trabajo, teorica, desarrollo = calculo1(trabajo, teorica, desarrollo)
    print(f"la nota del trabajo del 20% corresponde a: {trabajo}")
    print(f"la nota de la teorica del 30% corresponde a: {teorica}")
    print(f"la nota del desarrollo del 40% corresponde a: {desarrollo}")
    ponderado = ponderadodef(promedio, trabajo, teorica, desarrollo)
    ponderado = round(ponderado,2)

    mayor = mayordef(ponderado, mayor)
    menor = menordef(ponderado, menor)
    
    suma1+=ponderado
    print(f"El ponderado del alumno {nombre} {apellido} es: {ponderado}")
    ponderado = str(ponderado)
    ponderados+=ponderado + " "
    listaponderado = ponderados.split()

    
print("el promedio de los 3 alumnos es: {}".format(round(suma1 / 3,1)))
print("El maximo ponderado es: {}".format(round(mayor,2)))
print("El minimo poderado es: {}".format(round(menor,2)))
    
    
    
    

    


    
    
