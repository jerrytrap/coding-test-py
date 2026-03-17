import sys
import heapq
input = sys.stdin.readline

n = int(input())
info = []
select = []
answer = 0

# 입력 데이터를 집 -> 사무실 방향으로 통일
for _ in range(n):
    p1, p2 = map(int, input().split())

    info.append((p1, p2) if p1 < p2 else (p2, p1))

d = int(input())

info.sort(key=lambda x: x[1])

for start, end in info:
    # 거리가 d보다 크다면 포함될 수 없으므로 제외
    if end - start > d:
        continue

    # 선분의 끝이 end일 때 시작 지점
    range_start = end - d

    heapq.heappush(select, start)

    # 선분의 시작 지점보다 먼저 시작하는 경우는 제외
    while select and select[0] < range_start:
        heapq.heappop(select)

    answer = max(answer, len(select))

print(answer)
