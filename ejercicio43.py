cadena = input("Introduce una cadena de texto: ")
caracter = input("Introduce un caracter: ")
while caracter.isalpha() == False:
    print("Has introducido un caracter INVALIDO")
    caracter = input("Introduce un caracter: ")
print(f"El caracter {caracter} sale {cadena.count(caracter)} veces en la cadena.")
