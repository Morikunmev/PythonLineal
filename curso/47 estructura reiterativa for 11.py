def validar(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if num<=0:
                continue
            else:
                return num
        except ValueError:
            continue

def coordenadas():
    while True:
        try:
            x = int(input("Ingrese la coordenada x: "))
            y = int(input("Ingrese la coordenada y: "))
            return x, y
        except ValueError:
            continue
def primer(x,y):
    if x>0 and y>0:
        return x, y
def segundo(x,y):
    if x<0 and y>0:
        return x, y
def tercer(x,y):
    if x<0 and y<0:
        return x,y
def cuarto(x,y):
    if x>0 and y<0:
        return x,y

cantidad1 = 0
cantidad2 = 0
cantidad3 = 0
cantidad4 = 0
cantidad5 = 0
        
cantidad = validar("Ingresa la cantidad de puntos a procesar: ")
for i in range(cantidad):
    print(f"Coordenada {i+1}/{cantidad}")
    x, y = coordenadas()
    if primer(x,y):
        print("Pertenece al primer cuadrante")
        cantidad1 += 1
    elif segundo(x,y):
        print("Pertenece al segundo cuadrante")
        cantidad2 += 1
    elif tercer(x,y):
        print("Pertenece al tercer cuadrante")
        cantidad3 += 1
    elif cuarto(x,y):
        print("Pertenece al cuarto cuadrante")
        cantidad4 += 1
    else:
        print("La pendiente esta sobre el eje")
        cantidad5 += 1
print(f"primer cuadrante: {cantidad1}")
print(f"segundo cuadrante: {cantidad2}")
print(f"Tercer cuadrante: {cantidad3}")
print(f"Cuarto cuadrante: {cantidad4}")
print(f"Sobre el eje: {cantidad5}")

    
