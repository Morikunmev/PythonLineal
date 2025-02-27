numeros = "22 22 22 22"
numeros = numeros.split()
nummeros = [int(i) for i in numeros]
print(numeros)
numeros = list(numeros)
numeros = [int(i) for i in numeros]
print(numeros[0] + numeros[1])
print()
numeros1 = "22 23.44 44-4 444"
for i in numeros1:
    numeros1 = numeros1.replace(".", "").replace("-","")
    
numeros1 = numeros1.split()
numeros1 = [int(i) for i in numeros1]
print(numeros1)
print(len(numeros1))
print(numeros1[0] + numeros1[1])
