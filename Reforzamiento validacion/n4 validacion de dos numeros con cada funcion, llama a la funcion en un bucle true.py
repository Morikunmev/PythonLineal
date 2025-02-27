def validacion(n1):
    return 1<= n1 <=10

def validacion1(n2):
    return 11<= n2 <= 20


n1 = int(input("Ingresa un numero entre 1 y 10: "))
n2 = int(input("Ingresa otro numero entre 11 y 20: "))

while True:
    if validacion(n1):
        print("Validado")
        break
    else:
        n1 = int(input("Ingresa un numero entre 1 y 10: "))
        
while True:
    if validacion1(n2):
        print("Validado")
        break
    else:
        n2 = int(input("Ingresa otro numero entre 11 y 20: "))
        
        
