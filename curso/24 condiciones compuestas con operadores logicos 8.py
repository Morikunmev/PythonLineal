def primer(sueldo, ant):
    if sueldo <500 and ant>=10:
        aumento = sueldo * (1 + 0.20)
        return aumento
def segundo(sueldo,ant):
    if sueldo<500 and ant<10:
        aumento = sueldo * (1+ 0.05)
        return aumento
def tercero(sueldo):
    if sueldo >=500:
        return sueldo

sueldo, ant = int(input("Ingrese sueldo: ")), int(input("Ingrese antiguedad: "))
if primer(sueldo, ant):
    print("El aumento del 20% es: " +str(primer(sueldo, ant)))
elif segundo(sueldo,ant):
    print("El aumento del 5% es: " +str(segundo(sueldo,ant)))
elif tercero(sueldo):
    print("No se han efectuado cambios: " +str(tercero(sueldo)))

