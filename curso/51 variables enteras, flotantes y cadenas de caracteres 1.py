def nombredef():
    while True:
        try:
            nombre = input("Ingrese el nombre: ")
            if nombre.isnumeric() or any(i in ["@","#","!"] for i in nombre):
                continue
            else:
                return nombre.capitalize().strip()
        except ValueError:
            continue
def edaddef():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if 1<edad<=150:
                return edad
        except ValueError:
            continue
def alturadef():
    while True:
        try:
            altura = float(input("Ingrese su altura: "))
            if 1.00<= altura<=2.72:
                return altura
            else:
                print("Esa altura no puede ser posible: ")
        except ValueError:
            continue
def mayordef(altura,mayor):
    if altura > mayor:
        return altura
    else:
        return mayor
    
def menordef(altura, menor):
    if altura<menor:
        return altura
    else:
        return menor

menor = 2.72
mayor = 1.00

for i in range(2):
    nombre = nombredef()
    print("Nombre ingresado: {}".format(nombre))
    edad = edaddef()
    print("Edad ingresada: {}".format(edad))
    altura = alturadef()
    print("Altura ingresada: {}".format(altura))
    
    mayor = mayordef(altura, mayor)
    menor = menordef(altura, menor)

print(f"la mayor altura es: {mayor}")
print(f"la menor altura es: {menor}")
