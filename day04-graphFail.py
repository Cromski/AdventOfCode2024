from collections import defaultdict
# type keyVal = tuple[int, string]

with open("day04-small.txt", 'r') as file:
    rows = [row.strip() for row in file.readlines()]

graph = defaultdict(list)

def addEdge(graph,mainV,p1,p2,v1,v2):
    if(v1 < 0 or v2 < 0 or v1 >= len(rows) or v2 >= len(rows[p1])):
        return
    graph[(int(str(p1)+str(p2)),mainV)].append((int(str(v1)+str(v2)),rows[v1][v2]))

def findNextKey(graphList, letter):
    listWithLetter = []
    for (i,k) in graphList:
        if (letter == k):
            listWithLetter.append((i,k))
    return listWithLetter

print(rows)

for i,v in enumerate(rows):
    for j,w in enumerate(v):
        print(f"i: {i}. v: {v}. j: {j}. w: {w}.")
        addEdge(graph, w, i, j, i-1, j-1)
        addEdge(graph, w, i, j, i-1, j)
        addEdge(graph, w, i, j, i-1, j+1)
        addEdge(graph, w, i, j, i, j-1)
        addEdge(graph, w, i, j, i, j+1)
        addEdge(graph, w, i, j, i+1, j-1)
        addEdge(graph, w, i, j, i+1, j)
        addEdge(graph, w, i, j, i+1, j+1)

# print(graph)
for kv in graph:
    print(f"{kv} -> {graph[kv]}")

for (i,k) in graph.keys():
    if(k == 'X'):
        print(f"i: {i}, k: {k} -> {findNextKey(graph[(i,k)],'M')}")