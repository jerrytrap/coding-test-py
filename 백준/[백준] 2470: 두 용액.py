import sys
from math import inf
input = sys.stdin.readline

n = int(input())
info = list(map(int, input().split()))
answer = []
min_sum = inf

info.sort()

start = 0
end = n - 1

while start < end:
    current_sum = info[start] + info[end]

    # 0에 가까워야 하므로 두 수의 합의 절댓값 체크
    if abs(current_sum) < min_sum:
        min_sum = abs(current_sum)
        answer = (info[start], info[end])

    if current_sum < 0:
        start += 1
    elif current_sum > 0:
        end -= 1
    else:
        break

print(*answer)
