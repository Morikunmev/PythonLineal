def salirdef(bucle):
    return bucle


bucle = True
contador = ""
registro = ""


while salirdef(bucle):
    contador+="1" + " "
    lista = contador.split()
    lista = len(lista)
    lista = str(lista)

    registro+=lista + " "
    lista1 = registro.split()
    for i in range(len(lista1)):
        lista1[i] = int(lista1[i])
    print(lista1)
    
