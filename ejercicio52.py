lista = []
for num in (1,2,3,4,5):
	lista.append(input(f"{num} lista de caracteres: "))
lista_inversa = lista[::-1]
print(f"Lista ordenada: {lista}\nLista inversa: {lista_inversa}")
