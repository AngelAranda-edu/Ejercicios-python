contador = 0
lista = []
while contador != 5:
    print(f"Sublista numero {contador + 1}")
    sublista = []
    subcontador = 0
    while subcontador != 5:
        sublista.append(int(input(f"Ingrese el {subcontador + 1} número: ")))
        subcontador += 1
    lista.append(sublista)
    contador += 1
vuelta = 1
suma_e = 0
suma_a = 0
suma_b = 0
suma_c = 0
suma_d = 0
for a,b,c,d,e in lista:
    print(f"{vuelta} Vuelta : {a,b,c,d,e}")
    print(f"Suma vuelta {vuelta} : {a+b+c+d+e}")
    suma_a += a
    suma_b += b
    suma_c += c
    suma_d += d
    suma_e += e
    vuelta += 1
print(f"Suma a: {suma_a}, Suma b: {suma_b}, Suma c: {suma_c}, Suma d: {suma_d}, Suma e: {suma_e}")