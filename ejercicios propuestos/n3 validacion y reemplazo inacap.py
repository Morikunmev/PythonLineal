def validar():
    while True:
        nombre = input("Ingrese nombre: ")
        for i in nombre:
            if i in ["@","!","#","-"] or i.isnumeric() or nombre.count(" ") >=1:
                continue
            else:
                return nombre.strip().capitalize()
                
def correodef():
    while True:
        correo = input("Ingrese su correo: ")
        for i in correo:
            if "@" in correo and correo.count("@") == 1 and i.isalpha() and not correo.count(" ")>=1 and not any(i.isnumeric() for i in correo):
                return correo
            else:
                continue
def reemplazo(correo):
    if "@" in correo:
        nombre, dominio = correo.split("@")
        convertido = nombre + "@inacap.cl"
        return convertido.strip()

registros = 0
nombres = ""
correos = ""

while True:
    salir = input("pulse 's' si quiere continuar o 'n' si quiere salir: ")
    if salir.lower() == "n":
        print("Bucle terminado")
        break
    elif salir.lower() != "s":
        continue
    
    nombre = validar()
    nombres+=nombre + " "
    nombrelista = nombres.split()
    print(f"Listado de nombres {len(nombrelista)}: ")
    print(nombrelista)
    
    correo = correodef()
    nuevo = reemplazo(correo)
    correos+=nuevo + " "
    correoslista = correos.split()
    print(f"Correos Ingresados {len(correoslista)}:  ")
    print(correoslista)
    registros+=1
    
for i in range(registros):
    print(i+1, nombrelista[i], correoslista[i])


    
