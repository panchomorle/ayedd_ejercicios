tablero =[
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
]

turnos= ["▩", "▢"]

def mostrar():
    count = 1
    print("- 1 2 3 4 5 6 7")
    for fila in range(len(tablero)):
        print(count, end=" ")
        for columna in range(len(tablero[fila])):
            print(tablero[fila][columna], end=" ")
        count+=1
        print() ###para el carriage return

def checkWin():
    ##barrido horizontal
    for fila in range(len(tablero)):
        for i in range(4):
            for turno in turnos:
                if(
                    tablero[fila][i+0]==turno and
                    tablero[fila][i+1]==turno and
                    tablero[fila][i+2]==turno and
                    tablero[fila][i+3]==turno
                ):
                    return turno
    ##Barrido vertical
    for fila in range(4):
        for columna in range(len(tablero[fila])):
            for turno in turnos:
                if(
                    tablero[fila+0][columna]==turno and
                    tablero[fila+1][columna]==turno and
                    tablero[fila+2][columna]==turno and
                    tablero[fila+3][columna]==turno
                ):
                    return turno
    ##Barrido diagonal \
    for fila in range(3):
        for columna in range(4):
            for turno in turnos:
                if(
                    tablero[fila+0][columna+0]==turno and
                    tablero[fila+1][columna+1]==turno and
                    tablero[fila+2][columna+2]==turno and
                    tablero[fila+3][columna+3]==turno
                ):
                    return turno

    ##Barrido diagonal /
    for fila in range(3):
        for columna in range(6, 2, -1):
            for turno in turnos:
                if(
                    tablero[fila+0][columna-0]==turno and
                    tablero[fila+1][columna-1]==turno and
                    tablero[fila+2][columna-2]==turno and
                    tablero[fila+3][columna-3]==turno
                ):
                    return turno
    return None

def pisoColumna(col):
    if tablero[0][col]!='.':
        return -1
    
    for fila in range(len(tablero)):
        if tablero[fila][col] != '.':
            return fila-1
    return 5 #última fila
        
def jugar(columnaElegida, turno):
    tablero[pisoColumna(columnaElegida)][columnaElegida] = turno

bucle = True

while bucle:
    for turno in turnos:
        mostrar()
        while True:
            try:
                op = int(input(f"(turno de {turno}) Ingresa la columna: "))
                if(op < 1 or op>7):
                    raise Exception("ingrese un numero valido de columna")
                break
            except Exception as e:
                print(e)
        while True:
            if(pisoColumna(op-1)==(-1)):
                print("ERROR: COLUMNA LLENA")
                mostrar()
                op = int(input(f"(turno de {turno}) Ingresa la columna: "))
            else:
                jugar(op-1, turno)
                break

        if (ganador:=checkWin())!= None:
            mostrar()
            print(f"GANADOR: {ganador}")
            bucle = False
            break
