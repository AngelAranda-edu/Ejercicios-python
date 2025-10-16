total_ahorrado = 0
mes = 1

while mes <= 12:
    deposito = float(input(f"Introduce el ahorro del mes {mes}: "))
    total_ahorrado += deposito
    print(f"Total ahorrado hasta el mes {mes}: {total_ahorrado}eur")
    mes += 1

print(f"Total ahorrado en el año: {total_ahorrado} eur")
