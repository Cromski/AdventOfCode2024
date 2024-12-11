import functools, time

start_time = time.time()
with open("day11-data.txt", 'r') as file:
    stones = list(map(int,file.readline().strip().split()))

@functools.cache
def blink_single_stone(blinks, stone):
    if blinks == 0:
        return 1
    else:
        res = 0
        if stone == 0: res += blink_single_stone(blinks-1,1)
        elif len(str(stone)) % 2 == 0:
            res += blink_single_stone(blinks-1,int(str(stone)[:len(str(stone))//2]))
            res += blink_single_stone(blinks-1,int(str(stone)[len(str(stone))//2:]))
        else: res += blink_single_stone(blinks-1,stone*2024)
        return res

def do_the_blinks(blinks):
    total_stones = 0
    for stone in stones:
        total_stones += blink_single_stone(blinks, stone)
    return total_stones

print(f"pt1: {do_the_blinks(25)}, Time: {time.time() - start_time}")
print(f"pt2: {do_the_blinks(75)}, Time: {time.time() - start_time}")
