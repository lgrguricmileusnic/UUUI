class Node:
    def __init__(self, name, cost, parent):
        self.name = name
        self.parent = parent
        self.cost = cost

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name