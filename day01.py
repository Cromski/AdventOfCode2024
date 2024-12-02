import re
from functools import reduce
with open("day01data.txt", 'r') as file:
    rows = [row.strip() for row in file.readlines()]

############# PART 1 #############
left = []
right = []
for row in rows:
    left.append(int(re.findall(r"\d+", row)[0]))
    right.append(int(re.findall(r"\d+", row)[1]))
left.sort()
right.sort()

pt1 = reduce(lambda acc, b: acc+abs(left[b]-right[b]), list(range(len(left))), 0)
print(f"pt1: {pt1}")

############# PART 2 #############

pt2 = reduce(lambda acc, b: left[b]*right.count(left[b])+acc, list(range(len(left))), 0)
print(f"pt2: {pt2}")
