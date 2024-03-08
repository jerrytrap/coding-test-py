import sys
import heapq
input = sys.stdin.readline

priority_queue = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x == 0:
        if priority_queue:
            print(heapq.heappop(priority_queue)[1])
        else:
            print(0)
    else:
        heapq.heappush(priority_queue, (abs(x), x))
