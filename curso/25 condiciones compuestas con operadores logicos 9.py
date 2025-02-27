#dada una lista de tres valores numericos distintos se calcula e informa su
#rango de variacion (debe mostrar el mayor y el menor de ellos)


def menor(n1,n2,n3):
    if n1<n2 and n1<n3:
        return n1
    elif n2 <n1 and n2<n3:
        return n2
    else:
        return n3
    
def mayor(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else:
        return n3

n1,n2,n3 = int(input("Ingresa: ")), int(input("Ingresa: ")), int(input("Ingresa: "))
print("El mayor es: "+str(mayor(n1,n2,n3)))
print("El menor es: "+str(menor(n1,n2,n3)))

