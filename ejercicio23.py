suma = 0
t_num = 0
numero = 1
media = 0
while numero > 0:
    numero =  int(input("Introduce un número (0 para dejar de contar): "))
    if numero == 0:
        media = suma / t_num
        break
       
    else:     
        suma += numero
        t_num +=1
    
print(f"Suma de todos los números {suma}\nMedia de todos los número {media}")
