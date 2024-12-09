import re

with open("day07-data.txt", 'r') as file:
    rows = [list(map(int,re.findall(r"(\d+)", row.strip()))) for row in file.readlines()]

def isResultInLeafs(Tree,lst):
    root = Tree(lst[1])
    for v in lst[2:]:
        root.putNumbers(v)
    return lst[0] if lst[0] in root.getLeafs() else 0

############# PART 1 #############
class TreeForPart1:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def putNumbers(self, newNum:int):
        if(self.left is None): 
            self.left = TreeForPart1(self.data + newNum)
            self.right = TreeForPart1(self.data * newNum)
        else:
            self.left.putNumbers(newNum)
            self.right.putNumbers(newNum)
    def getLeafs(self):
        leafs = []
        def _getLeafs(node:TreeForPart1):
            if node.left is None:
                leafs.append(node.data)
            else:
                _getLeafs(node.left)
                _getLeafs(node.right)
        _getLeafs(self)
        return leafs
    
pt1 = 0
for l in rows:
    pt1 += isResultInLeafs(TreeForPart1,l)
print(f"pt1: {pt1}")

############# PART 2 #############
class TreeForPart2:
    def __init__(self, data):
        self.left = None
        self.mid = None
        self.right = None
        self.data = data
    def putNumbers(self, newNum:int):
        if(self.left is None): 
            self.left = TreeForPart2(self.data + newNum)
            self.mid = TreeForPart2(int(str(self.data) + str(newNum)))
            self.right = TreeForPart2(self.data * newNum)
        else:
            self.left.putNumbers(newNum)
            self.mid.putNumbers(newNum)
            self.right.putNumbers(newNum)
    def getLeafs(self):
        leafs = []
        def _getLeafs(node:TreeForPart2):
            if node.left is None:
                leafs.append(node.data)
            else:
                _getLeafs(node.left)
                _getLeafs(node.mid)
                _getLeafs(node.right)
        _getLeafs(self)
        return leafs
    
pt2 = 0
for l in rows:
    pt2 += isResultInLeafs(TreeForPart2,l)
print(f"pt2: {pt2}")
