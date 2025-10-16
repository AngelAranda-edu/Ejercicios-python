lim_inf = int(input("Introduce el límite inferior: "))
lim_sup = int(input("Introduce el límite superior: "))
ejecucion = True
contador_limite = 0
contador_iguales = 0
contador_otros = 0

while lim_sup < lim_inf:
    print("El limite superior que has introducido es menor al limite inferior")
    lim_sup = int(input("Introduce el límite superior: "))

while ejecucion == True:
    entrada = int(input("Introduce un número (0 para salir): "))

    if entrada == 0: 
        ejecucion = False
    elif entrada > lim_inf and entrada < lim_sup:
        contador_limite += 1
    elif entrada == lim_inf or entrada == lim_sup:
        contador_iguales += 1
    else:
        contador_otros += 1
print(f"""Total de números en el límite: {contador_limite}
Total números fuera de intervalo: {contador_otros}
Total números iguales a los limites del intervalo: {contador_iguales}
""")
