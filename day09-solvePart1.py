

with open("day09-data.txt", 'r') as file:
    rows = file.readline().strip()
# rows = '1310632'
# print(rows)

# longThing = [(0, 2), (9, 2), (8, 1), (1, 3), (8, 3), (2, 1), (7, 3), (3, 3), (6, 1), (4, 2), (6, 1), (5, 4), (6, 1), (6, 1), ('.', 14)]
longThing = []
dingo = 0
for i,c in enumerate(rows):
    if i % 2 == 0:
        longThing.append((dingo,int(c)))
    else: 
        longThing.append(('.',int(c)))
    if i % 2 == 0:
        dingo +=1

longThing.append(('.',0))
# longThing = [(0, 2), (9, 2), (8, 1), (1, 3), (8, 3), (2, 1), (7, 3), (3, 3), (6, 1), (4, 2), (6, 1), (5, 4), (6, 1), (6, 1), ('.', 14), (5, 3), ('.', 3), (8, 6), ('.', 3)]
pointer = len(longThing)-2

def swap(lst,tIndex,tuple):
    global longThing, pointer
    (t1,t2) = tuple
    if t1 == '.': 
        longThing[-1] = ('.',longThing[-1][1]+t2)
        longThing.pop(tIndex)
        return
    for i, (v1,v2) in enumerate(lst):
        if i == tIndex:
            longThing[tIndex] = tuple
            return
        deltaSpace = v2-t2
        if v1 == '.':
            if v2 == 0:
                longThing.pop(i)
                return
            if deltaSpace == 0:
                longThing[i] = (t1,t2)
                longThing[-1] = (longThing[-1][0],longThing[-1][1]+t2)
                longThing.pop(tIndex)
                return
            elif deltaSpace > 0:
                longThing[i] = (v1,deltaSpace)
                longThing[-1] = (longThing[-1][0],longThing[-1][1]+t2)
                longThing.pop(tIndex)
                longThing.insert(i,(t1,t2))
                return
            elif deltaSpace < 0:
                longThing[i] = (t1,v2)
                longThing[-1] = (longThing[-1][0],longThing[-1][1]+t2+deltaSpace)
                longThing[tIndex] = (t1,t2-v2)
                print(f"swap({t1,abs(deltaSpace)})")
                swap(longThing,tIndex,(t1,abs(deltaSpace)))
                return
        

#     print(longThing)
# longThing = [(3,3),('.',1),(4,2),('.',1),(5,4),('.',1),(6,6),('.',10)]
# pointer = len(longThing)-2
# print(longThing)
# for i,(v1,v2) in enumerate(longThing[:-1]):
#     if v1 == '.':
#         swap(longThing,pointer,longThing[pointer])
#         pointer = len(longThing)-2

# print(longThing)

# v = len(longThing)-2

for i,(v1,v2) in enumerate(longThing[:-1]):
    if v1 == '.':
        swap(longThing,pointer,longThing[pointer])
        pointer = len(longThing)-2

# print(longThing)
counter = 0
pt1 = 0

for v1,v2 in longThing:
    if v1 == '.': continue
    for i in range(int(v2)):
        toAdd = v1*counter
        pt1 += toAdd
        counter +=1
print(longThing)
print(f"pt1: {pt1}")

