def Login (usuario, contrasena):
	if usuario == "usuario1" and contraseña == "asdasd":
		return True
	else:
		return False
intentos = 0
while True:
	user = input("Introduce un nombre de usuario: ")
	passwd =input("Introduce la contraseña: ")
	acceso = Login(user,passwd)
	if acceso == True:
		print(f"Acceso correcto en el {intentos} intento")
	elif acceso == False:
		intentos +=1
		print(f"Acceso denegado, intento {intentos}")
	if intentos >= 3:
		print("Numero maximo de intentos permitidos")
		break
