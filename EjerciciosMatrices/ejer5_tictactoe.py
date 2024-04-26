"""
5. Crear un Tic-tac-toe juego donde el usuario empieza configurando el tamaño del tablero y el
símbolo de sus piezas. El juego debe alternar entre los jugadores hasta tener un ganador o
tablero lleno.
"""
def crearTablero(size):
    x = [["." for _ in range(size)] for _ in range(size)]
    return x

def printTablero(tab):
    print("+", end=" ")
    for i in range(len(tab[0])):
        print(i, end=" ")
    print() 
    for fila in range(len(tab)):
        print(fila, end=" ")
        for col in range(len(tab[fila])):
            print(tablero[fila][col], end=" ")
        print()

def setTurnos():
    turnos = [input(f"Ingrese el simbolo {i+1}: ") for i in range(2)]
    return turnos

def lugarVacio(fil, col):
    if tablero[fil][col] == ".":
        return True
    return False

def checkFilas(tablero):
    for fila in range(len(tablero)):
        selected = tablero[fila][0]
        if selected == ".":
            return False
        global coincidence
        coincidence = False
        for col in range (len(tablero[fila])):
            if tablero[fila][col] == selected:
                coincidence = True
            else:
                coincidence = False
                break
        if coincidence:
            return True
    return False

def checkColumnas(tablero):
    for col in range (len(tablero[0])):
        selected = tablero[0][col]
        if selected == ".":
            return False
        global coincidence
        coincidence = False
        for fila in range(len(tablero)):
            if tablero[fila][col] == selected:
                coincidence = True
            else:
                coincidence = False
                break
        if coincidence:
            return True
    return False

def diagonalPrincipal(tablero):
    selected = tablero[0][0]
    if selected == ".":
        return False
    for i in range(len(tablero)):
        if tablero[i][i] == selected:
            coincidence = True
        else:
            coincidence = False
            break
    return coincidence
def diagonalSecundaria(tablero):
    ##diagonal secundaria:
    last_index = len(tablero)-1
    cont = 0

    selected = tablero[0][last_index]
    if selected == ".":
        return False
    for i in range(last_index, -1, -1):
        if tablero[cont][i] == selected:
            coincidence = True
            cont+=1
        else:
            coincidence = False
            break
    return coincidence

def checkDiagonales(tablero):
    return diagonalPrincipal(tablero) or diagonalSecundaria(tablero)

tam = int(input("Ingrese el tamaño del tablero: "))
tablero = crearTablero(tam)
global turnos
turnos = setTurnos()
bucle= True

while bucle:
    for turno in turnos:
        while bucle:
            printTablero(tablero)
            try:
                opfil = int(input(f"Ingresa la fila para {turno}: "))
                opcol = int(input(f"Ingresa la columna para {turno}: "))
                print("-"*20)
                if lugarVacio(opfil, opcol):
                    tablero[opfil][opcol] = turno
                    if checkColumnas(tablero) or checkFilas(tablero) or checkDiagonales(tablero):
                        printTablero(tablero)
                        print(f"El ganador es: {turno}")
                        bucle = False
                    break
                else:
                    print(f"No puedes poner un(a) {turno} ahí.")
            except Exception as e:
                print(e)


