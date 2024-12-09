import re

with open("day07-data.txt", 'r') as file:
    rows = [list(map(int,re.findall(r"(\d+)", row.strip()))) for row in file.readlines()]

############# PART 1 #############

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def putNumbers(self, newNum:int):
        if(self.left is None or self.right is None): 
            self.left = Node(self.data + newNum)
            self.right = Node(self.data * newNum)
        else:
            self.left.putNumbers(newNum)
            self.right.putNumbers(newNum)
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()
    def PrintLeaves(self):
        if(self.left is None or self.right is None): 
            print(self.data)
        else:
            self.left.PrintLeaves()
            self.right.PrintLeaves()
    def getLeafs(self):
        leafs = []
        def _getLeafs(node:Node):
            if node.left is None:
                leafs.append(node.data)
            else:
                _getLeafs(node.left)
                _getLeafs(node.right)
        _getLeafs(self)
        return leafs

def isResultInLeafs(lst):
    root = Node(lst[1])
    for v in lst[2:]:
        root.putNumbers(v)
    return lst[0] if lst[0] in root.getLeafs() else 0

pt1 = 0

for l in rows:
    pt1 += isResultInLeafs(l)

print(pt1)
