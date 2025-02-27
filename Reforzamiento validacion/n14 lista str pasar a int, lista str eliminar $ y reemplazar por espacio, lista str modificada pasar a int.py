print()
listastocks = [int(i) for i in listastocks]
print(listastocks)

for x in range(len(listaprecios)):
    listaprecios[x] = listaprecios[x].replace("$","")
listaprecios = [int(i) for i in listaprecios]

for y in range(len(listafinal)):
    listafinal[y] = listafinal[y].replace("$","")
print(listafinal)
