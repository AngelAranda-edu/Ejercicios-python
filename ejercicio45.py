nombre_completo = "angel aranda mesa"
contador = nombre_completo.count(" ")
nombre = []
posicion = 0
ejecucion = 0

while ejecucion <= contador:
    if ejecucion < contador:
        posicion2 = nombre_completo.find(" ", posicion)
        nombre.append(nombre_completo[posicion:posicion2].capitalize())
        posicion = posicion2 + 1
    else:
        nombre.append(nombre_completo[posicion:].capitalize())
    ejecucion += 1

print(" ".join(nombre))