
"""
some notes:
AAAA -> 3, 2-2, 2-2, 3-2
  v
EEE		
E	  -> edges: 0,1, -1,-1, -1,-1, 1,0 -> 0,2, -1,-1, 2,2, -1,-1 -> 0,3, 1,4, 2,3 -> 2,2, 3,1, 2,0
          -> normal: 2       -> 2 	 -> 3		  -> 3

input: (0,1, 1,0 -> 0,2, 2,2 -> 0,3, 1,4, 2,3 -> 2,2, 3,1, 2,0



EEE corners[(0,0), (0,2), (2,2), (2,0)]  
E		1,2 when x == newY update så: corners[(0,0), (0,3), (2,3), (2,0)]
		2,1 when newY == y update så: corners[(0,0), (0,3), (3,3), (3,0)]

"""

from collections import defaultdict
import time

start_time = time.time()
with open("day12-smallE.txt", 'r') as file:
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
        a,b,c = k
        if a != 'E':continue
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
# # print_twoDArr(twoDArr)
# # print_map(map)

# # visited = []
# # def get_perimeter_of_key(map,keyTup):
# #     global visited
# #     if keyTup in visited:
# #         return (0,0)
# #     perimeter = 0
# #     prevLen = len(visited) # later used for getting amount of plants in region
# #     visited.append(keyTup)
# #     char,y1,x1 = keyTup
# #     for (plant,y2,x2) in map[keyTup]:
# #         if char != plant:
# #             perimeter += 1
# #         if char == plant: #and (plant,y2,x2) not in visited:
# #             perimeter += get_perimeter_of_key(map,(plant,y2,x2))[1]
# #     return (len(visited)-prevLen,perimeter)

# # pt1 = 0
# # for (char,y1,x1) in map.keys():
# #     tup1,tup2 = get_perimeter_of_key(map,(char,y1,x1))
# #     pt1 += tup1*tup2

# # print(f"pt1: {pt1}, Time: {time.time() - start_time}")


print_map(map)
print_twoDArr(twoDArr)

visited = []
def get_perimeter_list_of_key(map,keyTup):
    global visited
    if keyTup in visited:
        return (0,[])
    perimeter = []
    prevLen = len(visited) # later used for getting amount of plants in region
    nextPlant = [keyTup]
    visited.append(keyTup)
    char,y1,x1 = keyTup
    for x in nextPlant:
        whatever = []
        for (plant,y2,x2) in map[x]:
            if char == plant: #and (plant,y2,x2) not in visited:
                whatever.append((-1,-1))
                if (plant,y2,x2) not in visited:
                    nextPlant.append((plant,y2,x2))
                    visited.append((plant,y2,x2))
                continue
            whatever.append((y2,x2))
        perimeter.append(whatever)

    return (len(visited)-prevLen,perimeter)

# # # regionB = get_perimeter_list_of_key(map,('E',1,1))[1]
# # # print("AAAAAAAAAAAAAAA")
# # # print_twoDArr(regionB)
# # # print("AAAAAAAAAAAAAAA")

# # # # # def input(lst):
# # # # #     res = 0
# # # # #     for l in lst:
            
# # # # # testArr = [[(0,1), (-1,-1), (-1,-1), (1,0)], [(0,2), (-1,-1), (2,2), (-1,-1),], [(0,3), (1,4), (2,3), (-1,-1),], [(-1,-1), (2,2), (3,1), (2,0)]]

# # # # # print_twoDArr(testArr)

# # # def rotate_2d_arr(twoDArr):
# # #     return [list(v) for v in zip(*twoDArr)]

# # # regionB = rotate_2d_arr(regionB)
# # # print_twoDArr(regionB)

# # # def get_perimeter_of_region(lst):
# # #     newPerimeter = 0
# # #     for tupList in lst:
# # #         startTup1,startTup2 = tupList[0]
# # #         for i,(tup1,tup2) in enumerate(tupList):
# # #             if tup1 == -1: continue
# # #             # elif startTup1 == -1: continue
# # #             if startTup1 == tup1 and abs(tup2-startTup2) == 1:
# # #                 startTup1,startTup2 = tupList[i]
# # #             elif startTup2 == tup2 and abs(tup1-startTup1) == 1:
# # #                 startTup1,startTup2 = tupList[i]
# # #             elif startTup1 == -1:
# # #                 startTup1,startTup2 = tupList[i]
# # #                 newPerimeter +=1
# # #             else: newPerimeter += 1
# # #     return newPerimeter

# print(get_perimeter_of_region(regionB))

# print(get_perimeter_list_of_key(map,('A',1,1))[1])

# """
# regionB = get_perimeter_list_of_key(map,('C',2,3))[1]

# print(regionB)

# regionB = rotate_2d_arr(regionB)

# get_perimeter_of_region(regionB)

# """

# pt2 = 0
# for (char,y1,x1) in list(map):
#     print(f"char y1 x2: {char,y1,x1}")
#     amount,fence = get_perimeter_list_of_key(map,(char,y1,x1))

#     fence = rotate_2d_arr(fence)

#     pt2 += amount*get_perimeter_of_region(fence)

# print(f"pt1: {pt2}, Time: {time.time() - start_time}")
