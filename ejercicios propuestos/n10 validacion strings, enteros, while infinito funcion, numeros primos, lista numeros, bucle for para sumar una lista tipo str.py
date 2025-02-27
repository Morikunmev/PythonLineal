def validacion():
    while True:
        nombre = input("Ingrese un nombre: ")
        for i in nombre:
            if i.isnumeric() or any (i.isnumeric() for i in nombre) or not i.isalpha() or nombre.count(" ")>=1:
                continue
            return nombre.capitalize()

def enterosdef():
    while True:
        try:
            entero = int(input("Ingrese un numero: "))
            if entero <=0 or not 1<=entero<=100:
                continue
            return entero
        except ValueError:
            continue

        
def salirdef(bucle,registro):
    if registro == 5:
        return False
    return True

def primo(numero):
    if numero <2:
        return False
    for i in range(2,numero):
        if numero %i == 0:
            return False
    return True


bucle = True
listanumeros = ""
total_sum = 0
registro = 0

while salirdef(bucle,registro):
    registro+=1
    nombre = validacion()
    print("Nombre ingresado: {}".format(nombre))
    
    numero = enterosdef()
    numero = str(numero)
    listanumeros+=numero + " "
    convertido = listanumeros.split()
    print(convertido)


for i in convertido:
    total_sum+= int(i)
print(f"La suma de todos los valores: {total_sum}")

y = 0
while y<len(convertido):
    if primo(int(convertido[y])):
        convertido.pop(y)
    else:
        y+=1
print("Eliminacion de numeros primos: ")
print(convertido)
    
    
