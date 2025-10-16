numero = int(input("Introduce un número: "))

if numero <= 1:
    print(f"El número {numero} NO es primo")
elif numero == 2:
    print(f"El número {numero} es primo")
else:
    es_primo = True
    divisor = 2
    
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            es_primo = False
            break
        divisor += 1
    
    if es_primo:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} NO es primo")
