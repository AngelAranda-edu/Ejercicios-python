cadena = input("Introduce una cadena: ")
subcadena = input("Introduce la subcadena a buscar al inicio: ")

print(f"¿Primera letra igual? {cadena[0] == subcadena[0]}")
print(f"¿Primeras dos letras iguales? {cadena[0:1] == subcadena[0:1]}")
print(f"¿Primeras tres letras iguales? {cadena[0:2] == subcadena[0:2]}")