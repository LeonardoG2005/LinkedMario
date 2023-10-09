from Node import Node

class MatrixLinkedList:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.head = None
        self.build_matrix()

    def build_matrix(self):

        # Primero se crean las LinkedLists que represetan las filas...
        self.head = Node(None)
        current = self.head

        for i in range(self.rows):

          for i in range(self.cols):
            new_node = Node(None)
            new_node.prev = current
            current.next = new_node
            current = new_node

        #Ahora se hacen los enlaces up y down...

        for i in range(self.rows - 1):
          for j in range (self.cols):
            up_position = j + 1 + (self.cols)*i

            up_node = self.get_node_col(up_position)
            
            down_node = self.get_node_col(up_position + self.cols)

            up_node.down = down_node
            down_node.up = up_node

    def get_node_col (self, col):

        current = self.head
        for _ in range(col-1):
            current = current.next

        return current

    # Importante --> Aquí falta que se dispare una excepción OutOfRange cuando se intenta acceder
    # a un nodo que NO es parte de la matriz (por ejemplo : el self.head.up no debería ser accesible ...)
    def get_node(self, row, col):

        if 0 <= row < self.rows and 0 <= col < self.cols:
            current = self.head

            for _ in range(col):
                current = current.next

            for _ in range(row):
                current = current.down

            return current


    def __getitem__(self, index):
          row, col = index
          node = self.get_node(row, col)
          if node:
              return node.value
          else:
              raise IndexError("Índices fuera de rango")


    def set_value(self, row, col, value):

        node = self.get_node(row, col)
        if node:
            node.value = value

    def get_node_by_value(self, target_value):

        current = self.head

        while current:
            if current.value == target_value:
                return current
            current = current.next

        return None


    def print_matrix(self):
        for row in range(self.rows):
            current = self.get_node(row, 0)
            row_values = []

            for _ in range(self.cols):
                if current.value:
                  row_values.append(" "+str(current.value))
                else:
                  row_values.append(" "+str(0))
                current = current.next

            print(" ".join(row_values))
