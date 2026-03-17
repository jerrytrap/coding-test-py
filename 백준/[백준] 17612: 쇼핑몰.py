import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
info = [tuple(map(int, input().split())) for _ in range(n)]
counters = [(0, x, 0) for x in range(1, k + 1)] # (끝나는 시간, 계산대 번호, 고객 번호)
out = [] # 쇼핑몰을 빠져나오는 고객 정보

for id, w in info:
    prev_end_time, counter_number, prev_id = heapq.heappop(counters)

    end_time = prev_end_time + w
    heapq.heappush(counters, (end_time, counter_number, id)) # 계산할 때는 계산대 번호가 작은 순서
    heapq.heappush(out, (end_time, -counter_number, id)) # 계산을 마치고 나갈 때는 계산대 번호가 큰 순서

answer = 0
i = 1
while out:
    _, _, id = heapq.heappop(out)

    answer += id * i
    i += 1

print(answer)
