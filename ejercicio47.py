cadena = input("Introduce una cadena: ")

primer_caracter = input("Introduce el primer carácter: ")
while len(primer_caracter) != 1:
    print("Error: Debes introducir un solo carácter")
    primer_caracter = input("Introduce el primer carácter: ")

segundo_caracter = input("Introduce el segundo carácter: ")
while len(segundo_caracter) != 1:
    print("Error: Debes introducir un solo carácter")
    segundo_caracter = input("Introduce el segundo carácter: ")

cadena_modificada = cadena.replace(primer_caracter, segundo_caracter)

print(f"Cadena original: {cadena}")
print(f"Cadena modificada: {cadena_modificada}")