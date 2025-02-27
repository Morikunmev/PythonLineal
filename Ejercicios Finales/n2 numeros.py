def primo(numero):
    if numero <2:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True


numeros = "28, 28, 348 483 29 29 4 04"
numeros = numeros.replace(".","").replace(",","").split()
numeros = [int(i) for i in numeros]
print(numeros)
numeros = [num for num in numeros if not primo(num)]
print(numeros)
print()
numeros1 = "1 2 3 4 5 6"
numeros1 = numeros1.split()
numeros1 = [int(i) * 2 for i in numeros1]
numeros1 = [i for i in numeros1 if not i %2 == 0]
print(numeros1)

numeros = [str(i) for i in numeros]
print(numeros)

lista = [2,3,54,5,4,3]

i = 0
while i < len(lista):
    if primo(lista[i]):
        lista.remove(lista[i])
    else:
        i+=1
print(lista)
print()
x=0
lista1 = [2,3,4,3,5,6,3,3]

acumulador = ""
while True:
    numero0 = input("Ingresa: ")
    while numero0.isalpha() or any(i.isalpha() for i in numero0):
        numero0 = input("Ingresa: ")
    prueba = input("Ingresa OTRO: ")
    if prueba.isalpha() or any(i.isalpha() for i in prueba):
        continue
    print("PERFECTO")
    acumulador+=numero0 + " "
    listaa = acumulador.split()
    listaa = [int(i) for i in listaa]
    listaa = listaa * (2)
    for i in listaa[:]:
        if i % 2 == 0:
            listaa.remove(i)
    print(listaa)


acumulador = ""
while True:
    cadena = input("Ingresa: ")
    acumulador+= cadena + ","
    nueva_cadena = ""
    
    for i in acumulador:
        if i == ",":
            nueva_cadena += " "
        else:
            nueva_cadena += i
    
    print(nueva_cadena)

    

acumulador = ""
entero = 0
while True:
    numero = input("Ingresa: ")
    acumulador+= numero + " "
    acumulador = acumulador.replace(acumululador.isalpha, " ")
    print(acumulador)


numero1 = "5,5,5,5,5,5"
numero2="1,2,3,4,5,6"
numero3="2,4,5,4,2,4"
n1 = 0
n2 = 0
n3 = 0
numero1 = numero1.replace(","," ")
numero2 = numero2.replace(",","")
numero3= numero3.replace(",","")


    for j in range(len(numero2)):
        numero2[j] = int(numero2[j])
        for x in range(len(numero3)):
            numero3[x] = int(numero3[x])
            
print(numero1),print(numero2),print(numero3)

for i in numero1:
    n1+=i
for x in numero2:
    n2+= x
for j in numero3:
    n3+=j
print(), print(n1), print(n2), print(n3)


Eliminar la , por medio de un for, en vez de usar el replace
ac = ""
da = "1,2,2,2,22"
for i in range(len(da)):
    if da[i] == ",":
        ac+= " "
    else:
        ac+= da[i]
print(ac)
        
