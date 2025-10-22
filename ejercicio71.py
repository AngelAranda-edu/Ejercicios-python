diccionario = {"pera":3, "manzana": 2,"naranja": 3.5}
ejecucion = True
cantidad_vendida = 0
print("Frutas en diccionario: ")
for fruta, cantidad in diccionario.items():
	print(fruta)
while ejecucion == True:
	nombre_fruta = input("Introduce el nombre de la fruta: ")
	if nombre_fruta in diccionario:
		cantidad_vendida = int(input(f"Introduce la cantidad de {nombre_fruta}s vendidas: "))
	else:
		print("Esa fruta no esta en el diccionario.")
		continue
	print(f"Ganancias totales ({nombre_fruta}): {diccionario[nombre_fruta]*cantidad_vendida}")
	pregunta = input("¿Quieres continuar con la ejecucion? Sí / No: ")
	while pregunta not in ("Sí", "Si", "No"):
		print("Introduce una opción valida.")
		pregunta = input("¿Quieres continuar con la ejecucion? Sí / No: ")
	if pregunta == "Sí" or pregunta == "Si":
		continue
	elif pregunta == "No":
		break
