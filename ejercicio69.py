diccionario = {}
numero = int(input("Introduce un número para calcular el cuadrado de ese número hasta el número insertado: "))
for num in range(1,numero+1):
	diccionario[num]=num**2
print(diccionario)
