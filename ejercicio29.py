base = int(input("Introduce la base: "))
exponente = int(input("Introduce el exponente: "))
resultado = 1
t_exponente = exponente

while t_exponente > 0:
    resultado *= base
    t_exponente -=1

print(f"{base} elevado a {exponente} es: {resultado}")
