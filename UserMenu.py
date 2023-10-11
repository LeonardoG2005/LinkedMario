from Board import Board
from Node import Node
class UserMenu:

    def __init__(self, board):
        self.board = Board(board)
        self.current_player = "X"

    def start(self):
        while not self.board.winner:
            self.display_board()
            print(f"Turno del Jugador {self.current_player}")
            choice = input("¿Qué deseas hacer? (Mover[M] o Eliminar[E]): ").strip().lower()

            if choice == "m":
                if self.move_piece():
                    self.switch_player()
                else:
                    print(f"Jugador {self.current_player} Repite turno")
            elif choice == "e":
                if self.delete_square():
                    self.switch_player()
                else:
                    print(f"Jugador {self.current_player} Repite turno")
            else:
                print(f"Opción no válida. Inténtalo de nuevo. Jugador {self.current_player} Repite turno")

            #self.switch_player()

        self.display_winner()

    def move_piece(self):
        row = int(input("Ingresa la fila: "))
        col = int(input("Ingresa la columna: "))
        return self.board._move(self.current_player, row, col)

    def delete_square(self):
        row = int(input("Ingresa la fila a eliminar: "))
        col = int(input("Ingresa la columna a eliminar: "))
        return self.board.DeleteSquare(row, col)

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "Y"
        else:
            self.current_player = "X"

    def display_board(self):
        print("Tablero actual:")
        self.board.PrintBoard()

    def display_winner(self):
        print(f"¡Jugador {self.board.winner} ha ganado!")
        self.display_board()
