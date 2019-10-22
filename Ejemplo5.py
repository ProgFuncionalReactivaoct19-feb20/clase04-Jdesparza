"""
	Jdesparza
	Manejo de colecciones y tuplas


	# Encontrar la siguiente estructura
	#

	[(16.333333333333332, 'Ángel'), (16.666666666666668, 'José'), (13.0, 'Ana')]
	(16.666666666666668, 'José')
	[(13.0, 'Ana'), (16.666666666666668, 'José'), (16.333333333333332, 'Ángel')]

	 

	Dadas las siguientes estructuras

"""
# lista con datos enteros en forma de dupla
paraleloA = [(19, 10, 20), (20, 20, 10), (20, 10, 9)]
# lista con datos String
nombres = ["Ángel", "José", "Ana"]
# para sumar las notas de cada dupla
suma_promedio = lambda x: x[0]+x[1]+x[2]
# formula para calcular el promedio
promedio = lambda x: (suma_promedio(x)/len(x))
# para calcular el promedio en base a la suma de las notas
promedio1= (list(map(promedio, paraleloA)))
# para presentar los datos sin cambiar el orden
resultado = list(zip(promedio1, nombres))
# para presentar los datos cambiando el orden
resultado1 = list(reversed(resultado))
# se imprimen los resultados
print(resultado)
print(max(resultado))
print(resultado1)