from Linkedmatrix import MatrixLinkedList
from Node import Node

class Board:

  def __init__(self, n):
      self.winner = None
      self.rows = self.cols = n
      self.initBoard(n)

  def initBoard(self, n):
      self.board = MatrixLinkedList(n, n)

      self.board.set_value(0, n//2, "A")
      self.board.set_value(n-1, n//2, "B")

      self.board.print_matrix()
      print()

  def reset(self):
      self.initBoard()

  def DeleteSquare(self, row, col):
      self.board.set_value(row, col, "#")

  def PrintBoard(self):
      self.board.print_matrix()
      print()

  def _move(self, player, row, col):

      if self.MoveIsValid(player, row, col):
        target_node = self.board.get_node(row, col)
        node = self.board.get_node_by_value(player)

        #Mover la pieza:
        target_node.value = node.value
        node.value = None

      else:
        print("grave...")
        print()
        return;

      if (player == "A" and row == self.rows - 1) or (player == "B" and row == 0):
        self.winner = player

  def MoveDirection(self, piece, row, col):
      target_node = self.board.get_node(row, col)
      node = self.board.get_node_by_value(piece)

      if node and target_node:

        if node.up == target_node:
          return "up"

        if node.down == target_node:
            return "down"

        if node.next == target_node:
          return "right"

        if node.left == target_node:
          return "left"

  def MoveIsValid(self, piece, row, col):

    target_node = self.board.get_node(row, col)
    node = self.board.get_node_by_value(piece)

    if node and target_node:
      if target_node.value:
        return False

      if node.up:
        if not (node.up.value) and node.up == target_node:
          return True

      if node.down:
        if not (node.down.value) and node.down == target_node:
          return True

      if node.next:
        if not (node.next.value) and node.next == target_node:
          return True

      if node.prev:
        if not (node.prev.value) and node.prev == target_node:
          return True
    else:
      print(":))))))))))))))))))")