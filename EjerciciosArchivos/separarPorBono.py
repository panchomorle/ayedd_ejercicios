"""● Tiene 4 campos: el nro de alumno, apellido y nombre,
email y bono de fin de año.
● Generar 2 archivos: 1 uno con quienes el bono menor de
$10000 y otro con el resto."""
def printMatriz(matriz): #funcion para printear una matriz
    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            print(matriz[fila][col], end=' ')
        print()

matriz = []
with open(r"U10\curso.csv", "r", encoding="utf8") as archivo:
    linea = None
    while linea != '':
        linea = archivo.readline().strip()
        if linea != '':
            matriz.append(linea.split(","))

printMatriz(matriz)

with open("EjerciciosArchivos/menores10mil.csv", "w", encoding="utf8") as archivo:
    for alum in matriz:
        if float(alum[4]) < 10000:
            archivo.write(",".join(alum)+"\n")

with open("EjerciciosArchivos/mayores10mil.csv", "w", encoding="utf8") as archivo:
    for alum in matriz:
        if float(alum[4]) > 10000:
            archivo.write(",".join(alum)+"\n")

#with open(r'U10\curso.csv', "r", encoding="utf-8") as archivo:
#   linea = arch