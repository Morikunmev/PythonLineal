def enterodef():
    while True:
        try:
            num = int(input("Ingresa un numero: "))
            if num <= 0:
                continue
            return num
        except ValueError:
            continue

def salirdef(salir, registro):
    if registro == 10:
        return False
    return True
    
def multiplo2(numero):
    if numero %2 == 0:
        return numero
    
def primo(numero):
    if numero <2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

salir = True
multi2 = " "
primos = " " 
registro = 0

while salirdef(salir, registro):
    registro+=1
    numero = enterodef()
    if multiplo2(numero):
        print("Numeros multiplos de 2")
        numero = str(numero)
        multi2+= numero + " "
        lista2 = multi2.split()
        print(lista2)
        numero = int(numero)
        
    if primo(numero):
        print("Numeros primos")
        numero = str(numero)
        primos+= numero + " "
        lista3 = primos.split()
        print(lista3)
        numero = int(numero)


print("Listas vacias!")

x = 0
while x<len(lista2):
    if multiplo2(int(lista2[x])):
        lista2.pop(x)
    else:
        x+= 0
print(lista2)

i = 0
while i<len(lista3):
    if primo(int(lista3[i])):
        lista3.pop(i)
    else:
        i+=1
print(lista3)




    
    
