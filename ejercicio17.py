HH = 8
MM = 1
SS = 60
T = 3600

salida_segundos = HH * 3600 + MM * 60 + SS
llegada_segundos = salida_segundos + T

hora_llegada = int(llegada_segundos / 3600)
minuto_llegada = int((llegada_segundos - hora_llegada * 3600) / 60)
segundo_llegada = int(llegada_segundos - hora_llegada * 3600 - minuto_llegada * 60)

print(f"Hora de llegada: {hora_llegada}\nMinutos:{minuto_llegada}\nSegundos:{segundo_llegada}")