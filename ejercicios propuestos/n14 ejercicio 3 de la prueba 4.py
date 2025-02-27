#PRIMER PASO
print("PRIMERO: ")
registro = "1, 2, 3, 4, 5, 6, 7, 8, 9, 10"
registro = registro.replace(",","")
registro = registro.split()

rut = "11.111.111-2, 11.111.222-4, 11.111.111-6, 11.111.111-1, 11.111.222-5, 11.111.111-5, 11.111.111-7, 11.111.111-4, 11.111.111-3, 11.111.222-6"
rut = rut.replace(",","")
rut = rut.split()

apellido = "Vera, Fernandez, Gomez, Mendez, Salas, Barrientos, Soto, Lara, Jara, Jaque"
apellido = apellido.replace(",","")
apellido = apellido.split()

descuento = "0.04, 0.04, 0.03, 0.02, 0.05, 0.10, 0.03, 0.05, 0.05, 0.02"
descuento = descuento.replace(",","")
descuento = descuento.split()
descuento = [float(i) for i in descuento]

cod_carrera = "C001, C002, C001, C003, C004, C004, C005, C002, C001, C003"
cod_carrera = cod_carrera.replace(",","").split()
print()

for i in range(len(registro)):
    print(f"registro nro {registro[i]}, rut: {rut[i]}, apellido: {apellido[i]}, descuento: {descuento[i]}, cod: {cod_carrera[i]}")

print()

#SEGUNDO PASO, DECLARACION DE VARIABLES STR VACIAS

carrera = ""
costo = ""
final = ""

#TERCER PASO, Declaracion de las variables str

unico_cod = "C001, C002, C003, C004, C005"
unico_carrera = "administracion, contador, informatica, mecanica, prevencion"

unico_cod = unico_cod.replace(",","").split()
unico_carrera = unico_carrera.replace(",","").split()


#CUANTO PASO, declaracion de variables str que se pasaran a int

matricula = "$105000, $110000, $125000, $100000, $105000"
mensualidad = "$83500, $80500, $85000, $78000, $75000"

matricula = matricula.replace("$","").replace(",","").split()
matricula = [int(i) for i in matricula]

mensualidad = mensualidad.replace("$","").replace(",","").split()
mensualidad = [int(i) for i in mensualidad]

#QUINTO PASO, AÑADIR VALORES A CADENA CARRERA

carrera = ""

for i in cod_carrera:
    indice = unico_cod.index(i)  # Encuentra el índice correspondiente al i de carrera
    nombre_carrera = unico_carrera[indice]  # Obtiene el nombre de la carrera correspondiente al índice
    carrera += nombre_carrera + ", "


carrera = carrera.replace(",","").split()

#SEXTO PASO, CALCULAR EL COSTO CARRERA QUE CORRESPONDE A UNA MATRICULA Y 10 MENSUALIDADES y CALCULAR EL COSTO FINAL RESTANDO EL COSTO TOTAL CON EL DESCUENTO
#OTRA VEZ
carrera = ""

for i in cod_carrera:
    indice = unico_cod.index(i)  # Encuentra el índice correspondiente al i de carrera
    nombre_carrera = unico_carrera[indice]  # Obtiene el nombre de la carrera correspondiente al índice
    costo_carrera = matricula[indice] + mensualidad[indice] * 10
    costo_final = costo_carrera * (1-descuento[indice]) 

    costo_final = str(costo_final)
    costo_carrera = str(costo_carrera)
    
    carrera += nombre_carrera + ", "
    costo += "$" + costo_carrera + ", "
    final += "$" + costo_final + ", "
    
print("SEGUNDO: ")

carrera = carrera.replace(",","").split()
costo = costo.replace(",","").split()
final = final.replace(",","").split()


#SEPTIMA PARTE, mostrar de formas ascendente por rut

print("TERCERO")

indices_ordenados = sorted(range(len(final)), key=lambda i: float(final[i].replace("$", "")), reverse=True)

for indice in indices_ordenados:
    print(f"registro nro {registro[indice]}, rut: {rut[indice]}, apellido: {apellido[indice]}, "
          f"descuento: {descuento[indice]}, cod: {cod_carrera[indice]}, "
          f"carrera: {carrera[indice]}, costo: {costo[indice]}, final: {final[indice]}")

