import time, re

start_time = time.time()
with open("day13-data.txt", 'r') as file:
    rows = [list(map(int,re.findall(r"(\d+)", row.strip()))) for row in file.readlines()]

tokens = 0
for i in range(0,len(rows),4):
    for a in range(100):
        for b in range(100):
            if a*rows[i][0]+b*rows[i+1][0] == rows[i+2][0] and a*rows[i][1]+b*rows[i+1][1] == rows[i+2][1]:
                tokens += a*3+b
                break

print(f"tokens: {tokens}, Time: {time.time() - start_time}")