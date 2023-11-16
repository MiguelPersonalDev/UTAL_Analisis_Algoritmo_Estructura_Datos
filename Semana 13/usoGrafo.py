# Cargaremos el grafo de la imagen

from grafo import *
from pila import *

grafo = Grafo(False)

# INSERTAREMOS PRIMEROS LOS VERTICES
insertarVertice(grafo, "F")
insertarVertice(grafo, "X")
insertarVertice(grafo, "Z")
insertarVertice(grafo, "R")
insertarVertice(grafo, "T")

print("---- TAMAÑO GRAFO")
print(tamanio(grafo))


print("---- VERTICES")
imprimirVertices(grafo)

# INSERTAREMOS LUEGO LAS ARISTAS

insertarArista(grafo, 6, buscarVertice(grafo, "T"), buscarVertice(grafo, "X"))
insertarArista(grafo, 9, buscarVertice(grafo, "X"), buscarVertice(grafo, "Z"))
insertarArista(grafo, 4, buscarVertice(grafo, "Z"), buscarVertice(grafo, "R"))
insertarArista(grafo, 2, buscarVertice(grafo, "R"), buscarVertice(grafo, "F"))
insertarArista(grafo, 3, buscarVertice(grafo, "T"), buscarVertice(grafo, "F"))
insertarArista(grafo, 2, buscarVertice(grafo, "F"), buscarVertice(grafo, "X"))
insertarArista(grafo, 5, buscarVertice(grafo, "R"), buscarVertice(grafo, "X"))
insertarArista(grafo, 8, buscarVertice(grafo, "T"), buscarVertice(grafo, "R"))

# print("---- Imprimir adyacentes de X")
# adyacentes(buscarVertice(grafo, "X"))

# marcarNoVisitado(grafo)
# # print("---- Paso entre C y B")
# # print(existePaso(grafo, buscarVertice(grafo, "R"), buscarVertice(grafo, "Z")))
# marcarNoVisitado(grafo)
print('----->Resultado')
imprimir(dijkstra(grafo,buscarVertice(grafo, "T"), buscarVertice(grafo, "R")))
