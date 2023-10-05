# Cargaremos el grafo de la imagen

from grafo import *

grafo = Grafo()

# INSERTAREMOS PRIMEROS LOS VERTICES
insertarVertice(grafo, "A")
insertarVertice(grafo, "B")
insertarVertice(grafo, "C")
insertarVertice(grafo, "D")
insertarVertice(grafo, "E")
insertarVertice(grafo, "F")

print("---- TAMAÑO GRAFO")
print(tamanio(grafo))


print("---- VERTICES")
imprimirVertices(grafo)

# INSERTAREMOS LUEGO LAS ARISTAS

insertarArista(grafo, 5, buscarVertice(grafo, "A"), buscarVertice(grafo, "C"))
insertarArista(grafo, 5, buscarVertice(grafo, "A"), buscarVertice(grafo, "D"))
insertarArista(grafo, 7, buscarVertice(grafo, "A"), buscarVertice(grafo, "B"))
insertarArista(grafo, 4, buscarVertice(grafo, "B"), buscarVertice(grafo, "D"))
insertarArista(grafo, 11, buscarVertice(grafo, "B"), buscarVertice(grafo, "E"))
insertarArista(grafo, 9, buscarVertice(grafo, "C"), buscarVertice(grafo, "F"))
insertarArista(grafo, 18, buscarVertice(grafo, "C"), buscarVertice(grafo, "E"))
insertarArista(grafo, 2, buscarVertice(grafo, "D"), buscarVertice(grafo, "C"))
insertarArista(grafo, 6, buscarVertice(grafo, "E"), buscarVertice(grafo, "F"))
insertarArista(grafo, 1, buscarVertice(grafo, "F"), buscarVertice(grafo, "D"))
print("---- Imprimir por amplitud")
imprimirPorAmplitud(grafo, buscarVertice(grafo, "A"))
marcarNoVisitado(grafo)
print("---- Imprimir por profundidad")
imprimirPorProfundidad(grafo, buscarVertice(grafo, "A"))

print("---- Imprimir adyacentes de C")
adyacentes(buscarVertice(grafo, "C"))

marcarNoVisitado(grafo)
print("---- Paso entre C y B")
print(existePaso(grafo, buscarVertice(grafo, "C"), buscarVertice(grafo, "B")))

# ELIMINAREMOS UN VERTICE
eliminarVertice(grafo, "B")

print("---- VERTICES")
imprimirVertices(grafo)

#TAREA ARREGLAR EL ERROR QUE APARECE ACA OJO YO SI SE QUE PASA Y COMO ARREGLARLO
print("---- Imprimir adyacentes")
adyacentes(buscarVertice(grafo, "B"))

