nombre = "tichard"
for i in range(len(nombre)):
    if i == 0:
        nombre = nombre.replace(nombre[i], "L",1)
print(nombre)
