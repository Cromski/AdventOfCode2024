from collections import defaultdict

rules = defaultdict(list)
updates = []

with open("day05-data.txt", 'r') as file:
    rows = [row.strip() for row in file.readlines()]

#print(rows)

x = "rules"
for r in rows:
    if r == '': 
        x = "updates"
        continue
    match x:
        case "rules":
            kv = r.split('|')
            k,v = kv[0],kv[1]
            rules[k].append(v)
        case "updates":
            updates.append(r)
        case _:
            pass

# for r in rules.keys():
#     print(f"K: {r} -> Values: {rules[r]}")

#print(updates)

validUpdates = []

def isNumberLegal(numToCheck, keyNumbers):
    for ruleKey in keyNumbers:
        if numToCheck in rules[ruleKey]:
            return (False,keyNumbers.index(ruleKey))
    return (True,-1)


# print("AAAAAAAAAAAAA")
# print(f"end: {isNumberLegal('13',['75','29','47'])}")
# print("AAAAAAAAAAAAA")

def isUpdateValid(s):
    keyNumbers = s.split(",")
    for i in range(len(keyNumbers)-1):
        tf,_= isNumberLegal(keyNumbers[i],keyNumbers[i+1:])
        if tf:
            continue
        else:
            return False
    return True

for update in updates:
    if isUpdateValid(update):
        validUpdates.append(update)

def getSumOfMiddleNumbers(lst):
    sum = 0
    for v in lst:
        keyNumbers = v.split(",")
        sum += int(keyNumbers[int(len(keyNumbers)/2)])
    return(sum)

#print(validUpdates)
pt1 = getSumOfMiddleNumbers(validUpdates)
print(f"pt1: {pt1}")

def swapListValues(lst, i1,i2):
    temp = lst[i1]
    lst[i1] = lst[i2]
    lst[i2] = temp
    return lst

# print("AAAAAAAAAAAAA")
# print(swapListValues(['75','97','47','61','53'], 0,1))
# print("AAAAAAAAAAAAA")


# def fixShittyUpdate(u):
#     update = u.split(",")
#     for i in range(len(update)):
#         print(update)
#         if not (isNumberLegal(update[i],update[i+1:])):
#             update = swapListValues(update,i,i+1)
#             i = 0
#     return update
def fixShittyUpdate(u):
    update = u.split(",")
    i = 0
    while not isUpdateValid(",".join(update)):
        # print(update)
        try:
            tf,index = isNumberLegal(update[i],update[i+1:])
        except:
            print(f"update: {update}")
            print(f"i: {i}") #this becomes infinityyyyyyyyyyyyyyyyyyyyyyyy
        if not (tf):
            update = swapListValues(update,i,index+i+1)
            i = 0
        i+=1
    return update

nonOrderedUpdates = [update for update in updates if update not in validUpdates]

#print(nonOrderedUpdates)
fixedUpdates = []
for nonOrderedUpdate in nonOrderedUpdates:
    fixedUpdates.append(",".join(fixShittyUpdate(nonOrderedUpdate)))

#print(fixedUpdates)

pt2 = getSumOfMiddleNumbers(fixedUpdates)

print(f"pt2: {pt2}")

# print("AAAAAAAAAAAAA")
# print(f"end: {fixShittyUpdate('97,13,75,29,47')}")
# print("AAAAAAAAAAAAA")
