sb = 1000 # sueldo base
v1 = 500 # venta 1
v2 = 300 # venta 2
v3 = 600 # venta 3
comisiones= float(v1)*0.10 + float(v2)*0.10 + float(v3)*0.10

print(f"Total de comisiones: {comisiones}\nTotal al mes: {float(comisiones) + float(sb)}")
