############### Vocabulario

# Raíz: es el nodo que se encuentra en la parte superior del árbol, 
# mediante el cual se accede al árbol.

# Hijo: es un nodo que depende directamente de otro, 
# es decir está conectado mediante una flecha que llega. Todos, menos el nodo raíz.

# Padre: es aquel nodo del que depende al menos un nodo hijo, 
# es decir que los hijos son aquellos nodos a los que apuntan 
# las flechas que salen de este. 

# Hermanos: son el conjunto de nodos que tienen el mismo padre.

# Descendientes: los descendientes de un nodo son todos aquellos nodos que pertenecen
# a los subárboles de los hijos de dicho nodo.

# Ancestros: los ancestros de un nodo, son todos aquellos nodos en el camino desde la raíz a dicho nodo.

# Hoja: son todos los nodos que no tienen hijos, se ubican en la parte superior del árbol, 
# pero pueden estar en distintos niveles

# Nodo interno: son todos aquellos nodos que tienen al menos un hijo, 
# a excepción de la raíz.

# Grado de un nodo: es el número de subárboles de dicho nodo

# Rama: es la conexión entre dos nodos, también es llamado enlace.

# Grado de un árbol: es el grado (o aridad) máximo de todos los nodos del árbol, 
# es decir la cantidad máxima de hijos que tiene alguno de los nodos del árbol. 

# Camino: es una secuencia de nodos desde un nodoj a un nodok –distintos entre sí– 
# de modo que exista una rama que conecte cada par de nodos –siempre en sentido descendente–, 
# su longitud es el número de ramas que contiene. Además cada nodo del árbol a excepción del nodo raíz
# puede ser accedido desde este último mediante un camino único a través de una secuencia de ramas.
# Si existe un camino entre un nodo j y un nodo k , entonces nodo j es un ancestro de nodo k 
# y nodo k es un descendiente de nodo j.

# Nivel de un nodo: se define por el número de ramas entre dicho nodo y la raíz más uno.

# Altura de un nodo: es el número de ramas del camino más largo entre ese nodo y una hoja

# Profundidad de un nodo: es el número de ramas desde la raíz del árbol hasta dicho nodo



# Solucion Colas con prioridad ->

# Si bien se podría dar solución de manera sencilla al uso de colas de prioridad 
# sin alterar demasiado el TDA, para lo cual deberíamos mover al final todos los elementos que tengan prioridad mayor 
# o igual al nuevo elemento, luego insertar el nuevo elemento y después el resto de los elementos que quedaron 
# pendientes en la cola