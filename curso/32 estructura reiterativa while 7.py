def validar():
    while True:
        try:
            num = int(input("Ingrese la cantidad de empleados: "))
            if num <=0:
                print("No puede ingresar valores negativos o iguales a 0")
            else:
                return num
        except ValueError:
            continue
def validar1():
    while True:
        try:
            sueldo = int(input("Ingrese el sueldo del empleado: "))
            return sueldo
        except ValueError:
            continue
def sueldodef(sueldo):
    return 100<=sueldo<=300
def sueldodef1(sueldo):
    return sueldo>300

empleados = validar()
i = 1
contador = 0
contador1 = 0
contador2 = 0

while i<= empleados:
    sueldo = validar1()
    if sueldodef(sueldo):
        contador += 1
    elif sueldodef1(sueldo):
        contador1 += 1
    contador2 += sueldo
    i +=1
        
print(f"el sueldo de {empleados} empleados que cobran entre 100 y 300 es: {contador}")
print(f"El sueldo de {empleados} empleados que cobran mas de 300 es: {contador1}")
print(f"el importe que gasta la empresa de los {empleados} empleados es {contador2}")
    
    
