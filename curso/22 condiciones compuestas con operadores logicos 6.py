#Se Ingresan 3 valores por teclado,
#si todos son iguales se imprime la suma del primero con el segundo,
#y a este resultado se lo multiplica por el tercero

def suma1(n1,n2,n3):
    if n1 == n2 and n1 == n3:
        suma = n1 + n2
        return suma
    
def producto(n1,n2,n3):
    if n1 == n2 and n1 == n3:
        suma = n1 + n2
        producto = suma * n3
        return producto
    
n1, n2, n3 = int(input("Ingresa: ")), int(input("Ingresa: ")), int(input("Ingresa: "))
if suma1(n1,n2,n3) and producto(n1,n2,n3):
    print("la suma de los dos primeros numeros es: "+str(suma1(n1,n2,n3)))
    print("El producto de la suma y el ultimo numero es: "+str(producto(n1,n2,n3)))
