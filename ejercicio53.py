notas = []
total_notas = 0

while total_notas < 5:
    entrada = int(input("Introduce una nota: "))
    notas.append(entrada)
    total_notas += 1

notas_invertidas = notas[::-1]
nota_media = sum(notas) / len(notas)

print(f"""Elementos en orden inverso: {notas_invertidas}
Elementos en orden normal {notas}
Nota media: {nota_media}
Nota máxima: {max(notas)}
Nota mínima: {min(notas)}""")