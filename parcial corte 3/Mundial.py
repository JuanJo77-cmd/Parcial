puntos = {
    "Colombia": 0, 
    "Portugal": 0, 
    "Uzbekistán": 0, 
    "RD Congo": 0
}

partidos = [
    ["Portugal", 2, "RD Congo", 0],
    ["Uzbekistán", 1, "Colombia", 2],
    ["Portugal", 3, "Uzbekistán", 1],
    ["Colombia", 2, "RD Congo", 1],
    ["Colombia", 3, "Portugal", 1],
    ["RD Congo", 0, "Uzbekistán", 0],
]

for local, goles_l, visitante, goles_v in partidos:
    if goles_l > goles_v:
        puntos[local] += 3
    elif goles_v > goles_l:
        puntos[visitante] += 3
    else:
        puntos[local] += 1
        puntos[visitante] += 1

print("PUNTOS DEL GRUPO:")
print("Colombia:", puntos["Colombia"])
print("Portugal:", puntos["Portugal"])
print("Uzbekistán:", puntos["Uzbekistán"])
print("RD Congo:", puntos["RD Congo"])