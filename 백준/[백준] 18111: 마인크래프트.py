import sys
import math
from collections import Counter
input = sys.stdin.readline

n, m, b = map(int, input().split())
ground = []
ans_cost = math.inf
ans_height = 0
max_height = 256

for _ in range(n):
    ground += list(map(int, input().split()))

counter = Counter(ground)

for height in range(max_height + 1):
    put_block = 0  #놓아야 하는 블록 수
    get_block = 0  #제거해야 하는 블록 수

    for block, cnt in counter.items():
        # 블록 제거
        if block >= height:
            get_block += (block - height) * cnt
        # 블록 설치
        else:
            put_block += (height - block) * cnt

    #가지고 있는 블록 수보다 놓아야 할 블록 수가 많은 경우는 체크하지 않는다.
    if get_block + b < put_block:
        continue

    cost = get_block * 2 + put_block

    if cost <= ans_cost:
        ans_cost = cost
        ans_height = height

print(ans_cost, ans_height)