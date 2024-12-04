
with open("day04-data.txt", 'r') as file:
    rows = [row.strip() for row in file.readlines()]

############# PART 1 #############
def checkForXMASaroundLetter(i,j):
    amount = 0
    if(not(i-3 < 0)): #Up available
        if rows[i-1][j] == 'M' and rows[i-2][j] == 'A' and rows[i-3][j] == 'S': amount += 1
    if(not(i-3 < 0 or j+3 >= len(rows[i]))): #Up right available
        if rows[i-1][j+1] == 'M' and rows[i-2][j+2] == 'A' and rows[i-3][j+3] == 'S': amount += 1 
    if(not(j+3 >= len(rows[i]))): #Right available
        if rows[i][j+1] == 'M' and rows[i][j+2] == 'A' and rows[i][j+3] == 'S': amount += 1 
    if(not(i+3 >= len(rows) or j+3 >= len(rows[i]))): #Down right available
        if rows[i+1][j+1] == 'M' and rows[i+2][j+2] == 'A' and rows[i+3][j+3] == 'S': amount += 1 
    if(not(i+3 >= len(rows))): #Down available
        if rows[i+1][j] == 'M' and rows[i+2][j] == 'A' and rows[i+3][j] == 'S': amount += 1 
    if(not(i+3 >= len(rows) or j-3 < 0)): #Down left available
        if rows[i+1][j-1] == 'M' and rows[i+2][j-2] == 'A' and rows[i+3][j-3] == 'S': amount += 1 
    if(not(j-3 < 0)): #Left available
        if rows[i][j-1] == 'M' and rows[i][j-2] == 'A' and rows[i][j-3] == 'S': amount += 1 
    if(not(i-3 < 0 or j-3 < 0)): #Up left available
        if rows[i-1][j-1] == 'M' and rows[i-2][j-2] == 'A' and rows[i-3][j-3] == 'S': amount += 1 
    return amount

pt1 = 0

for i, v in enumerate(rows):
    for j, w in enumerate(v):
        if(w == 'X'):
            pt1 += checkForXMASaroundLetter(i,j)

print(f"pt1: {pt1}")

############# PART 2 #############
def checkForWeirdXMAS(i,j):
    if(rows[i-1][j-1] == 'M' and rows[i+1][j+1] == 'S' and rows[i-1][j+1] == 'M' and rows[i+1][j-1] == 'S') : return 1 #M top
    if(rows[i-1][j+1] == 'M' and rows[i+1][j-1] == 'S' and rows[i+1][j+1] == 'M' and rows[i-1][j-1] == 'S') : return 1 #M right
    if(rows[i+1][j-1] == 'M' and rows[i-1][j+1] == 'S' and rows[i+1][j+1] == 'M' and rows[i-1][j-1] == 'S') : return 1 #M bot
    if(rows[i-1][j-1] == 'M' and rows[i+1][j+1] == 'S' and rows[i+1][j-1] == 'M' and rows[i-1][j+1] == 'S') : return 1 #M left
    return 0

pt2 = 0

for i in range(1,len(rows)-1):
    for j in range(1,len(rows[i])-1):
        if(rows[i][j] == 'A'):
            pt2 += checkForWeirdXMAS(i,j)

print(f"pt2: {pt2}")