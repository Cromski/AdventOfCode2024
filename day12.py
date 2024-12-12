from collections import defaultdict
import time

start_time = time.time()
with open("day12-data.txt", 'r') as file:
    twoDArr = [list("@"+row.strip()+"@") for row in file.readlines()]

#add padding
padding = ["@" for c in twoDArr[0]]
twoDArr.insert(0,padding)
twoDArr.append(padding)

#prints
def print_twoDArr(twoDArr):
    for row in twoDArr:
        print(row)
def print_map(map):
    for k in map.keys():
        print(f"{k} -> {map[k]}")

map = defaultdict(list)

def addEdge(graph,key,keyY,keyX,value,valueY,valueX): #graph, key, keyY, keyX, value, valueY, valueX
    graph[(key,keyY,keyX)].append((value,valueY,valueX))

def construct_map(twoDArr):
    for i, row in enumerate(twoDArr[1:-1],1):
        for j, c in enumerate(row[1:-1],1):
            addEdge(map,c,i,j,twoDArr[i-1][j],i-1,j) # up
            addEdge(map,c,i,j,twoDArr[i][j+1],i,j+1) # right
            addEdge(map,c,i,j,twoDArr[i+1][j],i+1,j) # down
            addEdge(map,c,i,j,twoDArr[i][j-1],i,j-1) # left

construct_map(twoDArr)
# print_twoDArr(twoDArr)
# print_map(map)

visited = []
def get_perimeter_of_key(map,keyTup):
    global visited
    if keyTup in visited:
        return (0,0)
    perimeter = 0
    prevLen = len(visited) # later used for getting amount of plants in region
    visited.append(keyTup)
    char,y1,x1 = keyTup
    for (plant,y2,x2) in map[keyTup]:
        if char != plant:
            perimeter += 1
        if char == plant: #and (plant,y2,x2) not in visited:
            perimeter += get_perimeter_of_key(map,(plant,y2,x2))[1]
    return (len(visited)-prevLen,perimeter)

pt1 = 0
for (char,y1,x1) in map.keys():
    tup1,tup2 = get_perimeter_of_key(map,(char,y1,x1))
    pt1 += tup1*tup2

print(f"pt1: {pt1}, Time: {time.time() - start_time}")

# print(get_perimeter_of_key(map,('B',2,1)))
