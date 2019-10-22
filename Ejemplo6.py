"""
	Jdesparza
	Manejo de colecciones y tuplas


	# Encontrar la siguiente estructura
	#

	[(4.333333333333333, 13, 'Ángel'), (4.666666666666667, 14, 'Ana')]

	Dadas las siguientes estructuras

"""
# lista con datos enteros en forma de tupla
paraleloA = [(19, 10, 20), (1, 2, 10), (20, 10, 9), (1, 4, 9)]
# lista con datos String
nombres = ["Luis", "Ángel", "José", "Ana"]
# para sumar las notas de cada tupla
suma_promedio = lambda x: x[0]+x[1]+x[2]
# formula para calcular el promedio
promedio = lambda x: (suma_promedio(x)/len(x))
# para calcular el promedio en base a la suma de las notas
promedio1 = (list(map(promedio, paraleloA)))
# para mostrar la suma de las notas de cada tupla
suma_promedio1 = (list(map(suma_promedio, paraleloA)))
# muestra todos los promedios con el respectivo nombre
resultado_aprox = list(zip(promedio1, suma_promedio1,nombres))
# para mostrar solamente los promedios de las personas con calificaciones bajas
resultado = list(filter(lambda x: x[0]<13, resultado_aprox))
# se presentan los resultados
print(resultado)