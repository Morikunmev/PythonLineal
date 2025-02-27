print("PRIMERO: ")
registro = "1,2,3,4,5,6,7,8,9,10"
registro = registro.replace(","," ")
registro = registro.split()
for i in range(len(registro)):
    registro[i] = int(registro[i])

rut = "11.111.111-2, 11.111.222-4, 11.111.111-6, 11.111.111-1, 11.111.222-5, 11.111.111-5, 11.111.111-7, 11.111.111-4, 11.111.111-3, 11.111.222-6"
rut = rut.replace(",","").split()

apellido = "Vera, Fernandez, Gomez, Mendez, Salas, Barrientos, Soto, Lara, Jara, Jaque"
apellido = apellido.replace(",","").split()

descuento = "0.04, 0.04, 0.03, 0.02, 0.05, 0.10, 0.03, 0.05, 0.05, 0.02"
descuento = descuento.replace(",","").split()
for i in range(len(descuento)):
    descuento[i] = float(descuento[i])
    
cod_carrera = "C001, C002, C001, C003, C004, C004, C005, C002, C001, C003"
cod_carrera = cod_carrera.replace(",","").split()

for i in range(len(registro)):
    print(f"Registro nro: {registro[i]}, rut: {rut[i]}, apellido: {apellido[i]}, "
          f"descuento: {descuento[i]}, cod_carrera: {cod_carrera[i]}")

##print("SEGUNDO")

unico_cod = "C001, C002, C003, C004, C005"
unico_carrera = "administracion, contador, informatica, mecanica, prevencion"

unico_cod = unico_cod.replace(",","").split()
unico_carrera = unico_carrera.replace(",","").split()

matricula = "$105000, $110000, $125000, $100000, $105000"
mensualidad = "$83500, $80500, $85000, $78000, $75000"

matricula = matricula.replace("$","").replace(",","").split()
for i in range(len(matricula)):
    matricula[i] = int(matricula[i])

mensualidad = mensualidad.replace("$","").replace(",","").split()
for i in range(len(mensualidad)):
    mensualidad[i] = int(mensualidad[i])

print("TERCERO")
carrera = ""
costo = ""
final = ""

for i in cod_carrera:
    indice = unico_cod.index(i)
    nombre_carrera = unico_carrera[indice]
    costo_carrera = matricula[indice] + mensualidad[indice] * 10
    costo_final = costo_carrera * (1-descuento[indice])
    
    costo_carrera = str(costo_carrera)
    costo_final = str(costo_final)
    
    carrera+= nombre_carrera + " "
    costo+= "$" +costo_carrera + " "
    final += "$" +costo_final + " "
    
carrera = carrera.split()
costo = costo.split()
final = final.split()
print()
for i in range(len(registro)):
    print(carrera[i], costo[i], final[i])
print()
ordenados = sorted(range(len(rut)), key = lambda i: rut[i], reverse = True)

for i in ordenados:
    print(f"rut: {rut[i]}, apellido: {apellido[i]},{carrera[i]}, {costo[i]}, {final[i]}")


