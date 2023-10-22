from board import Board
from Menu import UserMenu

def main():

    board = Board(5)
    Menu = UserMenu(board)
    Menu.start()

if __name__ == "__main__":
    main()
