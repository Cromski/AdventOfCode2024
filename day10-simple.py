with open("day10-data.txt", 'r') as file:
    rows = [list(map(int,row.strip())) for row in file.readlines()]

countPt1, countPt2 = 0, 0

############# PART 1 & 2 #############
def theAlg(y,x,prevNum, knownLocations):
    global countPt1, countPt2
    try:
        if x < 0 or y < 0 or x >= len(rows[y]) or y >= len(rows): return 
    except:
        return 
    
    if prevNum != rows[y][x]-1: return 
    
    if rows[y][x] == 9:
        countPt2+=1
        if ((y,x) not in knownLocations):
            knownLocations.append((y,x))
            countPt1 +=1
    
    theAlg(y-1,x,prevNum+1, knownLocations)
    theAlg(y,x+1,prevNum+1, knownLocations)
    theAlg(y+1,x,prevNum+1, knownLocations)
    theAlg(y,x-1,prevNum+1, knownLocations)

for i,r in enumerate(rows):
    for j, num in enumerate(r):
        if(num == 0):
            theAlg(i,j,-1,[])

print(f"pt1: {countPt1}")
print(f"pt2: {countPt2}")
