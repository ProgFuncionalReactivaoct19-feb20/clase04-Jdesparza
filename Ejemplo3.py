"""
	Jdesparza
	Manejo de colecciones y tuplas
	# Encontrar la siguiente estructura
"""
# se cran las listas
# lista con datos enteros en forma de dupla
lista = [(100, 2), (20, 4), (30, 1)]
# lsita con datos tipo String
lista2 = ["b", "a", "c"]
# se transforma en mayuscula los datos de la lista 2
lista2_1 = map(lambda x: x.upper(), lista2)

# se imprime el resultado haciendo una sola lista que esta ordenada de menor
# a mayor dependiendo de los datos String
print(list(zip(sorted(lista), sorted(lista2_1, reverse=True))))