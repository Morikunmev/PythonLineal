def salirdef():
    if numeros>=1:
        desicion = input("Quieres ingresar mas?")
        if desicion.lower() in ["no","n"]:
            return False
    return bucle
def ingresodef():
    while bucle:
        cadena = input(f"Ingresa numero {numeros}: ")
        if cadena.isnumeric():
            return cadena
        else:
            continue
def opciondef(operacion,lista):
    n1 = "la suma es: "
    n2 = "la resta es: "
    n3 = "la multiplicacion es: "
    n4 = "la division es: "
    n5 = "No se pueden hacer divisiones entre 0"
    while bucle:
        opcion = input("Quieres?:\n"
                       "1. Sumar\n"
                       "2. restar\n"
                       "3. Multiplicar\n"
                       "4. Dividir\n"
                       "R: ")
        if opcion == "1":
            
            for i in range(len(lista)):
                operacion+=lista[i]
            return n1, operacion
        
        elif opcion == "2":
            resultado = lista[0]
            for i in lista[1:]:
                lista[0]-=i
            return n2, lista[0]
        
        elif opcion == "3":
            operacion = 1
            for i in range(len(lista)):
                operacion*=lista[i]
            return n3, operacion
        
        elif opcion == "4":
            resultado = lista[0]
            for i in lista[1:]:
                if i == 0:
                    return n5
                resultado/=i
            return n4, resultado
        else:
            continue
    


bucle = True
numeros = 0
strnumero = ""
lista = ""
numero = ""


#variables operadoras matematicas
operacion = 0

while salirdef():
    numeros+=1
    numero = ingresodef()
    strnumero+=numero+" "
    lista = strnumero.split()
    print("Ingresos")
    print(lista)

    
print("Ingreso Finales:")
for i in range(len(lista)):
    lista[i] = int(lista[i])
print(lista)

mensaje, opcion = opciondef(operacion,lista)
print(mensaje),print(opcion)
