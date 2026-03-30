import sys
from math import inf
input = sys.stdin.readline

n, m = map(int, input().split())
times = list(map(int, input().split()))
min_size = inf

start = max(times)
end = sum(times)

while start <= end:
    mid = (start + end) // 2
    count = 1 # 필요한 블루레이의 개수
    tmp = 0 # 한 블루레이에 녹화 중인 강의들의 크기 임시로 기록

    for time in times:
        # 블루레이에 계속 담을 수 있는 경우
        if mid - tmp >= time:
            tmp += time
        # 크기를 초과해 새 블루레이에 담아야 하는 경우
        else:
            tmp = time
            count += 1

    if count <= m:
        min_size = min(min_size, mid)
        end = mid - 1
    else:
        start = mid + 1

print(min_size)
