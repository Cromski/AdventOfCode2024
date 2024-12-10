

with open("day09-data.txt", 'r') as file:
    rows = file.readline().strip()

# print(rows)

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
pointer = len(longThing)-2

def swap(lst,tIndex,tuple):
    global longThing, pointer
    (t1,t2) = tuple
    if t1 == '.': 
        longThing[-1] = ('.',longThing[-1][1]+t2)
        longThing.pop(tIndex)
        return
    for i, (v1,v2) in enumerate(lst):
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
                print(f"swap({t1,abs(deltaSpace)})")
                swap(longThing,tIndex,(t1,abs(deltaSpace)))
                return
        

    # print(longThing)
# longThing = [(0, 2), (9, 2), ('.', 1), (1, 3), ('.', 0), (2, 1), ('.', 3), (3, 3), ('.', 1), (4, 2), ('.', 1),
#               (5, 4), ('.', 1), (6, 4), ('.', 1), (7, 3), ('.', 1), (8, 4), ('.', 0), ('.', 2)]
# print(longThing)
# swap(longThing, len(longThing)-2, longThing[len(longThing)-2])
# print(longThing[pointer])


for i,(v1,v2) in enumerate(longThing[:-1]):
    # if i >= pointer: break TODO BREAK AT GOOD POINT
    if v1 == '.':
        swap(longThing,pointer,longThing[pointer])
        pointer = len(longThing)-2


print(longThing)
# longThing = [0, 0, '.', '.', '.', 1, 1, 1, '.', '.', '.', 2, '.', '.', '.', 3, 3, 3, '.', 4, 4, '.', 5, 5, 5, 5, '.', 6, 6, 6, 6, '.', 7, 7, 7, '.', 8, 8, 8, 8, 9, 9]
# swap(2,len(longThing)-1)

# def isDone(lst):
#     foundDot = False
#     for c in lst:
#         if c == '.':
#             foundDot = True
#         elif foundDot and type(c) == int:
#             return False
#     return True

# # print(isDone([0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]))

# def doTheThings():
#     global longThing
#     fromLeft = 0
#     fromRight = len(longThing)-1
#     for c in longThing:
#         # print(f"left: {fromLeft} - right: {fromRight}")
#         if isDone(longThing): break
#         if type(c) == int:
#             fromLeft += 1
#             continue
#         while longThing[fromRight] == '.': fromRight -=1
#         swap(fromLeft,fromRight)
#         fromLeft +=1

# doTheThings()

# def getRes(lst):
#     res = 0
#     for i,v in enumerate(lst):
#         if type(v) != int: break
#         res += i*v
#     return res


# print(getRes(longThing))
