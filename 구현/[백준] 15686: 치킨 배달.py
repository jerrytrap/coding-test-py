from itertools import combinations
import math
def calc_dis(start, target):
    return abs(start[0] - target[0]) + abs(start[1] - target[1])

def calc_chicken_dis(start, chicken_list):
    return min(calc_dis(start, target) for target in chicken_list)

n, m = map(int, input().split())
maps = []
houses = []
chickens = []
ans = math.inf

for _ in range(n):
    maps.append(list(map(int, input().split())))

#집, 치킨집 좌표 저장
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            houses.append((i, j))
        elif maps[i][j] == 2:
            chickens.append((i, j))

#치킨집을 m개 고르는 경우의 수 모두 체크
for chicken in combinations(chickens, m):
    chicken_dis = 0
    for house in houses:
        chicken_dis += calc_chicken_dis(house, chicken)

    ans = min(ans, chicken_dis)

print(ans)
