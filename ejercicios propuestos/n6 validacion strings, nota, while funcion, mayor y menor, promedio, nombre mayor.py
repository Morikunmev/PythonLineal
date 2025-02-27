def salirdef(bucle,registro):
    if registro == 3:
        return False
    return True
def validar(nombre):
    while True:
        string =input(nombre)
        for i in string:
            if i in ["@","!","#","-"] or i.isnumeric() or any(i.isnumeric() for i in string) or string.count(" ")>=1:
                continue
            return string.capitalize()
def notadef(nota):
    while True:
        try:
            flotante = float(input(nota))
            if 1.0<= flotante<=7.0:
                return flotante
        except ValueError:
            continue

def mayordef(promedio, mayor):
    if promedio > mayor:
        return promedio
    else:
        return mayor
def menordef(promedio, menor):
    if promedio < menor:
        return promedio
    else:
        return menor
    
#variables mayores y menores
mayor = 0
menor = 7.0

#bucle infinito y acumulador de registro
bucle = True
registro = 0
#variables acumuladoras
nombres = ""
promedios = ""
#variables convertidas
convertido1 = ""
convertido2 = ""
#nombre mayor y menor
mayor_nombre = ""
menor_nombre = ""

while salirdef(bucle,registro):
    registro +=1
    nombre = validar(f"Ingrese nombre nro {registro}: ")
    nombres+=nombre + " "
    convertido1 = nombres.split()
    print(convertido1)
    suma = 0
    for i in range(3):
        nota = notadef(f"Ingrese su nota nro {i+1} /3: ")
        suma += nota
    promedio = suma / 3

    mayor = mayordef(promedio, mayor)
    if mayor == promedio:
        mayor_nombre = nombre
    menor = menordef(promedio, menor)
    if menor == promedio:
        menor_nombre = nombre
    

    promedio = str(round(promedio,1))
    promedios+= promedio + " "
    convertido2 = promedios.split()
    print(convertido2)
    

print(f"El promedio mayor fue {round(mayor,1)} que pertenece al nombre {mayor_nombre}")
print(f"El promedio menor fue {round(menor,1)} que pertenece al nombre {menor_nombre}")
    
    
