ejecucion = True
while ejecucion == True:
    entrada = input("Introduce un caracter para ver si es VOCAL o no (espacio para salir): ")
    entrada = entrada.lower()
    if entrada == 'a' or entrada == 'e' or entrada == 'i' or entrada == 'o' or entrada == 'u':
        print("El caracter introducido es VOCAL")
    elif entrada == " ":
        print("Saliendo ....")
        break
    elif entrada == "":
        print("Introduce un caracter valido")
    else: 
        print("El caracter introducido NO ES UNA VOCAL")
