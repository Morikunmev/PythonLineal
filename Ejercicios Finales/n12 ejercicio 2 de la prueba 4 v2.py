def bucledef():
    if len(contador2) >=1:
        opcion = input("Quieres ingresar mas?: ")
        if opcion.lower().strip() in ["no","n"]:
            return False
    return bucle
    
def productodef():
    while bucle:
        producto = input(f"Ingrese el nombre del producto nro {i+1}: ")
        if producto.isnumeric() or any(i.isnumeric() for i in producto) or producto.count(" ")>=1 or not producto.isalpha():
            continue
        return producto.capitalize()
def calculodef():
    n1 = "La cantidad es:"
    n2 = "el precio es:"
    n3= "el precio total es:"
    while bucle:
        try:
            stock = int(input(f"Ingrese la cantiad de {listaproducto[i]}: "))
            while stock<=0:
                stock = int(input(f"Ingrese la cantiad de {listaproducto[i]}: "))
            precio = int(input(f"Ingrese el precio por unidad de {listaproducto[i]}: "))
            while precio<=0:
                precio = int(input(f"Ingrese el precio por unidad de {listaproducto[i]}: "))
            calculo = stock * precio
            
            return n1,stock, n2,precio, n3,calculo
        except ValueError:
            continue
def disponibledef(stock):
    stock = int(stock)
    if stock<10:
        return stock

bucle = True
#str contador
contador = ""
contador0 = ""

contador1 = ""
contador2 = ""
#variables contadoras
productos = ""
stocks = ""
precios = ""
calculos = ""
#variables de disponibles
disponibles = ""
listadisponibles = ""

while bucledef():
    contador+= "1" + " "
    contador0 = contador.split()
    contador0 = len(contador0)
    contador0 = str(contador0)

    contador1+=contador0 + " "
    contador2 = contador1.split()
    for i in range(len(contador2)):
        contador2[i] = int(contador2[i])
    
    print(f"Registro nro: {contador0}")
    print(f"Lista de registro: {contador2}")

    producto = productodef()
    productos+=producto + " "
    listaproducto = productos.split()
    print(listaproducto)

    n1,stock, n2,precio, n3,calculo = calculodef()
    print(n1,stock)
    print(n2,precio)
    print(n3,calculo)

    stock = str(stock)
    stocks+=stock + " "
    listastocks = stocks.split()
    print(listastocks)
    
    precio = str(precio)
    precios+="$" +precio + " "
    listaprecios = precios.split()
    print(listaprecios)

    calculo = str(calculo)
    calculos+="$" + calculo + " "
    listacalculo = calculos.split()
    print(listacalculo)

    if disponibledef(stock):
        disponibles+="Agotandose" + " "
        listadisponibles = disponibles.split()
    else:
        disponibles+="Ok" + " "
        listadisponibles = disponibles.split()
    print(f"Estado: {listadisponibles[i]}")


print(f"Estado de los {contador0} registros")
for i in range(len(contador2)):
    print(f"Nombre: {listaproducto[i]}, stock: {listastocks[i]}, precio: {listaprecios[i]}, preciofinal: {listacalculo[i]}, estado: {listadisponibles[i]}")

print()
print("ESTADOS DISPONIBLES")
i = 0
contador = 0
while i <len(contador2) and contador < 2:
    if listadisponibles[i] == "Ok":
        print(f"Nombre: {listaproducto[i]}, estado: {listadisponibles[i]}")
        contador+=1
    i+=1

    



