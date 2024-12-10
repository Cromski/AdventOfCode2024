with open("day10-data.txt", 'r') as file:
    rows = [list(map(int,row.strip())) for row in file.readlines()]

############# PART 1 #############
def theAlgPt1(y,x,prevNum, knownLocations):
    count = 0
    try:
        if x < 0 or y < 0 or x >= len(rows[y]) or y >= len(rows): return 0
    except:
        return 0
    
    if(prevNum != -1):
        if prevNum != rows[y][x]-1: return 0
        
        if rows[y][x] == 9:
            if ((y,x) in knownLocations):
                return 0
            else:
                knownLocations.append((y,x))
                return 1
    
    count += theAlgPt1(y-1,x,prevNum+1, knownLocations)
    count += theAlgPt1(y,x+1,prevNum+1, knownLocations)
    count += theAlgPt1(y+1,x,prevNum+1, knownLocations)
    count += theAlgPt1(y,x-1,prevNum+1, knownLocations)
    return count

def getResPt1():
    res = 0
    for i,r in enumerate(rows):
        for j, num in enumerate(r):
            if(num == 0):
                res += theAlgPt1(i,j,-1,[])
    return res

pt1 = getResPt1()
print(f"pt1: {pt1}")

############# PART 2 #############

def theAlgPt2(y,x,prevNum):
    count = 0
    try:
        if x < 0 or y < 0 or x >= len(rows[y]) or y >= len(rows): return 0
    except:
        return 0
    if(prevNum != -1):
        if prevNum != rows[y][x]-1: return 0
        if rows[y][x] == 9: return 1

    count += theAlgPt2(y-1,x,prevNum+1)
    count += theAlgPt2(y,x+1,prevNum+1)
    count += theAlgPt2(y+1,x,prevNum+1)
    count += theAlgPt2(y,x-1,prevNum+1)
    return count

def getResPt2():
    res = 0
    for i,r in enumerate(rows):
        for j, num in enumerate(r):
            if(num == 0):
                res += theAlgPt2(i,j,-1)
    return res

pt2 = getResPt2()
print(f"pt2: {pt2}")