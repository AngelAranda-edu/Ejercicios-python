def EscribirCentrado (texto):
	print(f"{int(40-len(texto)/2)*' '} {texto} {int(40-len(texto)/2)*' '}")
	print(f"{int(40-len(texto)/2)*' '} {'='*len(texto)} {int(40-len(texto)/2)*' '}")
EscribirCentrado("Hola")
