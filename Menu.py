from constants import Player1, Player2
from colorama import init, Fore, Style

class UserMenu:

    def __init__(self, board):
        self.board = board
        self.current_player = Player1

    def start(self):
        while not self.board.winner:
            valid = False
            turn = None
            while not valid:
                self.display_board()
                print(f"\nTurno del Jugador {self.current_player}")
                init(autoreset=True)
                choice = input(Fore.WHITE + Style.BRIGHT + "\n¿Qué deseas hacer? (Mover[M] o Eliminar[E]): ").strip().lower()

                if choice == "m":
                    turn = self.move_piece()
                    valid = True
                elif choice == "e":
                    turn = self.delete_square()
                    valid = True
                else:
                    print("\nOpción no válida. Inténtalo de nuevo.")
            if turn == True:
                self.switch_player()

        self.display_winner()

    def move_piece(self):
        try:
            row = int(input("\nIngresa la fila: "))
            col = int(input("\nIngresa la columna: "))
            return self.board._move(self.current_player, row, col)
        except ValueError:
            print("\nPor favor, ingresa valores numéricos válidos para fila y columna.")
            return self.move_piece()

    def delete_square(self):
        try:
            row = int(input("\nIngresa la fila a eliminar: "))
            col = int(input("\nIngresa la columna a eliminar: "))
            return self.board.DeleteSquare(row, col)
        except ValueError:
            print("\nPor favor, ingresa valores numéricos válidos para fila y columna.")
            return self.delete_square()

    def switch_player(self):
        if self.current_player == Player1:
            self.current_player = Player2
        else:
            self.current_player = Player1

    def display_board(self):
        print("\nTablero actual:")
        self.board.PrintBoard()

    def display_winner(self):
        print(f"\n¡Jugador {self.board.winner} ha ganado!")
