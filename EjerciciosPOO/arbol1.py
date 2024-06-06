class Arbol:

    def __init__(self, valor):
        self.left = None
        self.right = None
        self.value = valor
        self.father = None
    
    def left(self, n):
        self.left = n
        n.father = self
        return n

    def right(self, n): #raiz.left(Arbol(18)).right(arbol(9)).etc
        self.right = n
        n.father = self
        return n
    
    def imprimir(self):
        print(self.value)

def inorden(n):
    #pasar por nodo izquierdo
    if(n.left):
        inorden(n.left)
    #visitar nodo
    print(n.value)
    #pasar por nodo derecho
    if(n.right):
        inorden(n.right)

def preorden(n):
    #visitar nodo
    print(n.value)
    #pasar por el izquierdo
    if(n.left):
        preorden(n.left)
    #pasar por el derecho
    if(n.right):
        preorden(n.right)

def postorden(n):
    #pasar por el izquierdo
    if(n.left):
        postorden(n.left)
    #pasar por el derecho
    if(n.right):
        postorden(n.right)
    #visitar nodo
    print(n.value)

def anchura(n):
    if n is None:
        return
    
    nivel = 0
    queue = [n]

    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def rama(raiz, n):
    path = []
    path.append(raiz)
    while raiz != n:
        if raiz.left == n:
            path.append(raiz.left)
            break
        elif raiz.right == n:
            path.append(raiz.right)
            break
        else:
            rama(raiz.left)
            rama(raiz.right)

caminos = [] #print todos los caminos
def print_caminos(n):
    if n == None: return
    global caminos
    caminos.append(n)
    print_caminos(n.left)

    #llega a una hoja, imprime el camino
    if (not n.left and not n.right):
        print(*caminos)

    print_caminos(n.right)
    caminos.remove(n)
        
"""
raiz = Arbol(8)

raiz.left = Arbol(9)
raiz.left.right = Arbol(7)
raiz.left.right.left = Arbol(3)
raiz.left.right.left.left = Arbol(2)
raiz.left.right.right = Arbol(1)
raiz.left.left = Arbol(11)
raiz.left.left.right = Arbol(20)
raiz.left.left.right.left = Arbol(21)
raiz.left.left.left = Arbol(15)
raiz.left.left.left.left = Arbol(19)

raiz.right = Arbol(5)
raiz.right.right = Arbol(12)
raiz.right.right.left = Arbol(17)
raiz.right.right.left.left = Arbol(16)
raiz.right.right.right = Arbol(18)
raiz.right.left = Arbol(6)
raiz.right.left.left = Arbol(4)
raiz.right.left.right = Arbol(14)
raiz.right.left.right.left = Arbol(10)
raiz.right.left.left.left = Arbol(13)
"""
#inorden(raiz)
#anchura(raiz)
#postorden(raiz)
