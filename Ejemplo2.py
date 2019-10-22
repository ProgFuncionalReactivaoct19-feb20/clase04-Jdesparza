"""
	Jdesparza
	Manejo de colecciones y tuplas
	# Encontrar la siguiente estructura
	# [("a", (30, 1)), ("b", (100, 2)), ("c", (20, 4))]
"""
# se cran las listas
# lista con datos enteros en forma de dupla
lista = [(100, 2), (20, 4), (30, 1)]
# lista con datos String
lista2 = ["b", "a", "c"]

"""
	lista1 = sorted(lista, key= lambda x: -x[0])
	resultado = sorted((list(zip(lista2, lista1))), reverse = False)
"""

# se imprime el resultado haciendo una sola lista que esta ordenada de mayor
# a menor dependiendo de los datos String
print(list(zip(sorted(lista2), sorted(lista, key = lambda x: x[1]))))