def salirdef(opcion):
    if opcion.lower() in ["si","s"]:
        return False
    return bucle

def empresadef():
    while bucle:
        empresa = input("Ingresa el nombre de la empresa: ")
        while empresa.isnumeric() or any(i.isnumeric() for i in empresa) or empresa.count(" ")>=1 or not empresa.isalpha():
            empresa = input("Ingresa el nombre de la empresa: ")
            
        tipo = input("Es publico o privada: ")
        while tipo.isnumeric() or any(i.isnumeric() for i in tipo) or tipo.count(" ")>=1 or not tipo.isalpha() or not tipo.lower() in ["publico", "privada"]:
            tipo = input("Es publico o privada: ")
            
        producto = input("Ingrese el nombre del producto: ")
        while producto.isnumeric() or any (i.isnumeric() for i in producto) or producto.count(" ")>=1 or not producto.isalpha():
            producto = input("Ingrese el nombre del producto: ")
            
        return empresa.capitalize(), tipo.capitalize(), producto.capitalize()
def cantidaddef():
    n1 = "la cantidad ingresada es:"
    n2 = "El precio ingresado es:"
    n3 = "El precio por unidad es:"
    while bucle:
        try:
            entero = int(input(f"Ingrese las cantidades de {productos}: "))
            while entero<=0:
                entero = int(input(f"Ingrese las cantidades de {productos}: "))

            precio = int(input(f"Ingrese el precio del producto {productos}: "))
            while precio<=0:
                precio = int(input(f"Ingrese el precio del producto {productos}: "))

            calculo = entero * precio

            return n1,entero,n2,precio,n3,calculo

                
        except ValueError:
            continue
    
bucle = True
registro = 0

empresas = ""
tipos = ""
productos = ""

while salirdef(opcion = input("se han terminado los productos?: ")):
    registro+=1
    print(f"registro nro {registro}")
    empresa, tipo, producto = empresadef()
    print()
    
    empresas+= empresa + " "
    listaempresa = empresas.split()
    print(f"LISTA EMPRESAS:\n{listaempresa}")

    tipos+=tipo
    listatipo = tipos.split()
    print(f"LISTA TIPOS:\n{listatipo}")

    productos+=producto + " "
    listaproducto = productos.split()
    print(f"LISTA PRODUCTO:\n{listaproducto}")

    print()
    mensaje1, cantidad,mensaje2,producto,mensaje3,calculo = cantidaddef()
    print(mensaje1,cantidad)
    print(mensaje2,"$",producto)
    print(mensaje3,"$",calculo)

    

    

    

    
    
    

    
