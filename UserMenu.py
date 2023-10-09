from Board import Board
from Node import Node
class UserMenu:

    def __init__(self, board):
        self.board = board
        self.current_player = "A"

    def start(self):
        while not self.board.winner:
            self.display_board()
            print(f"Turno del Jugador {self.current_player}")
            choice = input("¿Qué deseas hacer? (Mover[M] o Eliminar[E]): ").strip().lower()

            if choice == "m":
                self.move_piece()
            elif choice == "e":
                self.delete_square()
            else:
                print("Opción no válida. Inténtalo de nuevo.")

            self.switch_player()

        self.display_winner()

    def move_piece(self):
        row = int(input("Ingresa la fila: "))
        col = int(input("Ingresa la columna: "))
        self.board._move(self.current_player, row, col)

    def delete_square(self):
        row = int(input("Ingresa la fila a eliminar: "))
        col = int(input("Ingresa la columna a eliminar: "))
        self.board.DeleteSquare(row, col)

    def switch_player(self):
        if self.current_player == "A":
            self.current_player = "B"
        else:
            self.current_player = "A"

    def display_board(self):
        print("Tablero actual:")
        self.board.PrintBoard()

    def display_winner(self):
        print(f"¡Jugador {self.board.winner} ha ganado!")
