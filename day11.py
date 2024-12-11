import functools, time

start_time = time.time()
with open("day11-data.txt", 'r') as file:
    stones = list(map(int,file.readline().strip().split()))

@functools.cache
def blinkSingleStone(blinks,stone):
    if blinks == 0:
        return 1
    else:
        res = 0
        if stone == 0: res += blinkSingleStone(blinks-1,1)
        elif len(str(stone)) % 2 == 0:
            res += blinkSingleStone(blinks-1,int(str(stone)[:len(str(stone))//2]))
            res += blinkSingleStone(blinks-1,int(str(stone)[len(str(stone))//2:]))
        else: res += blinkSingleStone(blinks-1,stone*2024)
        return res

def doIt(blinks):
    totalStones = 0
    for stone in stones:
        totalStones += blinkSingleStone(blinks,stone)
    return totalStones

print(f"pt1: {doIt(25)}, Time: {time.time() - start_time}")
print(f"pt2: {doIt(75)}, Time: {time.time() - start_time}")