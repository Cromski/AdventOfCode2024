from functools import reduce
with open("day02data.txt", 'r') as file:
    reports = [row.strip().split() for row in file.readlines()]

############# PART 1 #############
def isSafe(lev):
    level = list(map(int, lev))
    currentValue = level[0]
    shouldIncrease = currentValue < level[1]
    for v in level[1:]:
        if(shouldIncrease and v-currentValue >= 1 and v-currentValue <= 3):
            currentValue = v
        elif(not shouldIncrease and currentValue-v >= 1 and currentValue-v <= 3):
            currentValue = v
        else:
            return False
    return True

pt1 = reduce(lambda acc, b: acc+1 if isSafe(b) else acc, reports, 0)
print(f"pt1: {pt1}")


############# PART 2 #############

def areAllLevelsSafe(lev):
    for ignoreIndex in range(len(lev)):
        if(isSafe(lev[0:ignoreIndex]+lev[ignoreIndex+1:len(lev)])):
            return True
    return False

pt2 = reduce(lambda acc, b: acc+1 if areAllLevelsSafe(b) else acc, reports, 0)
print(f"pt2: {pt2}")
