def primo(numero):
    if numero <2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True
numero = "2,49.2,4,5,3.4"
numero = numero.replace(","," ").replace("."," ")
print(len(numero))
numero = numero.split(" ")
print(numero)
print(len(numero))

for i in range(len(numero)):
    numero[i] = int(numero[i])
for i in range(len(numero)):
    numero[i] = str(numero[i])

print(numero)
for i in range(len(numero)):
    numero[i] = numero[i].replace("", "$",1)

for i in range(len(numero)):
    numero[i] = numero[i].replace("$","")

for i in range(len(numero)):
    numero[i] = int(numero[i])

    
for i in numero[:]:
    if primo(i):
        numero.remove(i)

print(numero)
