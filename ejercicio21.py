numero= int(input ("Introduce un número para calcular su factorial: "))
factorial =  1
while numero > 0:
	factorial = factorial * numero
	numero -= 1
print(f"El factorial es {factorial}")
