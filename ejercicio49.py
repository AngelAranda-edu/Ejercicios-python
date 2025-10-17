cadena = input("Introduce la cadena: ")
subcadena = input("Introduce la subcadena: ")

if subcadena in cadena:
    print(f"La subcadena \"{subcadena}\" se encuentra en la cadena.")
else:
    print(f"La subcadena \"{subcadena}\" NO se encuentra en la cadena.")