import time, re

start_time = time.time()
with open("day14-data.txt", 'r') as file:
    rows = [list(map(int,re.findall(r"(-?\d+)", row.strip()))) for row in file.readlines()]

width = 101
height = 103

map = [[ 0 for x in range(width)] for v in range(height)]
def print_map(map):
    for x in map:
        print(x)

def teleport_robots(data, seconds):
    for px, py, vx, vy in data:
        x_pos_after_tp = (px+vx*seconds)%width
        y_pos_after_tp = (py+vy*seconds)%height
        map[y_pos_after_tp][x_pos_after_tp] = map[y_pos_after_tp][x_pos_after_tp]+1

teleport_robots(rows,100)

def get_res(this_map):
    safety_factor_q1 = 0
    safety_factor_q2 = 0
    safety_factor_q3 = 0
    safety_factor_q4 = 0
    #top left quadrant
    for x in this_map[:height//2]:
        for y in x[:width//2]:
            safety_factor_q1 += y
    # bottom left
    for x in this_map[(height//2)+1:]:
        # print(x[:width//2])
        for y in x[:width//2]:
            safety_factor_q2 += y
    #bottom right
    for x in this_map[(height//2)+1:]:
        # print(x[(width//2)+1:])
        for y in x[(width//2)+1:]:
            safety_factor_q3 += y
    # top right
    for x in this_map[:(height//2)]:
        # print(x[(width//2)+1:])
        for y in x[(width//2)+1:]:
            safety_factor_q4 += y
    return safety_factor_q1*safety_factor_q2*safety_factor_q3*safety_factor_q4


pt1 = get_res(map)
print(f"pt1: {pt1}, Time: {time.time() - start_time}")

def reset_map():
    global map
    map = [[ 0 for x in range(width)] for v in range(height)]

def is_there_xmas_tree(map):
    for row in map:
        if '111111111111' in ''.join(str(x) for x in row):
            return True
    return False

counter = 0
reset_map()
teleport_robots(rows, 0)
while is_there_xmas_tree(map) == False:
    counter+=1
    reset_map()
    teleport_robots(rows, counter)

print(f"pt2: {counter}, Time: {time.time() - start_time}")
