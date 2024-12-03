import re 

############# PART 1 #############
def flatten(lst):
    flattenedLst = []
    for l in lst:
        for tup in l:
            flattenedLst.append(tup)
    return flattenedLst

with open("day03data.txt", 'r') as file:
    rows = flatten([re.findall(r"mul\((\d+),(\d+)\)", row.strip()) for row in file.readlines()])

pt1 = sum([int(tup1)*int(tup2) for tup1,tup2 in rows])

print(f"pt1: {pt1}")

############# PART 2 #############
with open("day03data.txt", 'r') as file:
    rows = flatten([re.findall(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))", row.strip()) for row in file.readlines()])

def removeDonts(line):
    fixedRow = []
    dont = False
    for v1,v2,v3,v4 in line:
        if(v3 == "don't()"):
            dont = True
            continue
        elif(v4 == "do()"):
            dont = False
            continue
        if(not dont):
            fixedRow.append((v1,v2))
    return fixedRow

pt2 = sum([int(tup1)*int(tup2) for tup1,tup2 in removeDonts(rows)])

print(f"pt2: {pt2}")