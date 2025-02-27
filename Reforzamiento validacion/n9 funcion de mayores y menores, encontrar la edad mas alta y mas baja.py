def mayordef(edad,mayor):
    if edad>mayor:
        return edad
    else:
        return mayor
def menordef(edad, menor):
    if edad<menor:
        return edad
    else:
        return menor

mayor = 0
menor = 100
for i in range(5):
    edad = int(input("Ingrese su edad: "))
    mayor = mayordef(edad,mayor)
    menor = menordef(edad,menor)
print(f"La edad mas alta ingresada es: {mayor}")
print(f"La edad mas baja ingresada es: {menor}")
