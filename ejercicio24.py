cant_numeros = int(input("Total de números a pedir: "))
vueltas = 0
num_mayores = 0
num_iguales = 0
num_menores = 0
while vueltas < cant_numeros:
    vueltas += 1
    numero = int(input("Introduce un número: "))
    if numero > 0:
        num_mayores += 1
    elif numero == 0:
        num_iguales += 1
    else:
        num_menores +=1
print(f"Total de números mayores a 0: {num_mayores}\nTotal de números menores a 0: {num_menores}\nTotal de números iguales a 0: {num_iguales}")