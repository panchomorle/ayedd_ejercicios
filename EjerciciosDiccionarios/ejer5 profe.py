"""Hacer un función recursiva que muestre todo el árbol del JSON con su
correspondiente indentación segun el nivel de profundidad de las dimensiones de
la matriz del mismo."""

from localidades import data

INDENT = "    "

def imprimirDiccionario(diccionario, indentacion=0):
    for k, v in diccionario.items():
        if isinstance(diccionario[k], dict):
            print(INDENT*(indentacion),k,":")
            imprimirDiccionario(diccionario[k], indentacion+1)

        elif isinstance(diccionario[k], list):
            print(INDENT*(indentacion),k,":")
            for elem in diccionario[k]:
                print(INDENT*(indentacion+1)+"-"*15)
                imprimirDiccionario(elem, indentacion+1)

        else:
            print(INDENT*indentacion, k, ": ",v)

imprimirDiccionario(data)



