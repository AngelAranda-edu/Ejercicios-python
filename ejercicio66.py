lista = []

opcion = 0
while opcion != 9:
    print("\nMENÚ DE OPCIONES")
    print("1. Añadir número a la lista")
    print("2. Añadir número en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número por posición")
    print("6. Contar apariciones de un número")
    print("7. Mostrar posiciones de un número")
    print("8. Mostrar todos los números")
    print("9. Salir")

    opcion = int(input("\nElige una opción (1-9): "))

    if opcion == 1:
        num = int(input("Introduce un número: "))
        lista.append(num)
        print("Número añadido a la lista")

    elif opcion == 2:
        num = int(input("Introduce el número: "))
        pos = int(input("Introduce la posición: "))
        if 1 <= pos <= len(lista) + 1:
            lista.insert(pos - 1, num)
            print("Número añadido en la posición indicada")
        else:
            print("Posición no válida.")

    elif opcion == 3:
        print(f"La lista tiene {len(lista)} elementos.")

    elif opcion == 4:
        print("Se elimina el último número: {lista[-1]}")
        lista.pop()

    elif opcion == 5:
        pos = int(input("Introduce la posición a eliminar: "))
        if 1 <= pos <= len(lista):
            print("Se elimina el número: {lista[pos - 1]})
            lista.pop(pos - 1)
        else:
            print("Posición no válida.")


    elif opcion == 6:
        num = int(input("Introduce el número a contar: "))
        print(f"El número {num} aparece {lista.count(num)} veces en la lista.")

    elif opcion == 7:
        num = int(input("Introduce el número a buscar: "))
        posiciones = []
        for i in range(len(lista)):
            if lista[i] == num:
                posiciones.append(i + 1)
        if len(posiciones) > 0:
            print(f"El número {num} está en las posiciones: {posiciones}")
        else:
            print("El número no está en la lista")

    elif opcion == 8:
        print(f"Los números en la lista son: {lista}")

    elif opcion == 9:
        print("Saliendo del programa...")

    else:
        print("Selecciona una opción valida")

