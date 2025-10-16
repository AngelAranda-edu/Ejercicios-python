ejecucion = True
print("Opcion1\nOpcion2\nOpcion3\nSalir")
while ejecucion == True:
	opcion = input("Escoge una opción: ")
	if opcion == '1':
		print("Opcion 1 escogida")
	elif opcion == '2':
		print("Opcion 2 escogida")
	elif opcion == '3':
		print("Opcion 3 escogida")
	elif opcion == 'Salir':
		print("Saliendo.....")
		break
	else:
		print("Escoge una opción valida")
