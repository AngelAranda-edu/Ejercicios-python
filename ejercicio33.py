dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
horas_totales = 0.0

for dia in dias:
    horas = float(input(f"Horas trabajadas el {dia}: "))
    horas_totales += horas

precio = float(input("Ingrese la precio por hora: "))
sueldo = horas_totales * precio
print(f"Horas totales trabajadas: {horas_totales}")
print(f"Sueldo a pagar: {sueldo} eur")
