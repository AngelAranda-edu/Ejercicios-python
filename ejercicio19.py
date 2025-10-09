preguntas_correctas = int(input("Introduce el número de preguntas correctas: "))
preguntas_incorrectas = int(input("Introduce el número de preguntas incorrectas: "))
preguntas_blanco = int(input("Introduce el número de preguntas en blanco: "))

total = (preguntas_correctas * 5) + (preguntas_incorrectas * -1) + (preguntas_blanco * 0)

print(f"""
Total de preguntas : {preguntas_correctas + preguntas_incorrectas + preguntas_blanco}
Preguntas correctas : {preguntas_correctas} ({preguntas_correctas * 5})
Preguntas incorrectas : {preguntas_incorrectas} ({preguntas_incorrectas * -1})
Preguntas en blanco : {preguntas_blanco} (0)
Total puntuación : {total}
""")