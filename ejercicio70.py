cadena = input("Introduce una cadena de texto: ")
diccionario = {}
for caracter in cadena:
	diccionario[caracter]= cadena.count(caracter)
print(diccionario)
