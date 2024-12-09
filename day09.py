

with open("day09-data.txt", 'r') as file:
    rows = file.readline().strip()

print(rows)

longThing = []
dingo = 0
for i,c in enumerate(rows):
    for j in range(int(c)):
        if i % 2 == 0:
            longThing.append(dingo)
        else: 
            longThing.append('.')
    if i % 2 == 0:
        dingo +=1

def swap(i1,i2):
    global longThing
    temp = longThing[i1]
    longThing[i1] = longThing[i2]
    longThing[i2] = temp
    print(longThing)
# print(longThing)
# longThing = [0, 0, '.', '.', '.', 1, 1, 1, '.', '.', '.', 2, '.', '.', '.', 3, 3, 3, '.', 4, 4, '.', 5, 5, 5, 5, '.', 6, 6, 6, 6, '.', 7, 7, 7, '.', 8, 8, 8, 8, 9, 9]
# swap(2,len(longThing)-1)

def isDone(lst):
    foundDot = False
    for c in lst:
        if c == '.':
            foundDot = True
        elif foundDot and type(c) == int:
            return False
    return True

# print(isDone([0, '.', '.', 1, 1, 1, '.', '.', '.', '.', 2, 2, 2, 2, 2]))

def doTheThings():
    global longThing
    fromLeft = 0
    fromRight = len(longThing)-1
    for c in longThing:
        # print(f"left: {fromLeft} - right: {fromRight}")
        if isDone(longThing): break
        if type(c) == int:
            fromLeft += 1
            continue
        while longThing[fromRight] == '.': fromRight -=1
        swap(fromLeft,fromRight)
        fromLeft +=1

doTheThings()

def getRes(lst):
    res = 0
    for i,v in enumerate(lst):
        if type(v) != int: break
        res += i*v
    return res


print(getRes(longThing))