# # Actividades parte 1: Iniciando
# # Desarrollar en Python las siguientes consignas utilizando los recursos ya vistos 
# # (variables, input, print, if, if - else, while, for) que consideren adecuados para 
# # cada uno de estos casos:

# # 1. Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no 
# # repetidas, guardarlos en una lista y mostrarlos. 
# lista_nombres = []

# while len(lista_nombres) < 10:
#     nombre = input("Ingrese un nombre: ").lower()
#     if nombre not in lista_nombres:
#         lista_nombres.append(nombre)

# for i in range(len(lista_nombres)):
#     lista_nombres[i] = lista_nombres[i].capitalize()

# print(lista_nombres)

# # 2.Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar 
# # la lista y mostrarlo.
# lista_nombres_2 = lista_nombres.copy() # Shallow copy.
# del lista_nombres_2[-1]
# del lista_nombres_2[2]
# lista_nombres_2.sort()
# print(lista_nombres_2)

# lista_nombres_2 = lista_nombres_2.pop() El método pop() elimina y devuelve el elemnto eliminado.

# 3.Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

# datos = {'nombre': 'Juan', 'apellido': 'Pérez', 'dni': '20899692', 'email': 'juanperez@gmail.com'}

# print(datos)

# # 4.En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento).

# familia = {
#            'Persona1': ('Juan', 'Pérez', '1258963', '1@gmail.com', '1996-04-01'), #YYYY-MM-DD
#            'Persona2': ('José', 'Gómez', '1258962', '1@gmail.com', '1996-04-01'),
#            'Persona3': ('Amalia', 'López', '1258961', '1@gmail.com', '1996-04-01'),
#            'Persona4': ('Roma', 'Casas', '1258960', '1@gmail.com', '1996-04-01')
#            }
# print(familia)
# 5. Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.
# # Nota: para saber si el número i es par hacer i % 2 == 0
# mi_lista = []
# numero = int(input("Ingrese un número: "))

# while len(mi_lista) < numero:
#     for i in mi_lista:
#         if i % 2 == 0:
#             mi_lista.append(i)

# mi_tupla = tuple(mi_lista)
# print(mi_tupla)

mi_lista = []
numero = int(input("Ingrese un número: "))
i = 0

while len(mi_lista) < numero:
    if i % 2 == 0:
        mi_lista.append(i)
    i += 1

mi_tupla = tuple(mi_lista)
print(mi_tupla)
