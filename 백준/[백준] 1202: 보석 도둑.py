import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
answer = 0
idx = 0 # 체크할 보석 번호
candidates = [] # 현재 담을 수 있는 보석 후보들

# 보석을 무게 순으로 정렬
jewels.sort()

# 가방을 무게 순으로 정렬
bags.sort()

# 가장 작은 가방부터 보석을 담음
for bag in bags:
    # 가장 가벼운 보석부터 체크하면서, 담을 수 있는 무게라면 후보에 추가
    while idx < n and jewels[idx][0] <= bag:
        heapq.heappush(candidates, -jewels[idx][1])
        idx += 1

    # 가장 가치가 높은 보석 선택
    if candidates:
        v = -heapq.heappop(candidates)
        answer += v

print(answer)
