def salir(bucle, contador):
    if contador== 2:
        return False
    return True
def notasdef():
    while True:
        try:
            nota = float(input(f"Ingrese la nota nro {i+1}/{4} del alumno {contador}: "))
            if 1.0<=nota<=7.0:
                return nota
        except ValueError:
            continue
        
def control(suma):
    return ((suma) /3) * 0.1

def trabajodef(trabajo):
    return trabajo * 0.2

def teoricadef(teorica):
    return teorica * 0.3
def desarrollodef(desarrollo):
    return desarrollo * 0.4

def todo(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 1.0<=nota<=7.0:
                return nota
        except ValueError:
            continue
def mayordef(ponderado,mayor):
    if ponderado > mayor:
        return ponderado
    else:
        return mayor

def menordef(ponderado, menor):
    if ponderado < menor:
        return ponderado
    else:
        return menor
def ponderadodef(promedio, trabajo, teorica, desarrollo):
    return promedio + trabajo + teorica + desarrollo

bucle = True
contador = 0
ponderadoG = 0
mayor = 0
menor = 7.0

while salir(bucle, contador):
    contador+=1
    suma = 0
    for i in range(3):
        nota = notasdef()
        suma+= nota
    promedio = control(suma)
    promedio = round(promedio,1)
    print(f"El promedio del 10% ponderado del alumno {contador} es: {promedio}")
    
    trabajo = todo("Ingresa la nota del trabajo: ")
    trabajo = trabajodef(trabajo)
    trabajo = round(trabajo,1)
    print(f"El trabjado del 20% ponderado del alumno {contador} es: {trabajo}")

    teorica = todo("Ingresa la nota de la teorica: ")
    teorica = teoricadef(teorica)
    teorica = round(teorica,1)
    print(f"la teorica del 30% ponderado del alumno {contador} es: {teorica}")

    desarrollo = todo("Ingresa la nota deel desarrollo: ")
    desarrollo = desarrollodef(desarrollo)
    desarrollo = round(desarrollo,1)
    print(f"el desarrollo del 40% del alumno {contador} es: {desarrollo}")


    ponderado = ponderadodef(promedio, trabajo, teorica, desarrollo)
    ponderado = round(ponderado,1)
    print(f"El ponderado del alumno {contador} es {ponderado}")

    mayor = mayordef(ponderado,mayor)
    menor = menordef(ponderado, menor)

    ponderadoG += ponderado
    ponderadoG = round(ponderadoG,1)
    print(f"Ponderado General: {ponderadoG}")

ponderadoG/=contador
print(f"El promedio del curso es: {ponderadoG}")
print(f"el maximo ponderado es: {mayor}")
print(f"el minimo ponderado es: {menor}")



    
    
    
