"""
2. Crear una función que verifica se existe alguna línea llena de caracteres iguales
3. Crear una función que verifica se existe alguna columna llena de caracteres iguales
4. Crear una función que verifica se existe alguna diagonal llena de caracteres iguales,
considere solamente matrices cuadráticas, y verifique la diagonal principal y secundaria."""

x =[
    ['X', 'X', '.', '.', '.', 'O', 'X'],
    ['.', 'X', '.', '.', '.', 'X', '.'],
    ['.', '.', 'O', '.', 'X', 'O', '.'],
    ['X', 'X', 'O', 'X', 'X', 'O', 'X'],
    ['.', '.', 'X', 'O', 'X', 'O', '.'],
    ['.', 'X', '.', '.', 'X', 'X', '.'],
    ['X', '.', '.', '.', 'X', 'X', 'X'],
]

def checkFilas(tablero):
    for fila in range(len(tablero)):
        selected = tablero[fila][0]
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

def checkDiagonales(tablero):
    selected = tablero[0][0]
    for i in range(len(tablero)):
        if tablero[i][i] == selected:
            coincidence = True
        else:
            coincidence = False
            break

    if coincidence:
        return coincidence
    ##diagonal secundaria:
    last_index = len(tablero)-1
    cont = 0
    selected = tablero[0][last_index]
    for i in range(last_index, -1, -1):
        if tablero[cont][i] == selected:
            coincidence = True
            cont+=1
        else:
            coincidence = False
            break
    return coincidence
        
print(checkDiagonales(x))