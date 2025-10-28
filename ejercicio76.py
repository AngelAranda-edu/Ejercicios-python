def EsMultiplo (num1, num2):
	resultado = num1/num2
	if resultado.is_integer():
		print(f"El número {num1} es multiplo del número {num2}")
	else:
		print("Los números no son multiplos")
EsMultiplo(int(input("Introduce el primer número: ")),int(input("Introduce el segundo número: ")))
