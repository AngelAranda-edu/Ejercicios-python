dias = 5
dia = 1
temperatura_min = []
temperatura_max = []
while dia <= dias:
	temperatura_min.append(int(input(f"Introduce la temperatura min del dia {dia}: ")))
	temperatura_max.append(int(input(f"Introduce la temperatura max del día {dia}: ")))
	dia += 1
t_media = sum(temperatura_max) + sum(temperatura_min) / len(temperatura_max) + len(temperatura_min)
t_min = min(temperatura_min)

temperatura = int(input("Ingresa una temperatura por teclado: "))
contador = temperatura_max.count(temperatura)
misma_t = 0
if temperatura in temperatura_max:
	print(f"Días que coinciden con esa misma temperatura {contador}")
	while contador > 0:
		misma_t = temperatura_max.index(temperatura, misma_t)
		print(f"El día {misma_t +1} coincide en temperatura max")
		contador -=1
		misma_t += 1
else:
	print(f"No hay ningun día con esa temperatura maxima")
