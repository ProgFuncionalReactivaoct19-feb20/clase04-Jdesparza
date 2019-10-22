"""
	Jdesparza
"""
# Creacion de dos listas una de tipo entero y la otra tipo  String
listaA = [10, 2, 3, 4]
listaB = ["a", "b", "c", "d"]
# para ordenar la primera lista de menor a mayor
lista1A = sorted(listaA, key= lambda x: -x)
# para ordenar la lista creada con zip de menor a mayor
resultado = sorted(list(zip(lista1A, listaB)))
# se imprime los resultados
print(resultado)
print(max(resultado))
