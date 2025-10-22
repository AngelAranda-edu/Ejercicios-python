diccionario = {}

# Relleno el diccionario con datos
while True:
	nombre_alumno = input("Introduce el nombre del alumno: ")
	notas = []
	if nombre_alumno == "salir":
		break
	elif nombre_alumno in diccionario:
		print("Ese alumno ya existe en el diccionario")
		continue
	while True:
		nota = int(input("     Introduce la nota del alumno: "))
		if nota < 0:
			break
		elif nota > 10:
			print("    **** Introduce una nota valida del 1 al 10 ****")
		notas.append(nota)
	diccionario[nombre_alumno] = notas


# Cálculo de notas medias
for alumno, notas in diccionario.items():
	suma = 0
	for nota in notas:
		suma += nota
	print(f"Media {alumno}: {suma / len(notas)}")
