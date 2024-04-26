"""Hacer un función recursiva que muestre todo el árbol del JSON con su
correspondiente indentación segun el nivel de profundidad de las dimensiones de
la matriz del mismo."""

from localidades import data 

INDENT = "    "

def imprimirDiccionario(diccionario, indentacion):
    for k, v in diccionario.items():
        if isinstance(diccionario[k], dict):
            print(INDENT*(indentacion),k,":")
            imprimirDiccionario(diccionario[k], indentacion+1)
        else:
            print(INDENT*indentacion, k, ": ",v)

for local in data["localidades"]:
    print("-"*15)
    imprimirDiccionario(local, 0)



