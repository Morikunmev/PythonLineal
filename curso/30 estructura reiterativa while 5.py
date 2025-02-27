def validar():
    while True:
        try:
            num = int(input("Ingrese la nota: "))
            return num
        except ValueError:
            print("Ingrese numeros enteros")

x = 1
menor = 0
mayor = 0

while x <=10:
    print(f"{x}/10")
    nota = validar()
    if nota >=7:
        mayor += 1
    else:
        menor += 1
    x +=1

print("Notas mayores a 7 son: " +str(mayor))
print("Notas menores a 7 son: " +str(menor))

    
    
