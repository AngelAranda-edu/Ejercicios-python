cadena = input("Ingrese una cadena de texto: ")
invertido = ""

for caracter in cadena:
    if caracter.isupper():
        invertido += caracter.lower()
    elif caracter.islower():
        invertido += caracter.upper()
    else:
        invertido += caracter

print(f"Cadena original: {cadena}\nCadena convertida: {invertido}")