num1 = int(input("Ingrese el primer número: "))
num2= int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"La distancia entre {num1} y {num2} es {num1 - num2}")
elif num2 > num1:
    print(f"La distancia entre {num1} y {num2} es {num2 - num1}")
elif num1 == num2:
    print("Los números son iguales, la distancia es 0")
