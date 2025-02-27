registro = ""
registro1 = ""

while True:
    registro+= "1" + " "
    lista = registro.split()
    lista = len(lista)
    lista = str(lista)
    print(f"numero : {lista}")

    registro1+=lista+ " "
    lista1 = registro1.split()
    for i in range(len(lista1)):
        lista1[i] = int(lista1[i])
    print(f"LISTA: {lista1}")
