def enteros(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            break
        except ValueError:
            print("Ingresa un numero entero: ")
    return numero

def strings (mensaje1):
    while True:
        string = input(mensaje1)
        if string.isnumeric():
            print("No puede ingresar valores numericos: ")
        elif string in ["@", "#"]:
            print("No puede ingresar esos caracteres!")
        else:
            break
    return string

def gratificaciondef(sueldo, grat = 0.25):
    calculo = sueldo * (1+grat)
    return calculo



nombres = []
apellidos = []
registros = []
sueldos = []
gratificaciones = []

n = enteros("Ingresa la cantidad de pesonas a evaluar: ")

for i in range(n):
    registros.append(i+1)
    nombre = strings(f"Ingrese el nombre del trabajador {i+1}/{n}: ").capitalize()
    nombres.append(nombre)
    print("-"*20)
    apellido = strings(f"Ingrese el apellido del trabajador {i+1}/{n}: ").capitalize()
    apellidos.append(apellido)
    print("-"*20)
    sueldo = enteros(f"Ingrese el sueldo del trabajador {nombres[i]}: ")
    sueldos.append(sueldo)
    print("-"*20)
    gratificacion = gratificaciondef(sueldo, grat = 0.25)
    print(f"El sueldo imponible del 25% del trabajador {nombres[i]} {apellidos[i]} es: ")
    gratificaciones.append(gratificacion)
    print(gratificaciones)


    

