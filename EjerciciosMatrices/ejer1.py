
##impresion de cada fila
def printMatrizPorFilas(matriz):
    for fila in range(len(matriz)):
        print(matriz[fila])

##impresion de cada elemento
def printMatriz(matriz):
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            print(matriz[fila][col], end=' ')
        print()

def crearMatrizBidimensional(fila: int, columna: int, valor):
    x = [[valor for _ in range(columna)] for _ in range(fila)]
    return x

def crearMatriz2(fila: int, columna: int):
    x = [[0+j for _ in range(columna)] for j in range(fila)]
    return x

def crearMatriz3(fila: int, columna: int):
    x = [[0+i for i in range(columna)] for _ in range(fila)]
    return x

def crearMatriz4(fila: int, columna: int):
    x = []
    cont = 0
    for _ in range(fila):
        z = []
        for _ in range(columna):
            z.append(cont)
            cont+=1
        x.append(z)
    return x

def crearMatriz4Ternaria(fila: int, columna: int):
    x = [[(4*j)+i for i in range(columna)] for j in range(fila)]
    return x

z= crearMatriz4Ternaria(5,4)
printMatriz(z)
