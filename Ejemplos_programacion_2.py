# EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada

# materia y quiere saber cuál es su promedio.
# Solicitar al usuario que ingrese las notas, separadas por coma
notas_input = input("Ingrese las notas obtenidas separadas por coma: ")

# Dividir la entrada en una lista de cadenas utilizando la coma como delimitador
notas_str = notas_input.split(',')

# Convertir las cadenas de notas a números enteros
notas = [int(nota) for nota in notas_str]

# Calcular el promedio de las notas
promedio = sum(notas) / len(notas)

# Imprimir el promedio
print("El promedio de las notas es:", promedio)



# EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo

# que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

# cliente le indica que necesita conocer el costo de mano de obra para pintar una

# pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

# cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

# pintar la pared.
# Solicitar al usuario que ingrese las dimensiones de la pared en metros
largo = float(input("Ingrese el largo de la pared en metros: "))
alto = float(input("Ingrese la altura de la pared en metros: "))

# Calcular el área de la pared en metros cuadrados
area_pared = largo * alto

# Costo por metro cuadrado (monto fijo por cada metro cuadrado)
costo_por_metro_cuadrado = 50  # Puedes ajustar este valor según el precio del pintor

# Calcular el costo de mano de obra para pintar la pared
costo_mano_de_obra = area_pared * costo_por_metro_cuadrado

# Imprimir el costo de mano de obra
print("El costo de mano de obra para pintar la pared es:", costo_mano_de_obra, "pesos")



# EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su

# equipo lleva acumulados en el campeonato, para ello recibe cada semana la

# información de la cantidad total de partidos, desde el inicio del campeonato, que

# el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado

# recibe un punto, por cada partido ganado tres puntos y por los perdidos cero

# puntos.
# Solicitar al usuario que ingrese la cantidad de partidos ganados, perdidos y empatados
partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))

# Calcular la cantidad total de puntos acumulados
puntos = (partidos_ganados * 3) + partidos_empatados

# Imprimir la cantidad total de puntos acumulados
print("El equipo lleva acumulados", puntos, "puntos en el campeonato.")
