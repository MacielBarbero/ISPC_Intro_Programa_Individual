# # Calcular el IVA.
# precio_incial = int(input("Ingrese el precio del producto: "))
# iva = precio_incial * 0.21
# precio_final = precio_incial + iva
# print(f"El precio final del producto es: ${precio_final}")

# Calcular el IVA permitiendo cambiar el porcentaje de la alícuota.
# precio_incial = int(input("Ingrese el precio del producto: "))
# alicuota = float(input("Ingrese porcentaje alícuota de I.V.A.: ")) / 100
# iva = precio_incial * alicuota
# precio_final = precio_incial + iva
# print(f"El precio final del producto es: ${precio_final}")

# Casa de cambio.
pesos = float(input("Ingrese la cantidad de pesos que desea convertir:"))
TC = float(input("Ingrese la tasa de cambio:"))
dolares = pesos / TC
print(f"Usted tiene la siguiente cantidad de dólares: {dolares} USD")


# Para comentar varias líneas en Visual Studio Code, basta con seleccionar las 
# líneas que se desean comentar y presionar las teclas Ctrl + K + C en Windows o
# Linux, o Cmd + K + C en Mac. Por otro lado, para descomentarlas, se debe presionar 
# Ctrl + K + U en Windows o Linux, o Cmd + K + U en Mac