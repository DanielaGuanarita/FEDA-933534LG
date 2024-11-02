# Combinaciones de juego 
# X = Movimientos jugador uno
# O = Movimientos jugador dos
# _ = Masilla en blanco, no hay movimientos.
board_no_winner = [["X", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
board_winner_rows = [["X", "X", "X"], ["O", "O", "_"], ["_", "_", "_"]]
board_winner_columns = [["O", "X", "_"], ["O", "X", "_"], ["O", "X", "_"]]
board_winner_diagonal = [["X", "O", "_"], ["_", "X", "O"], ["_", "_", "X"]]
board_tie = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
board_in_progress = [["X", "O", "X"], ["_", "O", "_"], ["O", "X", "_"]]
# Método o función para verificar si las combinaciones de usuario son una combinación ganadora
def verify_winner(table):
    pass
# None inicialmente pero debe evaluar cada matriz declarada en la parte superior.
print(verify_winner(None))





# Combinaciones de juego 
# X = Movimientos jugador uno
# O = Movimientos jugador dos
# _ = Casilla en blanco, no hay movimientos.

tablero_no_ganador = [["X", "O", "X"], ["O", "O", "X"], ["X", "X", "O"]]
tablero_ganador_filas = [["X", "X", "X"], ["O", "O", "_"], ["_", "_", "_"]]
tablero_ganador_columnas = [["O", "X", "_"], ["O", "X", "_"], ["O", "X", "_"]]
tablero_ganador_diagonal = [["X", "O", "_"], ["_", "X", "O"], ["_", "_", "X"]]
tablero_empate = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]
tablero_en_progreso = [["X", "O", "X"], ["_", "O", "_"], ["O", "X", "_"]]


def verificar_ganador(tablero):
    
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] and fila[0] != "_":
            return f"Ganador: {fila[0]}"
    
    
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] and tablero[0][columna] != "_":
            return f"Ganador: {tablero[0][columna]}"
    
    
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "_":
        return f"Ganador: {tablero[0][0]}"
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "_":
        return f"Ganador: {tablero[0][2]}"
    
    
    for fila in tablero:
        if "_" in fila:
            return "Juego en progreso"
    
    return "Empate"


print(verificar_ganador(tablero_no_ganador))   
print(verificar_ganador(tablero_ganador_filas))     
print(verificar_ganador(tablero_ganador_columnas))
print(verificar_ganador(tablero_ganador_diagonal)) 
print(verificar_ganador(tablero_empate))              
print(verificar_ganador(tablero_en_progreso))     
