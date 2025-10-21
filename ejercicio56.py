mes = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
numero_mes = int(input("Introuce un número de mes: "))
numero_mes -= 1
print(f"El mes de {mes[numero_mes]} tiene {dias[numero_mes]} días.")
