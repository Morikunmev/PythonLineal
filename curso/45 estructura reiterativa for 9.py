def validar(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if 1<=num<=10 or num != float(num):
                return num
            else:
                continue
        except ValueError:

            continue

while True:
    num = validar("Ingrese un numero entre el 1 y el 10: ")
    for i in range(1,13):
        print(f"{i} x {num} = {i*num}")
