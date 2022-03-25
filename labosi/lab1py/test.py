from node import Node

n1 = Node("a", 0, None)
n1.tcost = 0

n2 = Node("a", 0, None)
n2.tcost = 2

clsopn = set()
clsopn.add(n1)

if (n2 in clsopn):
    print(True)
    exit()
print(False)