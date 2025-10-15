num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
primer = num1
ultimo = num2
while str(primer)[-1] not in ('2','4','6','8','0'):
    primer +=1
while str(ultimo)[-1] not in ('2','4','6','8','0'):
    ultimo -=1 
par = primer
contador = 0
while par >= primer and par <= num2:
    contador += 1
    print(f"{contador}º numero par detectado: {par}")
    par +=2
print(f"Total de numeros pares: {contador}")