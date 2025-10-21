nombres = []
edades = []
ejecucion = True
mayor_edad = 0
while ejecucion == True:
	nombre = input("Introduce un nombre (* para salir): ")
	if nombre == "*":
		break
	edad = int(input(f"Introduce la edad de {nombre}: "))
	nombres.append(nombre)
	edades.append(edad)
	if edad > 18:
		mayor_edad += 1
print(f"Alumnos mayores de edad: {mayor_edad} / {len(nombres)}")
print(f"El alumno mayor tiene una edad de {max(edades)} {nombres[edades.index(max(edades))]}")
