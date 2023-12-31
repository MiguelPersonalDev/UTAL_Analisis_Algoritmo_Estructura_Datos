from cola import Cola, arribo, esVacia,atencion

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

def insertarNodo(raiz, info):
    if(raiz is None):
        raiz = nodoArbol(info)
    elif(info < raiz.info):
        raiz.izq = insertarNodo(raiz.izq,info)
    else:
        raiz.der = insertarNodo(raiz.der,info)
    return raiz

def arbolVacio(raiz):
    return raiz is None

def remplazar(raiz):
    aux = None
    if(raiz.der is None):
        aux = raiz
        raiz = raiz.izq
    else:
        raiz.der, aux = remplazar(raiz.der)
    return raiz, aux

def eliminarNodo(raiz,info):
    x = None
    if(raiz is not None):
        if(info<raiz.info):
            raiz.izq, x = eliminarNodo(raiz.izq,info)
        elif(info>raiz.info):
            raiz.der, x = eliminarNodo(raiz.der,info)
        else:
            x=raiz.info
            if(raiz.izq is None):
                raiz = raiz.der
            elif(raiz.der is None):
                raiz = raiz.izq
            else:
                raiz.izq, aux = remplazar(raiz.izq)
                raiz.info = aux.info
    return raiz, x

# def buscar() tarea por ejemplo si existe o no existe retornar el elemento o None

def imprimirInOrden(raiz):
    if(raiz is not None):
        imprimirInOrden(raiz.izq)
        print(raiz.info)
        imprimirInOrden(raiz.der)

def imprimirPreOrden(raiz):
    if(raiz is not None):
        print(raiz.info)
        imprimirPreOrden(raiz.izq)
        imprimirPreOrden(raiz.der)


def imprimirPorNivel(raiz):
    pendientes = Cola()
    arribo(pendientes, raiz)
    while(not esVacia(pendientes)):
        nodo = atencion(pendientes)
        print(nodo.info)
        if(nodo.izq is not None):
            arribo(pendientes,nodo.izq)
        if(nodo.der is not None):
            arribo(pendientes, nodo.der)


# imprimir postOrder tarea

# 

