tiempo = 20
pago = 10
contador = 0
total = 0
while tiempo > contador:
    contador += 1
    total += pago
    print(f"{contador} mes a pagar {pago} eur")
    pago *= 2
print(f"Total a pagar: {total} eur")