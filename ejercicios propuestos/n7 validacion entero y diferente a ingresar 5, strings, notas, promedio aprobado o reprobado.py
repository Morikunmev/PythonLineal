def diez():
    while True:
        try:
            num = int(input("Ingresa 5 cantidades: "))
            if num !=5:
                continue
            return num
        except ValueError:
            continue

def validar():
    while True:
        nombre = input(f"Ingrese nombre del alumno {i+1}/{n}: ")
        for y in nombre:
            if y.isnumeric() or any(y.isnumeric() for y in nombre) or not nombre.isalpha() or nombre.count(" ")>=1:
                continue
            return nombre.capitalize()
def notasdef():
    while True:
        try:
            nota = float(input(f"Ingrese la nota {x+1}/{3}: "))
            if 1.0<=nota<=7.0:
                return nota
        except ValueError:
            continue
def reprobadodef(promedio):
    return promedio<4.0

#lista de nombre
nombres = ""
#lista de nombre #2
nombrelista = ""
#contador de reprobado
reprobado = 0
#contador de aprobado
aprobado = 0
#alumnos aprobados
alumnoa = ""
#alumno reprobado
alumnob = ""
#convertido
con = ""
ja = ""


#CODIGO PRINCIPAL
n = diez()
for i in range(n):
    nombre = validar()
    nombres+= nombre + " "
    nombrelista = nombres.split()
    print(nombrelista)
    
    suma = 0
    for x in range(3):
        nota = notasdef()
        suma +=nota
    promedio = suma / 3
    print(round(promedio,1))
    if reprobadodef(promedio):
        reprobado += 1
        alumnob+= nombre + " "
        con = alumnob.split()
    else:
        aprobado += 1
        alumnoa+= nombre + " "
        ja = alumnoa.split()
        
print(f"{aprobado} alumnos han aprobado")
print(ja)
print(f"{reprobado} alumnos han reprobado")
print(con)
        
        
