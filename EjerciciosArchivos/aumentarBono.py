#import copy
def printMatriz(matriz): #funcion para printear una matriz
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            print(matriz[fila][col], end=' ')
        print()

matriz = []
with open(r'U10\curso.csv', "r", encoding='utf8') as archivo:
    line = None
    while line != '':
        line = archivo.readline().strip() #leo una linea sacandole los espacios del principio y final
        if line != '':
            matriz.append([item for item in line.split(",")])
            #esto tambien se puede hacer asi:
            #matriz.append(line.split(","))
            #pero lo dejo para que se entienda que agrego un array

"""
matriz_mod = copy.deepcopy(matriz)
for fila in range(len(matriz_mod)-1):
    last_col = len(matriz_mod[fila])-1
    matriz_mod[fila][last_col] = str(round(float(matriz_mod[fila][last_col])*1.13, 2))
"""
printMatriz(matriz)
print("-"*40)

for alum in matriz:
    alum[4] = str(round(float(alum[4])*1.13, 2))
    
printMatriz(matriz)

matriz_ordenada = sorted(matriz, key= lambda x:  float(x[len(x)-1]) )
print("-"*40)
printMatriz(matriz_ordenada)

with open(r'EjerciciosArchivos\bono_actualizado.csv', 'w') as archivo:
    for alum in matriz:
        archivo.write(",".join(alum) + "\n")

with open(r'EjerciciosArchivos\ordenados_por_bono.csv', 'w') as archivo:
    for alum in matriz_ordenada:
        archivo.write(",".join(alum) + "\n")