def cantidad(verdadero):
    while verdadero:
        try:
            numero = int(input("Ingresa la cantidad a evaluar: "))
            if numero<=0 or not 1<=numero<=10:
                continue
            return numero
        except ValueError:
            continue
def validar(verdadero):
    while verdadero:
        nombre = input(f"Ingrese el nombre del producto nro {i+1}: ")
        if nombre.isnumeric() or any(i.isnumeric() for i in nombre) or nombre.count(" ")>=1 or not nombre.isalpha():
            continue
        return nombre.capitalize()
    
def stocksdef(verdadero):
    while verdadero:
        try:
            stock = int(input(f"Ingrese la cantidad de {listanombres[i]}: "))
            if stock <=0:
                continue
            return stock
        except ValueError:
            continue
def preciodef(verdadero):
    while True:
        try:
            dinero = int(input(f"Ingrese el precio por unidad de {listanombres[i]}: "))
            if dinero<=0:
                continue
            return dinero
        except ValueError:
            continue
def valordef(precio,stock):
    precio,stock = int(precio), int(stock)
    calculo = precio * stock
    return calculo

def disponibledef(stock):
    stock = int(stock)
    if stock<10:
        return stock


#variables
verdadero = True
#listas de strings
productos = ""
stocks = ""
precios = ""
valors = ""
disponibles = ""


n = cantidad(verdadero)
for i in range(n):
    
    producto = validar(verdadero)
    productos+= producto + " "
    #conversion
    listanombres = productos.split()
    print(listanombres)

    stock = stocksdef(verdadero)
    stock = str(stock)
    stocks+= stock + " "
    listastocks = stocks.split()
    print(listastocks)

    precio = preciodef(verdadero)
    precio = str(precio)
    precios+= "$" + precio + " "
    listaprecios = precios.split()
    print(listaprecios)

    valor = valordef(precio,stock)
    print(f"El precio de {listanombres[i]} es: {valor}")
    valor = str(valor)
    valors+= "$" + valor + " "
    listafinal = valors.split()
    print(listafinal)

    if disponibledef(stock):
        disponibles+= "agotandose" + " "
        listadodisponibles = disponibles.split()
    else:
        disponibles+= "ok" + " "
        listadodisponibles = disponibles.split()
        
    print(f"estado: {listadodisponibles[i]}")
        
if n == 10:
    print("estado de los 10 registros")
    for i in range(n):
        print(f"producto nro {i+1}: {listanombres[i]}, precio final: {listafinal[i]}, estado: {listadodisponibles[i]} ")
print()
i = 0
contador = 0
while i<len(listadisponibles) and contador <2:
    if listadodisponibles[i] == "ok":
        print(f"nombre: {listanombres[i]} {listadodisponibles[i]}")
        contador+=1
    i+= 1
