def primerc(x,y):
    return x>0 and y>0
def segundoc(x,y):
    return x<0 and y>0
def tercerac(x,y):
    return x<0 and y<0
def cuartoc(x,y):
    return x>0 and y<0

x, y = int(input("Ingresa la coordenada x: ")), int(input("Ingresa la coordenada y: "))
if primerc(x,y):
    print("Se encuentra en el primer cuadrante")
elif segundoc(x,y):
    print("Se encuentra en el segundo cuadrante")
elif tercerac(x,y):
    print("Se encuentra en el tercer cuadrante")
elif cuartoc(x,y):
    print("Se encuentra en el cuarto cuadrante")
else:
    print("Se encuentra sobre un eje")
