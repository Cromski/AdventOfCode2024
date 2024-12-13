import time, re

start_time = time.time()
with open("day13-data.txt", 'r') as file:
    rows = [list(map(int,re.findall(r"(\d+)", row.strip()))) for row in file.readlines()]

def solve_machine(machine, small_change):
    tokens = 0
    for i in range(0,len(machine),4):
        a1,a2 = machine[i]
        b1,b2 = machine[i+1]
        c1,c2 = machine[i+2]
        if small_change > 0:
            c1 += small_change
            c2 += small_change
        A=round(((b2*c1-b1*c2)/(a1*b2-a2*b1)), 2)
        B=round(((a1*c2-a2*c1)/(a1*b2-a2*b1)), 2)
        
        if small_change > 0:
            if (A*a1+B*b1,A*a2+B*b2) == (c1,c2):
                tokens += A*3+B
        else:     
            if A <= 100 and B <= 100 and (A*a1+B*b1,A*a2+B*b2) == (c1,c2):
                tokens += A*3+B
    return tokens

pt1 = solve_machine(rows, 0)
pt2 = solve_machine(rows, 10000000000000)
print(f"pt1: {pt1}, Time: {time.time() - start_time}")
print(f"pt2: {pt2}, Time: {time.time() - start_time}")

"""debug prints
    # print(f"a1: {a1}, b1: {b1}, a2: {a2}, b2: {b2}, c1: {c1}, c2: {c2}")
    # print(f"A = ({b2}*{c1}-{b1}*{c2})/({a1}*{b2}-{a2}*{b1})")
    # print(f"B = ({a1}*{c2}-{a2}*{c1})/({a1}*{b2}-{a2}*{b1})")
    # print(A*a1+B*b1)
    # print(A*a2+B*b2)

    # print(f"{(A*a1+B*b1,A*a2+B*b2)}, {c1,c2}")
"""