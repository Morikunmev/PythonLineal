def primo(numero):
    if numero <2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True


lista = [2,3,5,2,4]

i = 0

while i<len(lista):
    if primo(lista[i]):
        lista.pop(i)
    else:
        i+=1
print(lista)
