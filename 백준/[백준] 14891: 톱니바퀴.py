import sys
input = sys.stdin.readline

gears = []
answer = 0

def rotate_gear(gear, way):
    if way == -1:
        return gear[1:] + gear[0]
    else:
        return gear[7] + gear[:7]

def check_left(gear_num, rotated):
    return gear_num != 0 and not rotated[gear_num - 1] and gears[gear_num][6] != gears[gear_num - 1][2]

def check_right(gear_num, rotated):
    return gear_num != 3 and not rotated[gear_num + 1] and gears[gear_num][2] != gears[gear_num + 1][6]

def check_near_gear(gear_num, way, rotated, info):
    if check_left(gear_num, rotated):
        info.append((gear_num - 1, -way))
        rotated[gear_num - 1] = True
        check_near_gear(gear_num - 1, -way, rotated, info)

    if check_right(gear_num, rotated):
        info.append((gear_num + 1, -way))
        rotated[gear_num + 1] = True
        check_near_gear(gear_num + 1, -way, rotated, info)

for _ in range(4):
    gears.append(input().strip())

k = int(input())

for _ in range(k):
    info = []
    gear_num, way = map(int, input().split())
    gear_num -= 1
    rotated = [False] * 4
    rotated[gear_num] = True

    info.append((gear_num, way))
    check_near_gear(gear_num, way, rotated, info)

    for g, w in info:
        gears[g] = rotate_gear(gears[g], w)

score = 1
for g in gears:
    answer += int(g[0]) * score
    score *= 2

print(answer)
