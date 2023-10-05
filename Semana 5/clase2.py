# Básicamente existen dos tipos de grafos, dirigidos y no dirigidos, 
# comencemos a estudiar el primero de estos también conocido como digrafos. 
# Este es un conjunto G= (V, A) que está compuesto por un conjunto de vértices 
# o nodos V (v1, v2, v3,..., vn) 
# y un conjunto de aristas o arcos A (a1, a2, a3,..., an).

# Camino: en un grafo dirigido en un conjunto de vértices (v1, v2, v3) 
# tal que existen los arcos del camino (v1-v2, v2-v3). 

# Longitud de un camino: es la cantidad de aristas del camino o 
# la cantidad de vértices del camino menos uno. 

# Etiqueta de una arista: es un valor que está asociado a la relación entre dos 
# vértices. 
# Este suele ser un valor numérico que representa tiempo, distancia, 
# cantidades que indican 
# el valor de ir desde el vértice origen al destino, 
# también se lo denomina peso.

# Conexo: un grafo dirigido es conexo si desde cualquier vértice se puede acceder
# a cualquier otro, ya sea de manera directa o indirecta –es decir pasando por nodos
#  intermedios–. 

# Acíclico: un grafo dirigido es acíclico si no tiene ciclos, esto implica que 
# para cada vértice 
# del grafo no exista ningún camino que empiece en un vértice y termine en el
#  mismo 
# –un vértice podría tener un arco a sí mismo y formar un ciclo–.

# Camino hamiltoniano: es un camino que consiste en visitar todos los vértices de 
# grafo pasando solo una vez por cada uno, 
# si además el primer vértices es adyacente de el último el camino también es un ciclo hamiltoniano.

# Camino euleriano: es un camino que consiste en pasar por cada arista del grafo solo 
# una vez –no importa que visite los vértices más de una vez–, 
# asimismo si el vértice de partida es el vértice de llegada el camino es un ciclo euleriano 
# (este último es el famoso problema de los puentes de Königsberg).

# Exploración en profundidad: se comienza por un vértice arbitrariamente, 
# se trata dicho vértice y se lo marca como visitado, 
# luego se trata recursivamente todos los vértices adyacentes no visitados, 
# si al finalizar quedan vértices sin visitar se toma el siguiente vértice sin tratar y 
# se repite el procedimiento. 


# Exploración en amplitud: se crea una cola a la cual se agrega un 
# vértice arbitrariamente 
# y se lo marca como visitado, luego mientras la cola no esté vacía se atiende el primer 
# elemento de la cola y se trata el vértice. 
# A continuación se agregan a la cola y se marcan como visitados todos los vértices 
# adyacentes que aún no hayan sido visitados; cuando la cola queda vacía si aún 
# quedan vértices sin visitar, 
# se toma el siguiente vértice sin tratar y repite el procedimiento anterior.
