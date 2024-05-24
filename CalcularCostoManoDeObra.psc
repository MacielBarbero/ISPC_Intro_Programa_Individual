//EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo
//que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
//cliente le indica que necesita conocer el costo de mano de obra para pintar una
//pared rectangular de un galpón. El pintor cobra un monto ?jo por cada metro
//cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
//pintar la pared.

ALGORITMO CalcularCostoManoDeObra
	
    // Definir variables
    DEFINIR anchoPared, altoPared, costoMetroCuadrado, costoTotal COMO REAL
	
    // Solicitar al usuario las medidas de la pared y el costo por metro cuadrado.
    ESCRIBIR "Ingrese el ancho de la pared en metros:"
    LEER anchoPared
    ESCRIBIR "Ingrese el alto de la pared en metros:"
    LEER altoPared
    ESCRIBIR "Ingrese el costo por metro cuadrado de mano de obra:"
    LEER costoMetroCuadrado
	
    // Calcular el área de la pared
    areaPared <- anchoPared * altoPared
	
    // Calcular el costo total de la mano de obra
    costoTotal <- areaPared * costoMetroCuadrado
	
    // Mostrar el costo total de la mano de obra
    ESCRIBIR "El costo total de mano de obra para pintar la pared es:", costoTotal, " ", "pesos"
	
FIN ALGORITMO

