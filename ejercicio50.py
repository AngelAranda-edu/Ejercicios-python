cadena = input("Introduce una cadena: ")
cadena = cadena.lower()

if cadena == cadena[::-1]:
    print("La cadena es una palabra palíndroma")
else:
    print("La cadena no es una palabra palíndroma")