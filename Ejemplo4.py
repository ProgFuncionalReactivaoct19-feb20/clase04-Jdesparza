"""
	Jdesparza
	Manejo de colecciones y tuplas


	# Encontrar la siguiente estructura
	#

	[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]

	Dadas las siguientes estructuras:
"""
# se crean las listas
# lista con datos enteros en forma de dupla
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
# lista con nombres
nombres = ["Ángel", "José", "Ana"]
# para sumar las notas de cada dupla
suma_promedio = lambda x: x[0]+x[1]+x[2]
# formula para calcular el promedio
promedio = lambda x: (suma_promedio(x)/len(x))
# para calcular el promedio en base a la suma de las notas
promedio1= (list(map(promedio, paraleloA)))
# para hacer una lista que tenga los datos del promedio y el nombre de la persona
resultado = list(zip(promedio1, nombres))
# se presentan el resultado en forma de lista
print(resultado)