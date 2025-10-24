import os
diccionario = {"Ana López": "601123456", "Luis Martín": "602987654", "Marta Pérez": "603555777", "David Gómez": "604112233", "Elena Ruiz": "605900800"}
while True:
    os.system("clear")
    print("Opciones: \n1 - Añadir/Modificar\n2 - Buscar\n3 - Borrar\n4 - Listar\n5 - Salir")
    opcion = input("Introduce una ocpión: ")
    if opcion == "1":
        nombre = input("Introduce el nombre del usuario: ")
        if nombre in diccionario:
            print(f"{nombre} : {diccionario[nombre]}")
            modificador = input(f"Quiere modificar el numero de telefono de {nombre}(S/N): ")
            if modificador == "S":
                diccionario[nombre] = input(f"Indica el nuevo numero de telefono de {nombre}: ")
                continue
            else:
                continue
        else:
            print("Ese usuario no esta en la lista, añadiendo....")
            telefono = input("Indica el número de télefono del usuario: ")
            diccionario[nombre] = telefono
    elif opcion == "2":
        cadena = input("Ingresa la cadena de caracteres por la que quieres buscar: ")
        coincidencia = []
        for nombre, telefono in diccionario.items():
            if nombre.startswith(cadena):
                coincidencia.append(nombre)
        if len(coincidencia) <= 0:
            print(f"No existe ningun usuario que empiece por {cadena}")
            continue
        for nombre in coincidencia:
            print(nombre, " - ", diccionario[nombre])
    elif opcion == "3":
        nombre = input("Introduce el nombre del usuario: ")
        if nombre in diccionario:
            borrar = input("El usuario existe. ¿Quieres borrarlo de la lista? S/N: ")
            if borrar == "S":
                diccionario.pop(nombre)
                continue
            else:
                continue
        else:
            print("El usuario no existe")
    elif opcion == "4":
        for nombre, telefono in diccionario.items():
            print(f"{nombre} : {telefono}") 
    elif opcion == "5":
        print("Saliendo.....")
        break
    else:
        print("Introduce una opción valida")
    input("Pulsar ENTER para continuar...")
