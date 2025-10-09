eur2 = int(input("Cantidad de monedas de 2 eur: "))
eur1 = int(input("Cantida de monedas de 1 eur: "))
cents50 = int(input("Cantidad de monedas de 50 cent: "))
cents20 = int(input("Cantidad de monedas de 20 cent: "))
cents10 = int(input("Cantidad de monedas de 10 cent: "))

t_centimos = (cents50 * 50 + cents20 * 20 + cents10 * 10) /100

t_euros = (eur1 + eur2 *2 )

print(f"Total en centimos : {t_centimos} eur\nTotal en euros : {t_euros} eur\nTotal : {t_centimos + t_euros} eur")