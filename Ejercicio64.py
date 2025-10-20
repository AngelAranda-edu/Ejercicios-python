precios = []
for precio in (1,2,3,4,5):
    precios.append(int(input(f"Indica el precio del {precio} articulo: ")))
lista = []
for n in (1,2,3,4):
    print(f"Sucursal número {n}")
    sublista = []
    for n in (1,2,3,4,5):
        sublista.append(int(input(f"Introduzca la cantidad vendida del articulo número {n}: ")))
    lista.append(sublista)
total_a = 0
total_b = 0
total_c = 0
total_d = 0
total_e = 0
for sucursales in lista:
    total_a += sucursales[0]
    total_b += sucursales[1]
    total_c += sucursales[2]
    total_d += sucursales[3]
    total_e += sucursales[4]
print(f""""Cantidad total vendida articulo 1: {total_a}
Cantidad total vendida articulo 2: {total_b}
Cantidad total vendida articulo 3: {total_c}
Cantidad total vendida articulo 4: {total_d}
Cantidad total vendida articulo 5: {total_e}""")
total_cantidad = 0
for producto in lista[1]:
        total_cantidad += producto

print(f"Cantidad total de articulos en la sucursal 2: {total_cantidad}")
print(f"Cantidad del articulo 3 en la sucursal 1: {lista[0][2]}")

total_empresa= 0
total_sucursales = []
num = 0
for sucursal in lista:
    total_sucursal = 0
    for val in sucursal:
         total_sucursal+=val
         total_empresa += val
    num +=1
    total_sucursales.append(total_sucursal)
    print(f"Total sucursal {num}: {total_sucursal}")
print(f"Total recaudación de la empresa {total_empresa}")
print(f"Sucursal de mayor recaudación: {max(total_sucursales)}")

            

