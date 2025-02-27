def nombredef():
    while True:
        nombre = input("Ingrese un mail: ")
        if "@" in nombre and nombre.count("@") == 1 and not any(i.isnumeric() for i in nombre):
            return nombre
        else:
            continue
def conversiondef(mail):
    if "@" in mail:
        nombre, dominio = mail.split("@")
        convertido = nombre + "@inacap.cl"
        return convertido

while True:
    mail = nombredef()
    convertido = conversiondef(mail)
    print(convertido)
