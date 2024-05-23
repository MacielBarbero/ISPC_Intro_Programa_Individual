# # Mostrar los números desde el 0 al número solicitado al usuario (input)
# numero = int(input("Ingrese un número: "))
# for i in range(numero + 1):
#     print(i)

# # Mostrar sólo los números pares desde 0 hasta el número ingresado (input). 
# # Nota: para saber si un número es par hacer i % 2 == 0)
# numero = int(input("Ingrese un número: "))
# for i in range(numero + 1):
#     if i % 2 == 0:
#         print(i)

# # Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta 
# # que el valor de lo que ingresa sea “fin”
# nombre = ""
# while nombre.lower() != "fin":
#     nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
#     print(nombre)


# # Calcular el promedio de notas y clasificar el rendimiento
# # En una escuela, luego de tomar un determinado examen, es necesario calcular el 
# # promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. Se necesita
# # saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable 
# # (el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). 
# # Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las 
# # autoridades del colegio saben cuántos estudiantes del curso han rendido el examen.

# cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))
# suma_notas = 0

# for _ in range(cantidad_alumnos):
#     nota = float(input("Ingrese la nota del alumno (entre 0 y 10): "))
#     suma_notas += nota

# promedio = suma_notas / cantidad_alumnos

# if promedio > 8:
#     print("El rendimiento del curso es elevado.")
# elif promedio >= 6:
#     print("El rendimiento del curso es aceptable.")
# else:
#     print("El rendimiento del curso es bajo.")

# Un profesor de matemática necesita generar la tabla de multiplicar de un 
# número entero comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer 
# como salida:
# 3x1=3
# 3x2=6
# 3x3=9
# …. y así hasta 10

# Resuelva este problema utilizando un mientras y de modo que por la salida se emita 
# la tabla tal como se propone.

numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
i = 1
while i <= 10:
    resultado = numero * i
    print(f"{numero}x{i}={resultado}")
    i += 1

# Resuelva este problema utilizando un para y de modo que por la salida se emita 
# la tabla tal como se propone.
numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero}x{i}={resultado}")

