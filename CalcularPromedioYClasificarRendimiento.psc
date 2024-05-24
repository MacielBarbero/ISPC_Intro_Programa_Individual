//
//Calcular el promedio de notas y clasificar el rendimiento
//En una escuela, luego de tomar un determinado examen, es necesario calcular el 
//promedio de notas (las notas van de 0 a 10) de los alumnos de un curso. Se necesita
//saber si el rendimiento ha sido elevado (el promedio es mayor a 8), aceptable 
//	(el promedio está comprendido entre 6 y 8) o bajo (promedio es inferior a 6). 
//Desarrollar un algoritmo que resuelva este problema. Para tener en cuenta: las 
//			autoridades del colegio saben cuántos estudiantes del curso han rendido el examen

ALGORITMO CalcularPromedioYClasificarRendimiento
	
    // Declaración de variables
    DEFINIR totalEstudiantes, nota, sumaNotas COMO ENTERO
    DEFINIR promedio COMO REAL
	
    // Inicialización de variables
    totalEstudiantes <- 0
    sumaNotas <- 0
	
    // Solicitar el número de estudiantes
    ESCRIBIR "Ingrese el número total de estudiantes:"
    LEER totalEstudiantes
	
    // Ciclo para ingresar las notas y calcular la suma de las notas
    PARA i DESDE 1 HASTA totalEstudiantes HACER
        ESCRIBIR "Ingrese la nota del estudiante ", i, " (entre 0 y 10):"
        LEER nota
        sumaNotas <- sumaNotas + nota
    FIN PARA
	
    // Calcular el promedio de notas
    promedio <- sumaNotas / totalEstudiantes
	
    // Clasificar el rendimiento
    SI promedio > 8 ENTONCES
        ESCRIBIR "El rendimiento es elevado."
    SINO SI promedio >= 6 Y promedio <= 8 ENTONCES
			ESCRIBIR "El rendimiento es aceptable."
		SINO
			ESCRIBIR "El rendimiento es bajo."
		FIN SI
	FIN SI
	FIN ALGORITMO
