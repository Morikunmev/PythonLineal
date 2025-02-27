#Se ingresan 3 numeros. si al menos uno de los valores ingresados es menor a 10.
#imprimir en pantalla "Algunos de los numeros es menor a diez"

def valid(n1,n2,n3):
    return n1 <10 or n2 <10 or n3<10
n1, n2, n3 = int(input("Ingresa ")),int(input("Ingresa ")),int(input("Ingresa "))

if valid(n1,n2,n3):
    print("Algunos de los numeros es menor a diez")

    


                                                    
