class Node:
    def __init__(self, name, cost, parent):
        self.name = name
        self.parent = parent
        self.cost = cost

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
    def __eq__(self, object) -> bool:
        # if self.__class__ != object.__class__:
        #      return False
        return self.name == object.name
    
    def __hash__(self) -> int:
        return hash(self.name)


class GCostNode(Node):
    def __init__(self, name, cost, parent):
        super().__init__(name, cost, parent)
        self.gcost = 0
    def __lt__(self, other):
        return self.gcost < other.gcost
    def __le__(self, other):
        return self.gcost <= other.gcost

class FCostNode(Node):
    def __init__(self, name, cost, parent):
        super().__init__(name, cost, parent)
        self.gcost = 0
        self.fcost = 0
        
    def __lt__(self, other):
        return self.fcost < other.fcost
    def __le__(self, other):
        return self.fcost <= other.fcost