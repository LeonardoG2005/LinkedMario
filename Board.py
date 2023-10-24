from constants import Player1, Player2
from copy import deepcopy
from matrix import MatrixLinkedList

class Board:

  def __init__(self, n):

      self.winner = None
      self.rows = self.cols = n
      self.initBoard(n)

  def initBoard(self, n):
      self.board = MatrixLinkedList(n, n)

      self.board.set_value(0, n//2, Player1)
      self.board.set_value(n-1, n//2, Player2)

      #self.board.print_matrix()
      print()

  def reset(self):
      self.initBoard()

  def DeleteSquare(self, row, col):
      if not(0<=row<self.rows and 0<=col<self.rows):
         print("La casilla ingresada NO EXISTE")
         return False
      if self.verifyDelete(row, col):
        print("Borrado correctamente")
        self.board.set_value(row, col, "🧱")
        return True
      else:
        print("No posible 🦁")
        return False

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
        print("\nMovimiento inválido... (grave)")
        return False
      
      if (player == Player1 and row == self.rows - 1) or (player == Player2 and row == 0):
        self.winner = player

      return True #creo

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
          if col == 0 and node.next  == target_node:
            return False
          if not (node.next.value) and node.next == target_node:
            return True

        if node.prev:
          if col == self.cols - 1:
            return False
          if not (node.prev.value) and node.prev == target_node:
            return True
      else:
        print("grave......")

  def deleteEdges(self, AuxBoard):

    for j in range(AuxBoard.rows - 1):
        lastNodeOfRow = AuxBoard.get_node(j, AuxBoard.cols - 1)
        nextNode = lastNodeOfRow.next

        # Verificar que nextNode no sea None antes de quitar los enlaces
        if nextNode:
            if nextNode.prev:
                nextNode.prev.next = None
            if nextNode.prev:
                nextNode.prev = None


  def verifyDelete(self, row, col):

      Auxboard = deepcopy(self.board)

      #Se borra la casilla, y se verifica si es posible...

      Auxboard.set_value(row, col, "🧱")
      self.deleteEdges(Auxboard)

      player1 = Auxboard.get_node_by_value(Player1)
      player2 = Auxboard.get_node_by_value(Player2)

      #print(self.verifyPathUp(player2))
      #print(self.verifyPathDown(player1))

      
      result = self.verifyPathUp(player2) and self.verifyPathDown(player1)
      del Auxboard.head
      del Auxboard
      return result

  def verifyPathUp(self, node, l = []):

    if node in l:
      return False
    if not node:
      return False
    if node.value == "🧱":
      return False
    if not node.up:
      return True

    l.append(node)

    return self.verifyPathUp(node.up, l) or self.verifyPathUp(node.prev, l) or self.verifyPathUp(node.next, l) or self.verifyPathUp(node.down, l)

  def verifyPathDown(self, node, l = []):

    if node in l:
      return False
    if not node:
      return False
    if node.value == "🧱":
      return False
    if not node.down:
      return True
    
    l.append(node)

    return self.verifyPathDown(node.up, l) or self.verifyPathDown(node.prev, l) or self.verifyPathDown(node.next, l) or self.verifyPathDown(node.down, l)