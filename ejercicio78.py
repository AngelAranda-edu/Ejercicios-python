import os
def calcSegundos(h, m, s):
	s_horas = h*3600
	s_min = m*60
	total_s = s + s_min + s_horas
	resultado = f"La conversion de {h}:{m}:{s} a segundos es {total_s}"
	return resultado
def calcHMS(s):
	h_segundos = s // 3600
	m_segundos = (s % 3600) // 60
	seg = s - (s - (s % 3600) // 60)
	resultado = f"La conversión de {s} segundos a horas equivale a {h_segundos} horas {m_segundos} minutos y {seg} segundos"
	return resultado
while True:
	os.system("clear")
	print("""Escoge una opción del menu
1) La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
2) La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
3) Salir
""")
	opcion = int(input())
	if opcion == 1:
		print(calcSegundos(int(input("Introduce la cantidad de horas: ")), int(input("Introduce la cantidad de minutos: ")), int(input("Introduce la cantidad de segundos: "))))
		input()
	elif opcion == 2:
		print(calcHMS(int(input("Introduce una cantidad de segundos: "))))
		input()
	elif opcion == 3:
		print("Saliendo....")
		break

