count = input("Introduce un texto aleatorio : ")
numero = 0
contador = 0
resuelto = False

for letra in count:
    numero +=1
    numero *= numero
total_vocales = count.count("a") + count.count("e") + count.count("i") + count.count("o") + count.count("u")
numero *= total_vocales
while numero > 100 or numero < 1:
    if numero > 100:
        numero//= 10
    elif numero < 1:
        numero *= 10 
    int(numero)

while contador < 10 and resuelto == False:
    respuesta= int(input("Introduce un número del 1 al 100: "))
    if respuesta > 100 or respuesta < 1:
        print("Introduce un número VALIDO del 1 al 100")
        continue
    elif respuesta == numero:
        print(f"Enhorabuena, has adivinado el número\nTotal de intentos requeridos: {contador}")
        resuelto = True
    elif respuesta != numero:
        contador +=1
        if respuesta > numero:
            print(f"El número es menor al introducido, tienes {10-contador} intentos")
        else:
            print(f"El número es mayor al introducido, tienes {10-contador} intentos")
    
if contador >= 10:
    print(f"Has superado los intentos permitidos, el numero era {numero}")