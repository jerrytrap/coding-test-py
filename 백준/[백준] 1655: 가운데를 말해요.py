import sys
import heapq
input = sys.stdin.readline

n = int(input())
left = [] # 중간값보다 작거나 같은 수를 담을 heap (최대 힙)
right = [] # 중간값보다 큰 수를 담을 heap (최소 힙)

for i in range(n):
    num = int(input())

    # left와 right의 길이를 같게 유지하기 위해 번갈아 넣어주기
    if i % 2 == 0:
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right,  num)

    # left의 최댓값이 right의 최솟값보다 클 때 자리 바꿔주기
    if right and -left[0] > right[0]:
        left_top = -heapq.heappop(left)
        right_top = heapq.heappop(right)
        heapq.heappush(left, -right_top)
        heapq.heappush(right, left_top)

    print(-left[0])
