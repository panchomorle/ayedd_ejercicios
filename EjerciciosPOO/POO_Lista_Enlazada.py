print("Ejemplo básico de Listas enlazadas con POO en Python")
print("---")

class Letra:
    def __init__(self, letra):
        self.letra = letra
        self.siguiente_letra = None
    
raiz = Letra("A")

raiz.siguiente_letra = Letra("B")

raiz.siguiente_letra.siguiente_letra = Letra("C")

def mostrar_lista(x):
    while x != None:
        print(x.letra)
        x = x.siguiente_letra

#mostrar_lista(raiz)
   
    
"""
Práctica:
---------
1) Hacer una función para agregar un elemento más al final de la lista
2) Hacer una función para sacar un elemento al final de la lista
3) Hacer una función para sacar un elemento al comienzo de la lista
4) Hacer una función para sacar un elemento en la posición x de la lista
   (reenlazar los objetos detrás)
5) Hacer una función para agregar un elemento más en la posición x de la lista
6) Hacer una función para sacar un elemento en la posición x de la lista
(reenlazar los objetos detrás)
7) Una empresa de transporte de carga que cuenta con vehículos propios
así como vehículos tercerizados organiza su sistema financiero en
centros de costo, donde cada centro de costo puede tener varios
vehículos agregados u otros centros de costo. Un vehículo pertenece a
un centro de costo, y es el único que genera gastos y facturación. Un
centro de costo representa a una empresa de terceros o la propia
empresa que gestiona todas las demás.
a. Haga una representación gráfica de esta estructura
organizacional, utilizando listas enlazadas para que pueda
calcular los gastos/facturación para toda la organización, así
como para un único centro de costos.
b. Haga una función recursiva para calcular el facturación de la
organización.  
"""
def agregar_al_final(raiz: Letra, obj: Letra):
    x = raiz
    while x.siguiente_letra != None:
        x=x.siguiente_letra
    else:
        x.siguiente_letra = obj

def eliminar_al_final(raiz: Letra):
    x = raiz
    while x.siguiente_letra.siguiente_letra != None:
        x=x.siguiente_letra
    else:
        x.siguiente_letra = None

agregar_al_final(raiz, Letra("D"))

def agregar_al_principio(obj: Letra):
    global raiz
    obj.siguiente_letra= raiz
    raiz = obj

def eliminar_principio():
    global raiz
    raiz = raiz.siguiente_letra

#4
def eliminar(pos: int):
    global raiz

    if(pos<0):
        print("posicion invalida")
        return None

    x = raiz
    cont = 0
    anterior = None

    while cont < pos and x.siguiente_letra != None:
        anterior = x
        x = x.siguiente_letra
        cont+=1

    if(pos== 0):
        raiz= raiz.siguiente_letra
    elif x.siguiente_letra == None:
        anterior.siguiente_letra = None
    else:
        anterior.siguiente_letra = x.siguiente_letra

#5
def agregar(obj: Letra, pos: int):
    global raiz

    if(pos<0):
        print("posicion invalida")
        return None

    x = raiz
    cont = 0
    anterior = None

    while cont < pos and x.siguiente_letra != None:
        anterior = x
        x = x.siguiente_letra
        cont+=1

    if(pos== 0):
        obj.siguiente_letra = raiz
        raiz= obj
    elif x.siguiente_letra == None:
        x.siguiente_letra = obj
    else:
        anterior.siguiente_letra = obj
        obj.siguiente_letra = x


agregar_al_principio(Letra("Z"))
mostrar_lista(raiz)

agregar(Letra("J"), 2)
mostrar_lista(raiz)

