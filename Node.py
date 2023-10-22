import copy

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.up = None
        self.down = None

    def __deepcopy__(self, memo):
        if id(self) in memo:
            return memo[id(self)]
        new_node = Node(copy.deepcopy(self.value, memo))
        memo[id(self)] = new_node
        new_node.next = copy.deepcopy(self.next, memo)
        new_node.prev = copy.deepcopy(self.prev, memo)
        new_node.up = copy.deepcopy(self.up, memo)
        new_node.down = copy.deepcopy(self.down, memo)
        return new_node
